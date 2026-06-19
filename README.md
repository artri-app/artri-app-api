# ArtriApp - API (Back-end)

Este repositório contém o código do back-end do aplicativo **ArtriApp**, desenvolvido utilizando Django e Django Rest Framework. A API é responsável pelo gerenciamento de usuários, diário de dor/fadiga/sono, checklist de medicamentos e recomendação de exercícios para o aplicativo mobile.

Este projeto é parte da disciplina de Desenvolvimento Mobile. Siga o guia abaixo para executar a API localmente na sua máquina para realizar testes e integrar com o seu front-end em Flutter.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Framework:** Django 5.x
* **API:** Django Rest Framework (DRF)
* **Banco de Dados:** PostgreSQL
* **Documentação da API:** Swagger/ReDoc (drf-yasg)

---

## ⚙️ Passo 0: Configuração de Variáveis de Ambiente (Obrigatório)

Seja rodando via Docker ou Localmente, o projeto **exige** um arquivo `.env` para conectar ao banco de dados. Sem ele, a aplicação (e o Docker) irá falhar.

1. Clone o repositório e entre na pasta:
```bash
   git clone [https://github.com/artri-app/artri-app-api.git](https://github.com/artri-app/artri-app-api.git)
   cd artri-app-api/artri_app_api

```

2. Na pasta `docker/django/`, existe um arquivo chamado `artriapp.env.example`.
3. Copie este arquivo para a **raiz** do projeto (onde está o `manage.py`) e renomeie-o para **`.env`** (com o ponto no início).
4. Abra o arquivo `.env` e preencha as variáveis do banco de dados (escolha uma senha e um usuário). Exemplo:
```env
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
DJANGO_ALLOWED_HOSTS=*

# Configurações do Banco de Dados
DB_ENGINE=django.db.backends.postgresql
DB_NAME=artriapp_db
DB_USER=artri_user
DB_PASSWORD=senha_super_segura
DB_HOST=db  # Use 'db' se for rodar via Docker, ou 'localhost' se for rodar Nativo
DB_PORT=5432

# Configurações necessárias para o contêiner do Postgres no Docker
POSTGRES_DB=artriapp_db
POSTGRES_USER=artri_user
POSTGRES_PASSWORD=senha_super_segura

```



Escolha **APENAS UM** dos caminhos abaixo para rodar o projeto: via Docker (Recomendado) ou Localmente (Nativo).

---

## 🐋 Caminho 1: Execução via Docker (Recomendado)

Esta é a maneira mais rápida e fácil, pois cria o banco de dados PostgreSQL automaticamente sem que você precise instalá-lo no seu computador.

**Pré-requisito:** Ter o [Docker](https://www.docker.com/) e o Docker Compose instalados.

### 1. Subir os contêineres

Na raiz do projeto (onde está o `manage.py`), execute:

```bash
docker-compose -f docker/docker-compose-local.yml up -d --build

```

*(O Docker fará o download do Python, do PostgreSQL, instalará as dependências e iniciará o banco).*

### 2. Configurar o Banco e Popular Dados (Seed)

Com os contêineres rodando, execute os comandos por dentro do contêiner da API:

```bash
# Aplica a estrutura das tabelas no banco de dados
docker-compose -f docker/docker-compose-local.yml exec api python manage.py migrate

# Roda o script de semeadura (popula o banco com os Treinos e Exercícios)
docker-compose -f docker/docker-compose-local.yml exec api python seed_banco.py

# Cria o usuário administrador do sistema
docker-compose -f docker/docker-compose-local.yml exec api python manage.py createsuperuser

```

**Tudo pronto!** A API já está rodando em `http://localhost:8000`. Pule para a seção "Endpoints".

---

## 💻 Caminho 2: Execução Local Nativa (Sem Docker)

Siga este caminho apenas se preferir rodar os serviços diretamente na sua máquina.

**Pré-requisitos Críticos:**

1. **Python 3.12+** instalado.
2. **PostgreSQL** instalado na sua máquina (ex: via pgAdmin ou instalador nativo).
3. *(Apenas Linux)*: Você precisa das bibliotecas de desenvolvimento do Postgres para o `pip install` funcionar. Rode: `sudo apt-get install libpq-dev python3-dev gcc`.

### 1. Criar o Banco de Dados no PostgreSQL

Antes de rodar o projeto, abra o seu terminal do Postgres (`psql`) ou o pgAdmin e rode os seguintes comandos SQL para criar a instância que o Django usará (certifique-se de que os nomes batem com os do seu arquivo `.env`):

```sql
CREATE DATABASE artriapp_db;
CREATE USER artri_user WITH PASSWORD 'senha_super_segura';
ALTER ROLE artri_user SET client_encoding TO 'utf8';
ALTER ROLE artri_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE artri_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE artriapp_db TO artri_user;

```

### 2. Criar e Ativar o Ambiente Virtual (Venv)

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

### 3. Instalar as Dependências

Com o ambiente ativado (você verá `(venv)` no terminal):

```bash
pip install -r requirements.pip

```

*(Se ocorrer erro nesta etapa, verifique se o PostgreSQL está corretamente instalado na sua máquina, pois a biblioteca `psycopg2` depende dele).*

### 4. Configurar e Popular o Banco (Seed)

Atenção: Garanta que a variável `DB_HOST` no seu arquivo `.env` está como `localhost` nesta etapa.

```bash
python manage.py migrate
python seed_banco.py
python manage.py createsuperuser

```

### 5. Rodar o Servidor

```bash
python manage.py runserver 0.0.0.0:8000

```

---

---

## ❓ Resolução de Problemas Frequentes (FAQ)

**1. O meu terminal parou na mensagem `0 static files copied... System check identified no issues`. O servidor travou?**
> **Não! Isso não é um erro.** Essa é a mensagem de SUCESSO do Django. Significa que o servidor iniciou perfeitamente, o banco conectou e ele está esperando as suas requisições. Deixe o terminal aberto e acesse `http://localhost:8000` no seu navegador.

**2. Erro: `could not translate host name "artriapp-db" to address`**
> Esse erro ocorre se você tentou rodar o projeto localmente (sem Docker) usando a configuração padrão do `.env`. Abra o seu arquivo `.env`, encontre a linha `DATABASE_URL` e troque a palavra `artriapp-db` por `localhost`.

**3. Erro no Redis ou Cache na hora de fazer login**
> Abra o seu `.env` e certifique-se de que a variável `CACHE_ENABLED=False`. O cache exige um servidor Redis rodando. Desativando-o, o Django funcionará normalmente para testes de desenvolvimento.

## 🔗 Endpoints e Documentação

Com o servidor rodando, você pode acessar os painéis através do seu navegador:

* **Painel Administrativo do Django:** [http://localhost:8000/admin/](https://www.google.com/search?q=http://localhost:8000/admin/)
* **Documentação Interativa da API (Swagger):** [http://localhost:8000/api/schema/swagger-ui/](https://www.google.com/search?q=http://localhost:8000/api/schema/swagger-ui/) *(Aqui você pode testar as rotas de login, envio de métricas de diário e visualizar o formato do JSON dos exercícios).*

