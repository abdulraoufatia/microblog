# My Microblog

## Guidance

This README is structured like this:

- A repository map
- Application Features
- Devops practices exercised

### Application Features

#### The concepts covered are

- Templates
- Conditional Statements
- Loops
- Templates
- Web Forms
- View Forms
- Receiving Form Data
- Improving Field Validation
- Generating links with `url_for` flask argument
- Databases in Flask
- Database Migration

#### The DevOps Practices used and their application

- Package Management: Poetry
- Containerisation: Docker
- Continious Integration: GitHub Actions / Docker
- Continious Delivery: GitHub Actions / Dockerhub / Heroku
- Database Management: SQLAlchemy, SQLite

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

```

Once Poetry is installed, it does not need activating. It can be used in the different ways, see [documentation](https://python-poetry.org/docs/cli/).

### Virtualenv installation and activation

The project also utilises a virtualenv for Python to create isolated environments.

```bash
pip install virtualenv
```

You would then need to create a virtual env. for the project:

```bash
pip -m venv name-of-venv
```

Activate the venv (Mac OS):

```bash
source name-of-venv/bin/activate
```

Activate the venv (Windows OS):

```bash
source name-of-venv/Scripts/activate
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
poetry install
```

To add a dependency:

```bash
poetry add <NAME_OF_DEPENDENCY>
```

## Running the App

Once the all dependencies have been installed and relevant information has been inputted, start the Flask app in development mode within the poetry environment by running:

```bash
poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## DevOps Applications - Containerisation

This application utilises a DevOps concept known as Containerisation. Containerisation entails placing a software component and it's environment, dependencies, and configuration, into an insolated unit called a container. This makes it possible to deploy an application consistently on any computing environment, whether on-premise or cloud-based.

To get started, you need to install a containerisation tool. The containerisation tool used for this project was Docker. However, you may find alternatives depending on your Operating System.

### Getting Started with Docker

#### Build and run the Docker Image

This project is built using multi-stage builds. Multi-stage builds are useful to optimise Dockerfiles while keeping them easy to read and maintain. To learn more about multi-stage builds, see [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) from the official Docker documentation.

To build the development environment, run the following command:

```bash
docker build --target development --tag microblog:development .
```

I have built the development environment image, you should see something similar to this:

```bash
(.venv) [L-237 x] {} microblog docker build --target development --tag microblog:development .
[+] Building 10.7s (10/10) FINISHED                                                                                                                                                
 => [base 1/5] FROM docker.io/library/python:3.10.
 => CACHED [base 2/5] WORKDIR /app                                                                                                                                                                0.0s
 => CACHED [base 3/5] RUN apt-get update     && apt-get -y install curl     && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -                   0.0s
 => CACHED [base 4/5] COPY . /app/                                                                                                                                                                0.0s
 => CACHED [base 5/5] RUN poetry config virtualenvs.create false --local && poetry install                                                                                                        0.0s
 => exporting to oci image format                                                                                                                                                                 8.0s
 => => exporting layers                                                                                                                                                                           0.0s
 => => exporting manifest sha256:784d67e8e26f3f75524debe19ba22ec79cc19aff719a74245c0309c496676b2f                                                                                                 0.0s
 => => exporting config sha256:aa100674e4df152df8ce1ae3cf04ef75d863dc891a0dc4b1b2d8be7e6623fe4b                                                                                                   0.0s
 => => sending tarball                                                                                                                                                                            7.9s
unpacking docker.io/library/microblog:development (sha256:784d67e8e26f3f75524debe19ba22ec79cc19aff719a74245c0309c496676b2f)...done
(.venv) [L-237 x] {} microblog 
```

The next step is to test the local development setup using the following command:

```bash
docker run -p 4000:5000 --mount type=bind,source="$(pwd)"/app,target=/app/app microblog:development
```

You should see see something like this:

```bash
docker run -p 4000:5000 --mount type=bind,source="$(pwd)"/app,target=/app/app microblog:development
Skipping virtualenv creation, as specified in config file.
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000 (Press CTRL+C to quit)
```

## Advanced Features of Docker - Docker Compose

Launching containers with long docker run commands can become tedious, and difficult to share with other developers.

### Building your image

The basic principle of `docker compose` is utilised to launch long docker run commands. So, rather than running the aforementioned commands, one could run a simple:

```bash
docker-compose up --build 
```

