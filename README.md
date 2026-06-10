# ArtriApp - API (Back-end)

Este repositório contém o código do back-end do aplicativo **ArtriApp**, desenvolvido utilizando Django e Django Rest Framework. A API é responsável pelo gerenciamento de usuários, diário de dor/fadiga/sono, checklist de medicamentos e recomendação de exercícios para o aplicativo mobile.

Este projeto é parte da disciplina de Desenvolvimento Mobile. Siga o guia abaixo para executar a API localmente na sua máquina para realizar testes e implementações de front-end.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Framework:** Django 5.x
* **API:** Django Rest Framework (DRF)
* **Banco de Dados (Local):** SQLite (Padrão de desenvolvimento)
* **Documentação da API:** Swagger/ReDoc (drf-yasg)

---

## 🚀 Como Executar Localmente (Modo Desenvolvimento)

### 1. Clonar o repositório
Abra o seu terminal e clone o projeto na sua máquina:
```bash
git clone https://github.com/artri-app/artri-app-api.git
cd artri-app-api/artri_app_api

```

### 2. Criar e Ativar o Ambiente Virtual (Venv)

O ambiente virtual isola as dependências do projeto para que elas não entrem em conflito com outros pacotes Python na sua máquina.

**No Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

**No Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

*(Você saberá que deu certo quando a palavra `(venv)` aparecer no início da linha do terminal).*

### 3. Instalar as Dependências

Com o ambiente ativado, instale os pacotes requeridos pelo Django:

```bash
pip install -r requirements.pip

```


### 4. Configurar o Banco de Dados e Carga de Dados (Seed)

Nós utilizamos um script para criar e popular o banco de dados rapidamente com todos os Treinos e Exercícios de fisioterapia já ordenados.

Execute os comandos abaixo na ordem exata:

```bash
# Aplica a estrutura das tabelas no banco de dados local
python manage.py migrate

# Roda o script de semeadura (lê o arquivo CSV e popula o banco)
python seed_banco.py

```

### 5. Criar o Administrador do Sistema

Para acessar o painel de administração e ver os dados salvos, crie uma conta administrativa:

```bash
python manage.py createsuperuser

```

*(O terminal pedirá que você digite um nome de usuário, e-mail e senha).*

### 6. Rodar o Servidor

Tudo pronto! Inicie o servidor local de desenvolvimento:

```bash
python manage.py runserver 0.0.0.0:8000

```

*(Se estiver usando Windows, pode usar apenas `python manage.py runserver`).*

---

## 🔗 Endpoints e Documentação

Com o servidor rodando, você pode acessar os painéis através do seu navegador:

* **Painel Administrativo do Django:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* **Documentação Interativa da API (Swagger):** [http://127.0.0.1:8000/api/schema/swagger-ui/](https://www.google.com/search?q=http://127.0.0.1:8000/api/schema/swagger-ui/) *(Aqui você pode testar as rotas de login, envio de métricas de diário e listagem de exercícios).*

---

## 🐋 Execução via Docker (Opcional)

Caso prefira não configurar o Python localmente e tenha o Docker instalado:

```bash
docker-compose -f docker/docker-compose-local.yml up -d --build

```

Após os contêineres subirem, execute as migrações por dentro do contêiner:

```bash
docker-compose -f docker/docker-compose-local.yml exec api python manage.py migrate
docker-compose -f docker/docker-compose-local.yml exec api python seed_banco.py
