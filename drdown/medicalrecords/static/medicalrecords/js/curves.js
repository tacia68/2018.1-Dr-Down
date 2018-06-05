
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

var height_data;
var weight_data;
var bmi_data;
var perimeter_data;

$("#height_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'height',
                'time_frame' : 'months'
            },
            success: function(response){
                height_data = JSON.stringify(response.data);
                
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_HeigthChart);
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#weight_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'weight'
            },
            success: function(response){
                weight_data = JSON.stringify(response.data);
                
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_WeigthChart);
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#bmi_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'bmi'
            },
            success: function(response){
                bmi_data = JSON.stringify(response.data);
                
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_BMIChart);
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#perimeter_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'cephalic_perimeter'
            },
            success: function(response){
                perimeter_data = JSON.stringify(response.data);

                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_PerimeterChart);
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

function convertToArray(string) {

    var json_data = JSON.parse(string);

    var array = []

    json_data.graphic.forEach(element => {
        array.push(element)
    });

    array.forEach(element => {

        var item = element.pop()

        if (item == 0){
            item = null;
        }

        element.push(item);

    });

    //populatePatientCurve(array)

    console.log(array)

    return array
}

var DATA_TYPES = {
    height: 'Height',
    weight: 'Weight',
    bmi: 'BMI',
    perimeter: 'Perimeter'
}

function defineOptions(data_type) {
    
    title = data_type;
    hAxis_title = 'Ages';
    vAxis_title = data_type;
    
    var h_values = [0,0];
    var v_values = [0,0];

    switch (data_type) {
        case DATA_TYPES.height:
            
            v_values[1] = 200;
            
            h_values[1] = 18*12;
            break;
        case DATA_TYPES.weight:
            v_values[1] = 250;


            h_values[1] = 18*12;
            break;
        case DATA_TYPES.bmi:
            v_values[0] = 10;
            v_values[1] = 50;

            h_values[0] = 3;
            h_values[1] = 18;
            break;
        case DATA_TYPES.perimeter:
            v_values[0] = 10;
            v_values[1] = 50;

            h_values[1] = 24;
            break;
    
        default:
            break;
    }

    return {
        title: title,
        curveType: 'function',
        hAxis: {
            title: hAxis_title,
            titleTextStyle: {color: '#333'},
        },
        vAxis: {
            title: vAxis_title,
            titleTextStyle: {color: '#333'},
            format: 'decimal',
            viewWindowMode: 'pretty',
        },
        explorer: {
            actions: ['dragToZoom', 'rightClickToReset'],
            axis: 'horizontal',
            keepInBounds: true,
            maxZoomIn: 4.0
        },
        crosshair: { trigger: 'selection' },
        lineWidth: 2,
        series: {
            0: { color: '#e2431e' },
            1: { color: '#e7711b' },
            2: { color: '#f1ca3a' },
            3: { color: '#6f9654' },
            4: { color: '#1c91c0' },
            5: { color: '#e7711b' },
            6: { color: '#e2431e' },
        },
        is3D: false
    };
}

function draw_HeigthChart() {

    var height_array = convertToArray(height_data)
    var data_height = google.visualization.arrayToDataTable(height_array);
    var options = defineOptions(data_type=DATA_TYPES.height)
    var height_chart = new google.visualization.LineChart(document.getElementById('height_chart'));
    height_chart.draw(data_height, options);

}

function draw_WeigthChart() {

    var weight_array = convertToArray(weight_data)
    var data_weight = google.visualization.arrayToDataTable(weight_array);
    var options = defineOptions(data_type=DATA_TYPES.weight)
    var weight_chart = new google.visualization.LineChart(document.getElementById('weight_chart'));
    weight_chart.draw(data_weight, options);
}

function draw_BMIChart() {

    var bmi_array = convertToArray(bmi_data)
    var data_bmi = google.visualization.arrayToDataTable(bmi_array);
    var options = defineOptions(data_type=DATA_TYPES.bmi)
    var bmi_chart = new google.visualization.LineChart(document.getElementById('bmi_chart'));
    bmi_chart.draw(data_bmi, options);
}

function draw_PerimeterChart() {

    var perimeter_array = convertToArray(perimeter_data)
    var data_perimeter = google.visualization.arrayToDataTable(perimeter_array);
    var options = defineOptions(data_type=DATA_TYPES.perimeter)
    var perimeter_chart = new google.visualization.LineChart(document.getElementById('perimeter_chart'));
    perimeter_chart.draw(data_perimeter, options);

}