Note: docker-compose.yml is configured in YAML. To further develop your understanding, please see [this link](https://docs.docker.com/compose/gettingstarted/) --> Docker Compose Getting Started | See step 3

Once running the docker compose command, you should see something similar to this:

![docker-compose-success](./images/docker-compose-success.png)

When you are ready to tear it all down, simply run ```docker-compose down``` command. The containers will stop and the network will be removed. Below is an expected outcome.

![plot](./images/docker-compose-down-success.png)

#### Running individual containers

If you wish to run a container seperately, use each command respecitively either:

```bash
docker-compose up web-development
```

```bash
docker-compose up web-production
```

## Application of Continious Integration and Continious Delivery

Continuous Integration (CI) is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This repoistory CI pipeline is set in the following manner:

### Continuous Integration

1. It runs Snyk to check for vulnerabilities with the python application
2. It builds the test image
3. It runs the test image, printing the results of the test, if all is well it proceed with the next step;
4. Notification is sent

### Continious Delivery

1. Second job will run upon the success of first job (CI)
2. Docker buildx is set up
3. Docker is authenticated
4. Production image is pushed to docker (using argument  `target: production`)
5. Image deployed on Heroku
6. Notification is sent

## Detecting and Fixing Dependency Vulnerabilities

This project utalises the `snyk fix` command, `snyk fix` is a new CLI command to apply the recommended updates for supported ecosystems automatically. Snyk CLI bring functionality of Snyk into the workflow. The CLI can be run locally or in the CI/CD pipeline to scan for vulnerabilities and licencse issues.

Snyk CLI is Open Source and Supports many languages and tools including Java, .NET, JavaScript, Python, Golang, PHP, C/C++, Ruby, and Scala.

### Pre-requisites

- An account with Snyk
- Snyk CLI Installed
- Snyk CLI authenticated with your device

### Getting Started with Snyk CLI - Local Machine

- Install snyk cli with `npm install -g snyk`
- Authorise your snky account with the CLI with `snyk auth`, ensure to to be logged in prior to authenticating - Create an account if you do not have one.
- Test your application for vulnerabilities using `snyk test`

![Snyk-Text](./images/L-252_Snyk_Test.png)

- Fix the vulnerability with `snyk fix`

![Snyk-Text](./images/L-252_Snyk_Fix.png)

This aforeattached image represents fixing 1 vulnerable path, Pin lxml@4.8.0 to lxml@4.9.1 to fix - ✗ NULL Pointer Dereference (new) [Medium Severity][https://snyk.io/vuln/SNYK-PYTHON-LXML-2940874] in lxml@4.8.0 introduced by pyspelling@2.7.3 > lxml@4.8.0 .

### Using Github Actions and Snyk

Run snyk Monitor on your machine (Any, virtual or local) - Sends a report to your Snyk Dashboard for further monitoring. You are able to find the latest monitored as a report.  The report will show you a project and how to fix it. You can mointor projects with Snyk Container, Snyk Opensource and Snyk IaC.

### Important Heroku Dockerfile commands and runtime

- If argument `target : <name_of_env>` is set to a specific target, it will upload the target name, the stage by default will upload the last stage. This is because, in our application, it's production, if you were to change this to `test`, the `test` target stage will be pushed to Dockerhub (action name = Pushing to DockerHub )
- The web process must listen for HTTP traffic on $PORT, which is set by Heroku
- EXPOSE in Dockerfile is not respected, but can be used for local testing. Only HTTP requests are supported.

# Database

## Database Migration Repoistory

The model class created wthin app/models.py defines the initial database structure (or schema) for this application. As the applcication will grow, the database schema will require changes to made. Alembic is a migration framework used by Flask-Migrate and will enable schema changes without database being re-created from scratch every time a change needs to be made. Alembic maintains a migration repository, which is a directory in which it stores its migration scripts. Each time a change is made to the database schema, a migration script is added to the repository with the details of the change.

Flask-Migrate exposes its commands through the `flask` command, the `flask` command is utilised through `flask run`, a sub-command native to Flask. The `flask db` sub-command is added by Flask-Migrate to manage everything related to database migrations. To enable easier and safer database migrations the `falsk db`sub command was utilised.

![database-migration-repository](./images/L-252_Database_Migration_Repository.png)

## First Database Migration

Upon the development of the migration repository, the first database migration was developed overseeing will the users table that maps to the User database model.

The command utilised to create the database migration `flask db migrate -m "users table"`. Here, the table created was titled as "users" table.

![first_database_migration](./images/L-253_flask_db_migrate_-m_command.png)

 Explanining what is happening above:

 The first two lines are informational can be ignored. A user table and two indexes were then found, then it tells you where it wrote the migration script. The `b1d826c7f739` code is an automatically generated unique code for the migration . The comment given with the -m option is optional, it adds a short descriptive text to the migration.

Discussing what was generated:

TL DR:

Two functions `upgrade()` and `downgrade()`. The `upgrade()` function applies the migration, and the `downgrade()` function removes it. This allows Alembic to migrate the database to any point in the history, to older versions also, by using the downgrade path.

Once the database migration was developed, the changes were applied by envoking `flask db upgrade`

![flask_db_upgrade_command](./images/L-253_flask_db_upgrade_command.png)

As the application database engine SQLALchemy utilises SQLite, the ``

## Database Upgrade and Downgrade Workflow - Database Migration Strategy, Explained

The application is currently at it's infancy stage. However in the case of an application being on a development machine and deployed to a production server and was decided for the next release a new change to the models will be introduced, for example, a new table to be added. Without migration, one would need to figure out how to the change schema of the database, both in development and production.

However, as we have database migration support, models in the appliation can be modified to generate a new migration script by envoking  `flask db migrate`. It is best to review the new model to ensure automatic generation did the right thing. Changes are then applied to the development database by running `flask db upgrade`.

Once the new version is ready to be released to the production environment, one would need to run `flask db upgrade`. Alembic will detect that the production database is not updated to the latest revision of the schema, and run all the new migration scripts that were created after the previous release.

To undo a last mirgration, `flask db downgrade` command is to be utilised. This command is unlikley to be used during production, however can be useful during development should one need to downgrade, delete a migration script then continue to generate a new script to replace it.

## Automated Testing

- to use pytest

Ideas:

- [ ] - testing field validation
- [ ] - closing of for loop in login.html ({% endfor %})
- [ ] - to see if all packages are installed with correct versions as stated within pyproject.toml
