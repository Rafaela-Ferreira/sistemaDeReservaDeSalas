## Sistema de Reserva de Salas

Sistema web completo desenvolvido em Flask, com Blueprints, módulos separados e injeção de dependências, seguindo boas práticas de desenvolvimento.

---

## 1. Introdução ao Projeto

Você deverá desenvolver uma aplicação web **completa e segura**, usando Flask, que inclua:

- Cadastro e login de usuários com **hash de senha**.
- Proteção de formulários com **CSRF** (Flask-WTF).
- CRUD completo de uma entidade principal (livros, produtos, alunos etc.).
- API RESTful com endpoints equivalentes ao CRUD.
- Persistência em banco de dados **MySQL** ou **PostgreSQL** via SQLAlchemy.
- Organização do código em **Blueprints** (módulos separados).
- Boas práticas de segurança (hash de senha, validação de dados, variáveis de ambiente).

---

## 2. Tema do Projeto

    Sistema de Reserva de Salas:
   
    Cadastro de salas de reunião.
    
    Reservas em horários diferentes.
    
    Visualização das reservas existentes.

## 3. Estrutura do Projeto

```
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
```

---

## 4. Preparar o Ambiente

    1 Crie e ative um ambiente virtual.

        Windows (PowerShell):
        
        python -m venv .venv

        .\.venv\Scripts\Activate.ps1

    2 Instale as bibliotecas necessárias:
    
        pip install Flask Flask-WTF WTForms email-validator Flask-Login Flask-SQLAlchemy PyMySQL psycopg2-binary

    3 Gere o requirements.txt para reprodutibilidade:
    
        pip freeze > requirements.txt


## 5. Testando no navegador

Abra no seu navegador: 👉 http://127.0.0.1:5000/

Você deverá ver a página inicial definida no Blueprint web, listando as salas cadastradas.