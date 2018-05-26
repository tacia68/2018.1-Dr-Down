import os.path
import sys
import random
import string

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def create_password():
    '''
    Generates passwords for each user
    '''

    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = ''.join(random.choice(string.ascii_uppercase +
                                     string.ascii_lowercase +
                                     string.digits) for _ in range(9)
                       )
    return password


def create_super_user(username, email):
    '''
    Creates the superuser and ensures that if any error occurs the
    script does not continue
    '''

    password = create_password()
    try:
        u = User.objects.create_superuser(username,
                                          email,
                                          password,
                                          is_active=True)
        EmailAddress.objects.create(
            user=u, email=email,
            primary=True, verified=True)
        u.set_password(password)
        u.save()
        print ('\nSuperUser:', User.objects.get(is_superuser=True).username)
        print('username: {0} -- password: {1} \n'.format(username, password))

        return u

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_user(first_name, last_name, name, username, email, birthday, gender):
    """
    Creates the user and ensures that if any error occurs the
    script does not continue
    """
    password = create_password()
    try:
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            name=name,
            username=username,
            email=email,
            password=password,
            birthday=birthday,
            telephone='(22)22222-2222',
            gender=gender,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            is_active=True,
            has_specialization = False
        )

        # EmailAdress is for validating email confirmation on user creation
        EmailAddress.objects.create(
            user=u, email=email,
            primary=True, verified=True)
        u.save()

        print('User: - {0} {1}'.
              format(str(u.first_name), str(u.last_name)))
        print('username: {0}  -- password: {1} \n'.format(username, password))

        return u

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_patient(user, n, responsible):

    try:
        patients = Patient.objects.create(
            ses='11234561'+str(n),
            user=user,
            mother_name="Janaína Roussef",
            father_name="João das neves",
            ethnicity=3,
            sus_number='1234567891'+str(n),
            civil_registry_of_birth='1234567891'+str(n),
            declaration_of_live_birth='1234567891'+str(n),
            responsible=responsible
        )

        Risk.objects.filter(patient=patients).update(
            patient=patients,
            priority_speech_theraphy = 5,
            priority_psychology = 5,
            priority_physiotherapy = 5,
            priority_neurology = 5,
            priority_cardiology = 5,
            priority_pediatrics = 5,
            priority_general_practitioner = 5,
        )

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_healthteam(user, n, cpf):
    try:
        HealthTeam.objects.create(
            cpf=cpf,
            user=user,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number='123456'+str(n),
            registration_state=HealthTeam.DF,
        )
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_responsible(user, cpf):
    try:
        responsible = Responsible.objects.create(
            cpf=cpf,
            user=user
        )
        return responsible

    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def create_employee(user, cpf):

    try:
        Employee.objects.create(
            cpf=cpf,
            user=user,
            departament=Employee.ADMINISTRATION
        )
    except IntegrityError:
        raise ValidationError("An error occurred. Stopping the script")


