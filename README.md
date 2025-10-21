# Sistema de Reserva de Salas

Sistema web completo desenvolvido em Flask, com Blueprints, módulos separados e injeção de dependências, seguindo boas práticas de desenvolvimento.

1. Introdução ao Projeto

    Este projeto tem como objetivo criar uma aplicação web segura e funcional, com as seguintes funcionalidades:

    Cadastro e login de usuários com hash de senha (Flask-Login).

    Proteção de formulários com CSRF (Flask-WTF).

    CRUD completo da entidade principal (Salas de Reunião).

    API RESTful com endpoints equivalentes ao CRUD.

    Persistência de dados em MySQL ou PostgreSQL via SQLAlchemy.

    Código organizado em Blueprints (módulos separados).

    Boas práticas de segurança: hash de senha, validação de dados e uso de variáveis de ambiente.

2. Tema do Projeto

Sistema de Reserva de Salas:

Cadastro de salas de reunião.

Reservas em horários diferentes.

Visualização das reservas existentes.

3. Estrutura do Projeto
    /meu_projeto
    |-- app.py
    |-- config.py
    |-- models.py
    |-- extensions.py          # inicialização de db, login_manager etc.
    |-- /blueprints
    |   |-- __init__.py
    |   |-- web
    |   |   |-- __init__.py
    |   |   |-- routes.py      # rotas HTML (CRUD com Flask-WTF)
    |   |   |-- forms.py
    |   |-- api
    |   |   |-- __init__.py
    |   |   |-- routes.py      # rotas RESTful (JSON)
    |-- /templates
    |   |-- layout.html
    |   |-- login.html
    |   |-- registro.html
    |   |-- lista.html
    |   |-- editar.html
    |-- /static
    |   |-- css
    |   |-- img
    |-- /uploads
    |-- requirements.txt

4. Preparar o Ambiente

    1. Crie e ative um ambiente virtual.
    Windows (PowerShell):
    
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

    2. Instale as bibliotecas necessárias:
    pip install Flask Flask-WTF WTForms email-validator Flask-Login Flask-SQLAlchemy PyMySQL psycopg2-binary

    3. Gere o requirements.txt para reprodutibilidade:
    pip freeze > requirements.txt

5. Executar o Projeto 
    1. Execute a aplicação:
    python app.py

    2. Abra no navegador:
    http://127.0.0.1:5000/

Você deverá ver a página inicial definida no Blueprint web, listando as salas cadastradas.




# Testando no navegador

Abra no seu navegador: 👉 http://127.0.0.1:5000/

Você deverá ver a página inicial definida no blueprint web.