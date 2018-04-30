
# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 24/03/2018 | 0.0.1 | Abertura do documento | Geovana Ramos |
| 26/03/2018 | 0.1.0 | Tópicos 1 e 2 | Guilherme Guy e Gabriela Medeiros |
| 26/03/2018 | 0.2.0 | Tópicos 3 e 4 | Daniel Maike e Joberth Rogers |
| 26/03/2018 | 0.3.0 | Tópicos 5 e 6 | Elias Bernardo e Geovana Ramos |
| 27/03/2018 | 0.3.1 | Correção de informações histórico de revisão | Daniel Maike, Gabriela Medeiros e Joberth Rogers |
| 27/03/2018 | 0.4.0 | Diagrama de classes | Elias Bernardo, Geovana Ramos e Guilherme Guy |
| 28/03/2018 | 0.5.0 | Alteração no tópico 3 | Daniel Maike e Geovana Ramos |
| 28/03/2018 | 0.6.0 | Modelo Entidade Relacionamento | Daniel Maike e Joberth Rogers |
| 28/03/2018 | 0.6.1 | Revisão geral | Daniel Maike e Joberth Rogers |
| 28/03/2018 | 1.0.0 | Entrega da primeira versão estável | Daniel Maike, Elias Bernardo, Joberth Rogers, Guilherme Guy, Gabriela Medeiros e Geovana Ramos |
| 29/03/2018 | 1.0.1 | Revisões gerais | Daniel Maike, Guilherme Guy e Joberth Rogers |
| 29/03/2018 | 1.1.0 | Adição do tópico 2.4 | Geovana Ramos |
| 01/04/2018 | 1.2.0 | Melhorando o tópico de representação arquitetural | Victor Arnaud |
| 01/04/2018 | 1.2.1 | Corrigindo inconsistências | Victor Arnaud |
| 12/04/2018 | 1.3.0 | Modificando para arquitetura baseada em componentes | Victor Arnaud |
| 15/04/2018 | 1.4.0 | Modificando imagem da arquitetura | Victor Arnaud e Geovana Ramos |
| 22/04/2018 | 2.0.0 | Versão 2.0 do Arquitetura e componentes da sprint 07 | Victor Arnaud, Geovana Ramos e Gabriela Medeiros |
| 26/04/2018 | 2.1.0 | Inserindo componentes da sprint 08 | Victor Arnaud |

## 1: Introdução

### 1.1	Finalidade

Este documento tem como finalidade apresentar uma visão geral da arquitetura que será usada no desenvolvimento do projeto e permitir um maior entendimento do sistema Dr. Down e de como ele irá se comportar e se comunicar com as outras aplicações que compõem o projeto. Com o maior detalhamento da arquitetura, espera-se deixar explícitas as decisões arquiteturais feitas pela equipe.

### 1.2	Escopo

Dr. Down será uma ferramenta desenvolvida para gerenciar, auxiliar e facilitar a administração do fluxo de pacientes do CRIS DOWN, além de possibilitar a comunicação entre médicos, pacientes e familiares. O documento apresentará toda a parte arquitetural para a confecção do software Dr. Down, a fim de tornar claras as características arquiteturais do projeto.

### 1.3	Definições, acrônimos e abreviações

| Abreviação | Definição |
|--------|------|
| SD | Síndrome de Down |
| CRIS DOWN |Centro de Referência em Síndrome de Down |
| MDS | Métodos de Desenvolvimento de Software |
| EPS| Engenharia de Produto de Software |
| UnB | Universidade de Brasília |
| SES | Secretaria de Estado de Saúde |
| CBV | Class-Based Views |

## 2: Representação Arquitetural