def populate():

    print ('\n----------------------')
    print ('Populating Database...')
    print ('----------------------\n')

    create_super_user('admin', 'admin@admin.com')

    print ('\n------------------------')
    print ('Creating Health Teams...')
    print ('------------------------\n')

    healthteam_1 = create_user(
        'Laura',
        'Oliveira',
        'Laura',
        'laura',
        'laura@email.com',
        '1998-04-05',
        'F'
    )

    healthteam_2 = create_user(
        'Maura',
        'Oliveira',
        'Maura',
        'maura',
        'maura@email.com',
        '1998-04-05',
        'F'
    )

    healthteam_3 = create_user(
        'Sara',
        'Oliveira',
        'Sara',
        'sara',
        'sara@email.com',
        '1998-04-05',
        'F'
    )

    create_healthteam(healthteam_1, 1, '326.763.330-38')
    create_healthteam(healthteam_2, 2, '875.076.060-23')
    create_healthteam(healthteam_3, 3, '452.347.400-13')

    print ('\n------------------------')
    print ('Creating Responsibles...')
    print ('------------------------\n')

    responsible_1 = create_user(
        'José',
        'Vaz',
        'José',
        'jose',
        'jose@email.com',
        '1998-04-05',
        'M'
    )

    responsible_2 = create_user(
        'Ana',
        'Vitória',
        'Ana',
        'ana',
        'ana@email.com',
        '1998-04-05',
        'F'
    )

    responsible_3 = create_user(
        'Júlio',
        'Tavares',
        'Júlio',
        'julio',
        'julio@email.com',
        '1998-04-05',
        'M'
    )

    responsible1 = create_responsible(responsible_1, "902.876.510-70")
    responsible2 = create_responsible(responsible_2, "715.643.220-68")
    responsible3 = create_responsible(responsible_3, "445.821.390-35")

    print ('\n----------------------')
    print ('Creating Patients...')
    print ('----------------------\n')

    print ('(Minnor)')
    patient_3 = create_user(
        'Enzo',
        'Gabriel',
        'Enzo',
        'enzo',
        'enzo@email.com',
        timezone.now() - timezone.timedelta(days=3650),
        'M',
    )

    print ('(Minnor)')
    patient_4 = create_user(
        'Valentina',
        'Valente',
        'Valentina',
        'valentina',
        'valentina@email.com',
        timezone.now() - timezone.timedelta(days=1),
        'F'
    )

    print ('(18+)')
    patient_1 = create_user(
        'Gabriel',
        'dos Santos',
        'Gabriel',
        'gabriel',
        'gabriel@email.com',
        '1998-04-05',
        'M'
    )

    print ('(18+)')
    patient_2 = create_user(
        'Carla',
        'Júlia',
        'Carla',
        'carla',
        'carla@email.com',
        '1998-04-05',
        'F'
    )

    print ('(Minnor)')
    patient_5 = create_user(
        'Bia',
        'Falcão',
        'Bianca',
        'bianca',
        'bianca@email.com',
        timezone.now() - timezone.timedelta(days=1),
        'F'
    )

    print ('(18+)')
    patient_6 = create_user(
        'Nathan',
        'Vilela',
        'Nathan',
        'nathan',
        'nathan@email.com',
        '1998-04-05',
        'M'
    )

    create_patient(patient_3, 3, responsible1)
    create_patient(patient_4, 4, responsible2)
    create_patient(patient_5, 5, responsible2)
    create_patient(patient_6, 6, responsible2)
    create_patient(patient_1, 1, None)
    create_patient(patient_2, 2, None)

    print ('\n------------------------')
    print ('Creating Employees...')
    print ('------------------------\n')

    employee_1 = create_user(
        'Pedro',
        'Victor',
        'Pedro',
        'pedro',
        'pedro@email.com',
        '1998-04-05',
        'M'
    )

    employee_2 = create_user(
        'Raíssa',
        'Parente',
        'Raíssa',
        'raissa',
        'raissa@email.com',
        '1998-04-05',
        'F'
    )

    create_employee(employee_1, "112.954.800-77")
    create_employee(employee_2, "832.164.830-45")

    category1 = Category.objects.create(
        name='Medicamentos',
        description='Fórum de discussão sobre medicamentos',
        slug='med',
    )

    post1 = Post.objects.create(
        title="Qual medicamento tomar?",
        message="Tenho dores de cabeça",
        created_by=patient_1,
        category=category1,
    )

    Commentary.objects.create(
        message='Gostaria de saber também',
        post=post1,
        created_by=patient_2,
    )

    category2 = Category.objects.create(
        name='Espaço dos pais',
        description='Um lugar para os pais discutirem e trocarem infrmações',
        slug='event',
    )

    post2 = Post.objects.create(
        title="Meu filho não tá legal",
        message="Ele não fala com ninguém. É normal?",
        created_by=responsible_1,
        category=category2,
    )

    Commentary.objects.create(
        message='O meu conversa com os amigos normalmente. Veja com um médico.',
        post=post2,
        created_by=responsible_2,
    )

    category3 = Category.objects.create(
        name='Dúvidas',
        description='Espaço de dúvidas',
        slug='event',
    )

    post3 = Post.objects.create(
        title="Onde achar um bom site sobre SD?",
        message="Gostaria de achar um site muito bom sobre SD",
        created_by=employee_1,
        category=category3,
    )

    Commentary.objects.create(
        message='Você está nele :D',
        post=post3,
        created_by=employee_2,
    )

    print ('================================================================')
    print ('WARNING:\n')
    print ('All passwords displayed on this terminal '
           'are generated randomly\n and can not be '
           'displayed again. Be sure to save them in '
           'a safe \nplace before continuing, otherwise'
           'you will have to redo the whole\n process.')
    print ('================================================================\n')

    input("I saved the passwords in a safe place (press enter to continue...)")

    print ('\n------------------------------\n')
    print ('Database populated with sucess')
    print ('------------------------------\n')

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from django.utils import timezone
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from drdown.forum.models.model_category import Category
from drdown.forum.models.model_post import Post
from drdown.forum.models.model_commentary import Commentary
from drdown.medicalrecords.models.model_risk import Risk
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from allauth.account.models import EmailAddress

populate()