![Arquitetura](https://uploaddeimagens.com.br/images/001/384/606/full/arquitetura.png?1524422037)

A arquitetura utilizada no projeto será a arquitetura baseada em componentes. O conceito de _Django Application_ é uma das principais inovações do Django e um dos grandes responsáveis por sua flexibilidade e alto reaproveitamento de componentes, ou seja, um aplicação é criada, mantida, executada e distribuída de forma totalmente independente contendo as seguintes características: alta coesão, baixo acoplamento, reutilizável e independente, que representa um contexto de negócio, além de ser externo ao projeto que irá utilizá-lo. Com isso, serão adotadas aplicações que sigam todas essas características e estejam empacotadas no [pypi](https://pypi.python.org/pypi). Cada aplicação do Django utiliza da arquitetura MVT internamente.

A arquitetura baseada em componentes é um ramo de Engenharia de Software, com ênfase na decomposição dos sistemas em componentes independentes, substituíveis e modulares, elas ajudam a gerenciar a complexidade e encorajam a reutilização.

Alguns benefícios desse modelo de arquitetura:

* **Fácil deploy**: Compatibilidade de novas versões quando disponíveis. É possível substituir a versão existente sem impacto em outros componentes do sistema como um todo.

* **Redução de custos**: O uso do componente de terceiros permite a redução do custo do desenvolvimento e manutenção.

* **Fácil desenvolvimento**: Implementar componentes bem como a funcionalidade definida pela interface, permite desenvolvimento sem impacto em outros partes do sistema.

* **Reutilização**: A reutilização de componentes é um meio de agilizar o desenvolvimento e manutenção, reduzindo custos da aplicação.

O projeto terá algumas aplicações externas que serão inseridas e comunicadas com as aplicações do projeto. O framework já disponibiliza toda a estrutura para fazer essa comunicação entre componentes. Porém, serão utilizados microsserviços ou APIs se necessário, com esses se comunicando via requisições HTTP.

Abaixo está listado como a arquitetura do projeto se comunicará com outros serviços externos de configuração, como servidor NGINX, banco de dados PostgreSQL, entre outros. Nos tópicos seguintes será explicado com mais detalhes o funcionamento da arquitetura de cada aplicação presente no projeto Django (MVT) e uma tabela com os possíveis aplicações selecionados para a inserção ou não no projeto.

### 2.1 NGINX:

O NGINX é um servidor web que pode atuar como um proxy reverso para HTTP, HTTPS, SMTP, POP3 e IMAP, bem como um balanceador de carga. O NGINX é um servidor web rápido e com inúmeras possibilidades de configuração para melhor performance.

No projeto ele é utilizado como um redirecionador de portas utilizando-se de proxy reverso para que ambos os arquivos estáticos e o servidor de produção do Django possam compartilhar da mesma porta 80, servindo os arquivos estáticos separados da aplicação.

### 2.2 Django

O Dr.Down será uma aplicação web desenvolvida a partir do framework Django, o qual é escrito em Python. O padrão arquitetural utilizado pelas aplicações do Django é a MVT (Model, View e Template), que é derivada da do padrão arquitetural MVC (Model, View e Controller). De acordo com o DjangoBook, a parte de controller, em Django, é tratada pelo próprio framework. Portanto a View do MVT desempenha um papel próximo, mas não igual ao controller.

Como citado acima, cada aplicação do Django pode ser considerada um componente caso siga todas as características citadas e esteja empacotado e mantido no **pypi**. Para maiores informações: <a href="https://docs.djangoproject.com/pt-br/2.0/intro/reusable-apps/">Tutorial avançado: Como escrever aplicações reutilizáveis</a>

Abaixo explica-se o funcionamento da arquitetura interna de cada aplicação do Django e quais componentes foram selecionados para complementar o projeto.

#### 2.2.1 Model

É uma representação do banco de dados. Além disso, também inclui características, relações e outros comportamentos que os dados podem assumir.

O Django inclui varias ferramentas para automatizar tanto quanto possível o processo e a manipulação do banco de dados, de forma que o desenvolvedor não precise se preocupar tanto com o banco de dados, o que ajuda no foco do desenvolvimento da aplicação de forma mais rápida.

#### 2.2.2 View

Estabelece uma ponte entre a Models e o Templates. Recebe as requisições do usuário a partir do template, acessa o banco de dados e então retorna a informação solicitada pelo usuário, por meio de HTML, XML e/ou os erros encontrados.

#### 2.2.3 Template

Agrega toda a parte visual que estará visível para os usuários. Inclui os códigos HTML, CSS, JavaScript, entre outras linguagens que são utilizadas na apresentação da View ao usuário.

#### 2.2.4 Componentes

Critérios de aceitação de um componente:

1. **Alta coesão**: O componente deve realizar apenas uma tarefa específica e deve ser pequeno.
2. **Baixo acoplamento**: O componente não deve depender de outra classe ou funcionalidade do projeto no qual está sendo inserido.
3. **Independente**: O componente deve ser criado, mantido, executado e distribuído de forma independente, ou seja, deve ter o mínimo de dependência com outros componentes.
4. **Reutilizável**: O componente deve ser reutilizável, ou seja, pode ser inserido em qualquer projeto, independente de seu contexto, e facilmente substituído, se for preciso.
5. **Extensibilidade**: Um componente pode ser estendido a partir de outro componente para fornecer um novo comportamento.
6. **Encapsulamento**: O componente deve expor uma interface para os invocadores utilizarem suas funcionalidades e não revelar detalhes do seu processo interno, das variáveis internas e de seu estado.
7. **Externo ao projeto**: O componente deve estar disponibilizado no **pypi**.
8. **Qualidade**: O componente deve estar testado e ter build funcionando, além de ser completo e estar em uma versão estável.

A cada sprint do projeto será definido a utilização ou não de cada componente disponibilizado nas tabelas abaixo. Os microsserviços e APIs consumidas também serão listados nas tabelas abaixo. As tabelas abaixo está mapeada com a EAP do projeto.

#### Cadastro de usuário (Equipe de Saúde, Paciente, Responsável, Funcionário):

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-allauth](https://www.intenct.nl/projects/django-allauth/)|O django-allauth é um aplicativo Django reutilizável que permite autenticação local e social.|Sim|Ele foi utilizado para a criação do usuário base que será a base para todos os outros usuários do sistema|

#### Informações gerais

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[NewsAPI](https://newsapi.org/s/google-news-api)|API que disponibiliza manchetes, artigos, imagens e outros metadados de artigos do Google Notícias via JSON.|Não|Essa API é complexa e não pega informações especificas que precisamos.|

#### Foruns e discussões

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-forum-app](https://github.com/urtzai/django-forum-app)|Um aplicativo muito simples e minimalista para criar fóruns|Não|Foi proposta no meio da implementação do mesmo, logo foi descartado|

#### Consultas e Eventos

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[pinax-calendars](https://github.com/pinax/pinax-calendars/)|Aplicação django para publicar eventos como um calendario|A decidir|A aplicação ainda está sendo avaliada pela equipe.|
|[django-calendarium](https://github.com/bitlabstudio/django-calendarium)|Um aplicativo Django reutilizável para gerenciar e exibir um calendário em seus modelos.|A decidir|A aplicação ainda está sendo avaliada pela equipe.|
|[django-scheduler](https://github.com/llazzaro/django-scheduler)|Uma aplicação de calendario do django|A decidir|A aplicação ainda está sendo avaliada pela equipe.|
|[django-schedule-thauber](https://github.com/thauber/django-schedule)|Uma aplicação de calendario do django|A decidir|A aplicação ainda está sendo avaliada|
|[pinax-notifications](https://github.com/pinax/pinax-notifications/)|Gerenciamento de notificação de usuário para o framework web Django|A decidir|A aplicação ainda está sendo avaliada|
|[django-frontend-notification](https://github.com/areski/django-frontend-notification)|Aplicativo Django para exibir no frontend a lista de notificações e executar algumas ações básicas como "visualizar todas as notificações", "excluir notificações", ele também fornece ajudantes para exibir notificações|A decidir|A aplicação ainda está sendo avaliada|
|[django-webline-notifications](https://github.com/alireza-molaee/django-webline-notifications)|É uma biblioteca python, que permite notificar tudo para o(s) usuário(s)|A decidir|A aplicação ainda está sendo avaliada|

#### Ficha de acompanhamento e Relatórios

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-pagedown](https://github.com/timmyomahony/django-pagedown)|Um aplicativo django que permite a fácil adição do editor de marcação "PageDown" do Stack Overflow a um campo de formulário django, seja em um aplicativo personalizado ou no Django Admin.|Sim|O componente está sendo usado no prontuário|
|[django-markdown-deux](https://github.com/trentm/django-markdown-deux)|Componente para evitar a inserção de código malicioso no markdown|Sim|O componente está sendo usado no prontuário|
|[pdf-report](https://github.com/Edinburgh-Genome-Foundry/pdf_reports)|Biblioteca Python e tema CSS para gerar relatórios em PDF a partir de HTML/Pug|A decidir|A aplicação está sendo avaliada pela equipe|
|[django-easy-pdf](https://github.com/nigma/django-easy-pdf)|Visualização de PDF de uma maneira fácil|A decidir|A aplicação está sendo avaliada pela equipe|

#### Localização

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[GoogleMapsAPI](https://developers.google.com/places/web-service/?hl=pt-br)|API do Google Maps com informações sobre milhões de locais|A decidir|A API ainda está sendo avaliada pela equipe.|

#### Outros

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-role-permissions](https://github.com/vintasoftware/django-role-permissions)|É um aplicativo de Django para permissões baseadas em função. Ele é construído sobre as funcionalidades Group e Permission do usuário do Django contrib.auth e não adiciona nenhum outro modelo ao seu projeto, ou seja, é totalmente independente.|Sim|Ele será utilizado no projeto para a criação de permissões de cada tipo de usuário do sistema e as permissões de acesso a determinadas páginas|
|[django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/)|É um aplicativo do Django que permite a construção, customização e reutilização de formulários facilmente, podendo usar qualquer framework CSS, sem escrever código de template e sem ter que cuidar de outros tipos de detalhes.|Sim|Foi utilizado para facilitar a criação de formulários|
|[django-simple-search](https://github.com/gregplaysguitar/django-simple-search)|A busca simples do Django fornece a mesma funcionalidade e conveniência que o search fields faz no admin do django.|A decidir|A aplicação ainda está sendo avaliada|
|[django-search-view](https://github.com/inmagik/django-search-views)|Componente para pesquisa e filtros usando Class Based Views|Sim|O componentes está sendo usando em algumas partes do software que precisa pesquisar algo.|

#### Comunicação entre usuários (Removido do escopo)

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[Rocket.Chat](https://github.com/jadolg/rocketchat_API)|É um microserviço de chat open source baseado no Slack e construído em Meteor|Não|O chat foi removido do escopo do projeto.|
|[Receita-Mais](https://github.com/fga-gpp-mds/2017.2-Receita-Mais)|Software responsável por auxiliar na prescrição de medicamentos|Não|Não passou em quase todos os critérios definidos acima, a aplicação chat do projeto está bastante acoplada, ou seja, teria dificuldade de desacoplar e empacotar o mesmo, gastando tempo e esforço|
|[django-private-chat](https://github.com/Bearle/django-private-chat)|Chat assíncrono baseado em WebSocket|Não|O chat foi removido do escopo do projeto.|
|[django-tawkto](https://github.com/CleitonDeLima/django-tawkto)|Projeto simples integrado com o chat [tawk.to](https://www.tawk.to/)|Não|O chat foi removido do escopo do projeto.|

### 2.3 Banco de dados PostgreSQL

PostgreSQL é um poderoso sistema de banco de dados objeto-relacional de código aberto. Ele é executado em todos os principais sistemas operacionais, tem 15 anos de desenvolvimento ativo e uma arquitetura comprovada que lhe garantiu uma forte reputação de confiabilidade, integridade de dados e correção.

Para o projeto será utilizado o PostgreSQL como o banco de dados de desenvolvimento e produção da aplicação Dr. Down, pela simplicidade e segurança do mesmo.

### 2.4 Redis

Redis é um banco de dados não relacional, também conhecido como NOSQL que armazena dados no formato "chave-valor" em memória e é extremamente rápido.

O Redis é um servidor TCP e seu funcionamento é baseado em um modelo cliente-servidor, dessa forma, quando uma requisição é feita para o Redis, um comando é enviado ao servidor (Redis) pelo cliente e este fica aguardando uma resposta do servidor através de uma conexão estabelecida via socket. Quando o servidor processa o comando, ele envia a resposta de volta ao cliente.

O Redis é uma boa opção para cenários nos quais é necessário alta performance para gravação e/ou leitura de dados baseado em chave-valor, sendo ele utilizado como um servidor de cache para a aplicação, pois além de tudo, ele ainda permite que uma chave expire após um determinado período. Dessa forma, pode ser utilizado para gerenciar sessões de usuário.

O redis é usado na aplicação para fazer o cacheamento (_cache_) Django, com isso, alguma _query_ que a aplicação faria diretamente ao banco, o redis se comunica e armazena o cache já com o resultado. Desta forma, o desempenho é aumentado e a aplicação _mint_ (com performance sempre igual desde o primeiro) é mantida, mesmo com grandes quantidades de dados. O redis se comunica o container do Django e com o PostgreSQL e, em seguida, serve resultados de volta para o Django.

### 2.5 Celery

O Celery é uma ferramenta de execução de tarefas assíncronas que trabalha de forma distribuída. Ele é focado em operações _real-time_, mas suporta tarefas agendadas. Com ele é possível executar uma fila de tarefas (que ele recebe por meio de mensagens), pode agendar tarefas direto no seu projeto sem precisar do cron e ele ainda tem integração fácil com a maioria dos frameworks Python mais utilizados como, por exemplo, o Django e o Flask.

No caso do Django, sempre que um cliente faz uma requisição web (request), o servidor faz um processamento. Ele lê a requisição, trata os dados recebidos, salva ou recupera registros do banco de dados (através dos models), faz algum processamento do que será exibido para o usuário, renderiza isso em um template e manda uma resposta (response) para o cliente.

Dependendo da tarefa que você executa no servidor, a resposta pode demorar muito e isso leva à problemas de **TimeOut**, comprometendo a experiência do usuário. Existem diversas tarefas no projeto que podem demorar para serem executadas, como relatórios pesados, enviar diferentes e-mails para uma lista de usuários, etc.

O Celery funciona da seguinte maneira: O cliente (Django) pode passar uma lista de tarefas para a fila do **Message Broker**, um programa responsável por manter a fila de mensagens que serão trocadas entre o seu programa e o Celery (geralmente é o RabbitMQ ou o Redis, no nosso caso será o Redis). O Message Broker distribui essas tarefas ente os **workers**, que vão executar as tarefas que devem ser assíncronas, e o resultado dessas tarefas pode ser escrito em um **Result Score** (Memória cache, MongoDb ou até mesmo o Redis) que mais tarde pode ser lido pelo cliente novamente.

No presente projeto o Celery executa a tarefa de comunicação com o Sentry (https://sentry.io), que é uma ferramenta para equipes que agrega logs de erro, podendo verificar os ambientes de homologação e produção buscando por erros de execução. Dessa forma, a equipe pode analisar e agir quando há problemas no software.

### 2.6 Caddy

Caddy é o servidor web HTTP/2 com HTTPS automático. O HTTPS é a sigla em inglês de Hyper Text Transfer Protocol Secure, que em português significa "Protocolo de Transferência de Hipertexto seguro". Ele é a versão mais segura do protocolo de transferência de dados entre redes de computadores na internet. Nossa aplicação está utilizando desse protocolo para dar mais segurança ao acesso dos usuários.

### 2.7 Comunicação

1 - O **web client (navegador)** manda uma requisição para o **web server (Nginx)** com o protocolo HTTP.

2 - Os arquivos estáticos armazenados no sistema de arquivos, como CSS, JavaScript, Imagens e documentos PDF, são processados diretamente pelo **web server (Nginx)**.

3 - A parte dinâmica é delegada ao servidor de aplicativos WSGI (Web Server Gateway Interface) do Django. No caso, o **Gunicorn**, que é um servidor WSGI para Unix feito em python puro e disponibilizada pelo framework Django, irá converter solicitações HTTP recebidas do servidor em chamadas python em colaboração com o framework Django, que irá ter um arquivo chamado urls.py que dirá ao Nginx qual código deverá ser executado de acordo com o path e código HTTP recebido. Através de proxy reverso, será feito o redirecionamento inicial do Nginx com o servidor da aplicação, ou seja, o proxy reverso irá funcionar como uma ponte de ligação entre o Nginx e o Django através do Gunicorn.

4 - Dentro do **Django** a requisição recebida pelo **web server** é mapeada para uma view específica através das urls. Elas pedem dados às models, que por sua vez fazem uma requisição ao **redis**. Este que pega os dados do banco de dados **Postgresql** e retorna à view, que seleciona o template e fornece os dados. Assim, o template é preenchido e devolvido à view, que devolve o template como resposta ao web server.

5 - O web server (Nginx) retorna a resposta para o web client (navegador)

## 3:  Requisitos e Restrições Arquiteturais

### 3.1 Dr. Down

| Requisito | Ferramenta/Solução |
|---|---|
|Linguagem| Python 3.6.4 |
|Framework| Django 2.0.3 |
|Plataforma| Web - Navegadores Google Chrome, Safari e Firefox |
|Segurança | O sistema terá informações pessoais dos pacientes que só poderão ser vistas pelo mesmo ou pelo(s) seu(s) respectivo(s) médico(s). Outros dados pessoais só poderão ser vistos pelo próprio usuário.
|Internacionalização (i18n)|	A aplicação terá suporte aos idiomas: Inglês e Português do Brasil (sendo esta a linguagem padrão).

### 3.2 Docker e Compose

| Nome | Versão |
|---|---|
| Docker | 1.13.1
| Docker Compose | 1.8.0

## 4:	Visão Lógica

### 4.1	Visão Geral: Pacotes e Camadas

O framework Django organiza os projetos em apps, que são pastas que contêm uma funcionalidade independente do restante da aplicação. Além disso, existem arquivos de configuração e arquivos estáticos globais. A figura a seguir mostra a organização de pastas de um app.

![Diagrama de Pacotes](http://uploaddeimagens.com.br/images/001/384/521/original/DiagramaPacotes.png?1524419574)

* **apps**: cada app tem uma pasta com as suas models, views, formulários, testes, templates e arquivos estáticos. Além disso, também há um arquivo URLs que será incluso no URLs global.

    - **migrations** : pasta com as migrações para o banco de dados.

    - **static** : pasta com arquivos CSS, JavaScript e imagens.

    - **tests** : arquivos de testes refente ao app.

    - **templates** : arquivos html do app.

    - **locale** : traduções referentes ao app.

    - **models** : arquivos de models do app.

    - **views** : arquivos de views do app.

    - **forms** : arquivos de formulários do app.

    - **admin** : arquivo de conexão do app com o admin.

    - **urls.py** : arquivo que mapeia as as views com templates de cada app

    - **\__init\__** : arquivo que transforma o app em um pacote python.

    - **apps** : mapeia a pasta que o contém como um app.

    - **utils** : arquivos de validação dos apps.


* **config** : pasta com as configurações do projeto Django.

    - **urls.py** : inclui todos os URLs.py dos apps.

    - **\__init\__** : arquivo que transforma as configurações em um pacote python.

    - **settings** : arquivos com as configurações básicas da aplicação.

    - **wsgi** : especificação para uma interface simples e universal entre servidores web e aplicações web.

- **manage.py** : arquivo criado automaticamente pelo Django para gerênciamento de comandos.

- **docs** : documentação da aplicação.

- **compose** : pasta com arquivos do docker.

- **utility** : arquivos para o auxílio na instalação do software.

- **requirements** : organiza todos os pacotes/componentes que a aplicação utiliza em arquivos.


## 5:	Visão de Implementação

### 5.1  Class-Based Views

Proporcionam um método alternativo para implementar views como objetos ao invés de funções. As Class-Based Views (CBV) são classes que implementam métodos e atributos que são comumente utilizados na programação das views. Dessa maneira, o programador pode utilizar métodos já implementados ou sobrescrevê-los e implementá-los da sua maneira. Para atender os mais variados casos de uso das views, as CBV oferecem diversos temas para implementação.

Podemos então agregar as funções básicas das views dentro de classes, como métodos. Os recursos das Class Based Views estão em algumas classes “pré-prontas”, as quais outras classes podem herdar. A partir daí as alterações que precisam ser feitas são mínimas!

### 5.2 Diagrama de Classes

![Diagrama de Classes](http://uploaddeimagens.com.br/images/001/379/381/original/Diagrama.jpeg?1524078112)

### 5.3 Modelo Entidade Relacionamento (MER)

#### USER:

| Atributo | Tipo |Característica | Descrição |
|---|---|---|---|
| photo | Image | Opcional | Foto do usuário |
| name | CharField[255] | Opcional | Nome completo do usuário |
| gender | CharField{choices} | Opcional | Gênero: masculino ou feminino |
| telephone| CharField[14] | Opcional | Telefone do usuário |
| birthday | DateField | Opcional | Data de nascimento |
| created_at | DateField | Automático | Data de criação da conta |
| updated_at | DateField | Automático | Data de modificação das informações da conta |
| has_specialization | BooleanField | Automático | Classifica em user base ou especializado |
| username | CharField[150] | Obrigatório, único | Nome de usuário |
| email | CharField[50] | Obrigatório, único | E-mail do usuário |
| is_active | BooleanField | Obrigatório | Verifica se o usuário está ativo no sistema |
| is_superuser | BooleanField | Obrigatório | Verifica se o usuário é um super administrador |
| last_login | DateField | Automático | Último momento que o usuário logou |
| password | CharField[50] | Obrigatório | Senha do usuário |
| is_staff | BooleanField | Obrigatório | Verifica se o usuário é um funcionário |

#### EMPLOYEE:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| cpf | CharField[14] | Obrigatório, único, validado | CPF do funcionário |
| department | CharField{choices} | Obrigatório | Departamento do funcionário |

#### RESPONSIBLE:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| cpf | CharField[14] | Obrigatório, único, validado | CPF do responsável |

#### PATIENT:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| priority | IntergerField{choices} | Obrigatório | Grau de urgência para atendimento do paciente |
| ses | CharField[9] | Obrigatório, único, validado | Número SES do paciente |
| mother_name | CharField[80] | Obrigatório | Nome da mãe |
| father_name | CharField[80] | Obrigatório | Nome da pai |
| ethnicity | IntegerField{choices} | Obrigatório | Etnia |
| sus_number | CharField[15] | Obrigatório | número do SUS |
| civil_registry_of_birth | CharField[11] | Obrigatório | Registro civil de nascimento |
| declaration_of_live_birth | CharField[11] | Obrigatório | Declaração de nascimento |


#### HEALTH TEAM:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| crm | CharField[7] | Obrigatório, único, validado | Número CRM do médicos |
| speciality | CharField[20] | Obrigatório | Especialidade |
| cpf | CharField[14] | Obrigatório, único, validado | CPF do médicos |
| council_acronym | CharField{choices} | Obrigatório | Conselho Regional |
| register_number | CharField[7] | Obrigatório, validado | Número de registro |

#### ADDRESS:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| city | CharField[40] | Obrigatório | Cidade |
| cep | CharFieldField[8] | Obrigatório, validado | CEP |
| number |  CharField[5] | Obrigatório | Número da moradia|
| uf | CharField{choices} | Obrigatório | Unidade da Federação |
| neighborhood | CharField[30] | Opcional | Bairro |

#### CATEGORY:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| name | CharField[100] | Obrigatório | Nome da categoria |
| description | TextField[100] | Obrigatório | Assunto da categoria |
| slug | SlugField[40] | Obrigatório | Usado para inserir URLs renomeadas |

#### POST:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| title |CharField[100] | Obrigatório | Título do post |
| message | TextField[4000] | Obrigatório | Mensagem do post |
| created_at | DateField | Automático | Data de criação do post |
| updated_at | DateField | Automático | Data de modificação do post |

#### COMMENTARY:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| message | TextField[4000] | Obrigatório | Mensagem do comentário |
| created_at | DateField | Automático | Data de criação do comentário |
| updated_at | DateField | Automático | Data de modificação do comentário |

#### MEDICAL QUESTIONARY:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| psychosocial_risk | IntergerField | Obrigatório | Risco psicossocial |
| health_risk |IntergerField | Obrigatório | Risco de vida |
| family_risk | IntergerField | Obrigatório | Risco familiar |
| total_risk | IntergerField | Obrigatório | Risco total |

#### MEDICAL RECORD:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| history | CharField[4000] | Obrigatório | Histórico médico |


#### QUEUE:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| speciality | CharField[50] | Obrigatório | Especialidade |
| time_left | DateField | Automático | Tempo faltando |
| position | IntergerField | Automático | Posição |

#### EVENTS:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| name | CharField[100] | Obrigatório |Nome do evento |
| date | DateField | Obrigatório | Data do evento |
| description | TextField[4000] | Obrigatório | Descrição do evento |

#### APPOINTMENTS:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| name | CharField[100] | Obrigatório | Nome do compromisso |
| date | DateField | Obrigatório | Data do compromisso |
| description | TextField[100] | Opcional | Descrição do compromisso |

#### CLINIC:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| name | CharField[100] | Obrigatório | Nome da clínica |


#### RELACIONAMENTOS:

##### 1 - APPOINTMENTS tem USERS (HealthTeam):

A equipe de saúde pode ter uma ou várias consultas e uma consulta pertence a um membro da equipe de saúde.

Cardinalidade: 1 X N

##### 2 - APPOINTMENTS tem USERS (Patient):

Um paciente pode ter uma ou várias consultas e uma consulta pertence a um único paciente.

Cardinalidade: 1 X N

##### 3 - MEDICAL RECORDS tem USERS (Patient):

Um prontuário pertence a um único paciente, e um paciente tem um prontuário.

Cardinalidade: 1 X 1

##### 4 - USER (médico) tem USERS (Patient):

Um médico pode ter um ou vários pacientes, e  um paciente pode ter um ou vários membros da equipe de saúde.

Cardinalidade: N X M

##### 5 - POST pertence a USER:

Um usuário pode ter um ou vários Posts, e um post pertence a um único usuário.

Cardinalidade:  1 X N

##### 6 - POST tem COMMENTARIES:

Um comentário pode conter um único post, e um post pode conter vários comentários.

Cardinalidade: 1 X N

##### 7 - CLINIC possui ADDRESS:

Um endereço pode pertencer a apenas uma clinica, e uma clinica pode ter apenas um endereço.

Cardinalidade: 1 X 1

##### 8 - EVENTS possui ADDRESS:

Um evento pode ter apenas um endereço, e um endereço pode ter apenas um evento.

Cardinalidade: 1 X 1


##### 9 - CATEGORIES tem POSTS:

Um post pode conter uma única categoria, e uma categoria pode conter vários posts.

Cardinalidade: 1 X N

## Referências

ARTEFATO: DOCUMENTO DE ARQUITETURA DE SOFTWARE. FUNPAR. Disponível em: <http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sadoc.htm>. Acesso em: 24 Mar. 2018.

ARQUITETURA BASEADA EM COMPONENTES. Disponível em: <https://marcobaccaro.wordpress.com/2010/10/05/arquitetura-baseada-em-componentes/>. Acessado em: 10 Abril. 2018.

CLASS-BASED VIEWS. DJANGO PROJECT. Disponível em: <https://docs.djangoproject.com/en/2.0/topics/class-based-views/>. Acesso em: 28 Mar. 2018.

DESMISTIFICANDO O CONCEITO DE DJANGO APPS. Disponível em: <http://henriquebastos.net/desmistificando-o-conceito-de-django-apps/>. Acesso em: 10 abril. 2018

PADRÕES ARQUITETURAIS MVC X ARQUITETURA DO DJANGO. GITHUB. Disponível em: <https://github.com/fga-gpp-mds/A-Disciplina/wiki/Padr%C3%B5es-Arquiteturais---MVC-X-Arquitetura-do-Django>. Acesso em: 26 Mar. 2018.

POSTGRESQL. Disponível em: <https://www.postgresql.org/about/>. Acesso em: 03 abril. 2018

REDIS O QUE É E PARA QUE SERVE. Disponível em: <https://pt.linkedin.com/pulse/redis-o-que-%C3%A9-e-para-serve-romulo-cianci>. Acesso em: 03 Abril. 2018.

TAREFAS ASSINCRONAS COM DJANGO E CELERY. Disponível em: <https://fernandofreitasalves.com/tarefas-assincronas-com-django-e-celery/>. Acesso em: 03 Abril. 2018.

THE MODEL-VIEW-CONTROLLER DESIGN PATTERN. THE DJANGO BOOK. Disponível em: <https://djangobook.com/model-view-controller-design-pattern/>. Acesso em: 26 Mar. 2018.