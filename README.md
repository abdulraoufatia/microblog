# My Microblog

## Guidance

This README is structured like this:

- Application Features
- DevOps Practices Exercised

### Application Features

#### The concepts covered are

- Templates
- Conditional Statements
- Loops
- Web Forms
- View Forms
- Receiving Form Data
- Improving Field Validation
- Generating links with `url_for` flask argument
- Database Administration (SQLAlchemy, SQLite)
- User Login ([Flask-Login](https://flask-login.readthedocs.io/en/latest/))
  - Authentication (UserMixin)
  - Logging in (`current_user()`, `login_user()`)
  - Logging out (`logout_user`)

#### DevOps Practices Exercised

- Package Management: Poetry
- Containerisation: Docker
- Continuous Integration: GitHub Actions
- Continuous Delivery: GitHub Actions
- Continuous Deployment: Microsoft Azure

## System Requirements

The project uses poetry for Python dependency management. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

```

Once Poetry is installed it does not need activating, it can be used in different ways, see [documentation](https://python-poetry.org/docs/cli/) (https://python-poetry.org/docs/cli/).

### Virtualenv installation and activation

The project also utilises a virtual environment for Python to create isolated environments. A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.

The isolated environment package used for this project is [virtualenv](https://pypi.org/project/virtualenv/) (https://pypi.org/project/virtualenv/).

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

This project uses the Poetry tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. To install the required packages, run the following from your preferred shell:

```bash
poetry install
```

To add a dependency:

```bash
poetry add <NAME_OF_DEPENDENCY>
```

## Running the App

Once all dependencies have been installed and relevant information has been inputted, start the Flask app in development mode within the poetry virtualenv environment by running the following command:

```bash
poetry run flask run
```

You should see an output similar to the following:

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

This application utilises a DevOps concept known as Containerisation. Containerisation can be defined as meaning placing a software component and its environment, dependencies, and configuration, into an insolated unit called a container. This makes it possible to deploy an application consistently in any computing environment, whether on-premise or cloud-based.

To get started, you need to install a containerisation tool. The containerisation tool used for this project was [Docker](https://www.docker.com/) (https://www.docker.com). However, you may find alternatives depending on your Operating System.

### Getting Started with Docker

#### Build and run the Docker Image

This project is built using multi-stage builds. Multi-stage builds are useful to optimise Dockerfiles while keeping them easy to read and maintain. To learn more about multi-stage builds, see [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) (https://docs.docker.com/develop/develop-images/multistage-build/) from the official Docker documentation.

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

The next step is to test the local development setup using the following command: You should see something like this:

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

The basic principle of docker-compose` is utilised to launch long docker run commands. So, rather than running the aforementioned commands, one could run a simple:

```bash
docker-compose up --build 
```

Note: docker-compose.yml is configured in YAML. To further develop your understanding, please see [this link](https://docs.docker.com/compose/gettingstarted/) (https://docs.docker.com/compose/gettingstarted/) --> Docker Compose Getting Started | See step 3

Once running the docker-compose command, you should see something similar to this:

![docker-compose-success](./images/docker-compose-success.png)

When you are ready to tear it all down, simply run ```docker-compose down``` command. The containers will stop and the network will be removed. Below is an expected outcome.

![plot](./images/docker-compose-down-success.png)

#### Running individual containers

If you wish to run a container separately, use each command respectively either:

```bash
docker-compose up web-development
```

```bash
docker-compose up web-production
```

## Application of Continuous Integration and Continuous Delivery

Continuous Integration (CI) is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This repository CI pipeline is set in the following manner:

### Continuous Integration

1. It runs Snyk (pronounced as Sneak) to check for vulnerabilities within the python application
2. It builds the development image
3. Notification is sent through slack

### Continuous Delivery

1. The second job will run upon the success of the first job (CI)
2. Docker buildx is set up
3. Docker is authenticated
4. Production image is pushed to docker (using argument  `target: production`)
5. Image deployed on Heroku
6. Notification is sent

You may view the application by visiting the Heroku web app at [my-microblog-application.herokuapp.com](https://my-microblog-application.herokuapp.com/)(https://my-microblog-application.herokuapp.com/).

### Important Heroku Dockerfile commands and runtime

- If argument `target: <name_of_env>` is set to a specific target, it will upload the target name, the stage by default will upload the last stage. This is because, in our application, it's production, if you were to change this to `test`, the `test` target stage will be pushed to Dockerhub (action name = Pushing to DockerHub )
- The web process must listen for HTTP traffic on $PORT, which is set by Heroku
- EXPOSE in Dockerfile is not respected, but can be used for local testing. Only HTTP requests are supported.

### Continuous Deployment - Tooling and Cloud Infrastructure

### Getting Ready

One would need to have an Azure account set up for this part. If you do not have an Azure Account, create one here at [Microsoft Azure - GB](https://azure.microsoft.com/en-gb/free/) (azure.microsoft.com).

#### Setting up an Azure Account

When prompted select the "Start with an Azure free trial". This gives 12 months of access to some resources, and $150 credit for 30 days, along with "always free" tiers for most common resources. One could use the  Free Tier for this exercise, ensure you select the "FREE Tier" or "SKU F1" when creating resources, as the default is usually the cheapest paid option. The Free Tier and Free Subscription have some downsides: the size, scalability and some functionality of resources are limited, and you can only have one or two of each resource type taking advantage of the Free Subscription.

If you see the "The subscription you have selected already has an app with free tier enabled" then either delete the existing resource in the Portal or opt for the cheap-but-paid Basic Tier for your resource.

#### Creating and Locating a Resource Group

A resource group is a logical container into which Azure resources, such as web apps, databases, and storage accounts, are deployed and managed. More Azure Terminology [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#terminology).

- Within the portal, search for "Resource group"
- Click on  "+ Create". It will open a form to create a resource group. Select your subscription.

#### Installing the CLI

The Azure Command-Line Interface (CLI) allows the execution of commands through a terminal using interactive command-line prompts or a script. Furthermore, the CLI is available to install in Windows, macOS and Linux environments. It can also be run in a Docker container and Azure Cloud Shell.

Once installed, open a new terminal window and enter `az login`, which will launch a browser window to allow you to log in.

### Install on Windows

For Windows, the Azure CLI is installed via the Microsoft Installer (MSI), which gives you access to the CLI through the Windows Command Prompt (CMD) or PowerShell. When installing for Windows Subsystem for Linux (WSL), packages are available for your Linux distribution. See the main install page for the list of supported package managers or how to install manually under WSL.

The current version of the Azure CLI is 2.37.0 (26th July 2022 - 11:00 AM). For further information about the latest release, see the release notes. To find your installed version and see if you need to update, run the `az version` command.

Microsoft Installer: [Link](https://aka.ms/installazurecliwindows) (aka.ms installazurecliwindows)

### Install on macOS

With Homebrew, it is the easiest way to manage your CLI install. It provides convenient ways to install, update, and uninstall. If you don't have homebrew available on your system, [install homebrew](https://docs.brew.sh/Installation.html) before continuing.

You can install the Azure CLI on macOS by updating your brew repository information, and then running the `install` command:

``` brew update && brew install azure-cli ```

*The Azure CLI has a dependency on the* Homebrew python@3.10 package and will *install it.*

For troubleshooting, please see [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos#troubleshooting) (docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos#troubleshooting).

### Hosting Frontend on Azure

Side note: Azure App Service" with Containers vs "Azure Container Instances"

Azure App Services are set up for hosting long-running web applications, with a nice setup for front-facing web applications, with SSL and domain names built in, and allows either raw code or a Container Image to be uploaded.

- One Basic Tier App Service is part of the "Always Free" offering from Azure.

- Azure Container Instances are for lightweight short-run "compute" containers and quickly releasing local Docker compose-based apps. They are faster to deploy and billed per-second, with better orchestration for multiple containers. However, they are more expensive than App Services to run for extended periods and aren't as suited to production web applications.

- Azure Container Apps are a relatively new (General Availability Q2 2022) way of running containers on Azure, with built-in autoscaling support and a focus on microservices.

### Uploading Container Image on DockerHub registry

As Azure Container Registry (ACR) has a cost attached to it, so, therefore, this project is set up with container images pushed to the DockerHub registry. This CI/CD pipeline contains an action that it uploads to Docker Hub Registry.

#### Creating a Web App

<Webapp_name> needs to be *globally* unique, and will form part of the URL of the deployed app: <<https://<webapp_name>.azurewebsites.net>>.

Below are two different methods of how one can create the web_app:

- Portal
  - Within the portal, search for `App Services`
  - Click on `+ Create button`
  - Choose the right `Resource Group`
  - Name your App Service -  *Globally Unique*
  - Choose the desired `OS`
  - Chose the best `region` for low latency
  - Click Next: Docker
  - For `Image Source`, choose the appropriate   source, for the microblog app, I have chosen `Docker Hub`
  - The rest is left as default, others are optional and may have additional costs involved, and click on`create`

- CLI

  - Create the Service App Plan:

  `az appservice plan create --resource-group <resource_group_name> -n <appservice_plan_name> --sku B1 --is-linux`

- Create the Web App:

  `az webapp create --resource-group <resource_group_name> --plan <appservice_plan_name> --name <webapp_name> --deployment-container-image-name <dockerhub_username>/todo-app:latest`

#### Setting up the Environment Variables

This is an optional setting, as the Microblog application is at its infancy stages, and it does not have environment variables. However, for future references, it's good to know.

- Portal

  - Under the `Settings Blade`, Click on `Configuration`
  - Add all environment variables accordingly to your .env file as `New application Setting`
  - Press save!

- CLI

  - You can enter environment variables individually via:

     `az webapp config appsettings set -g <resource_group_name> -n
     <webapp_name> --settings FLASK_APP=app.routes:app. <env1=token> <env2=key>`

     Don't forget to add all the environment variables your application needs.

#### Confirming Status of Application

Browse to `<http://<webapp_name>.azurewebsites.net/>` and confirm no functionality has been lost.

### Setting up Continuous Deployment

When creating an App Service, Azure sets up a webhook URL. Post requests to this endpoint cause your app to restart and pull the latest version of the container image from the configured registry.

- Find the webhook URL: From the app service in Azure Portal, navigate to Deployment Center

- Test webhook provided with:

  `curl -dH -X POST your_webhook_url`

- To prevent the `$username` part of the webhook from being interpreted by your shell as a variable name place backslash before the dollar sign. For example:
`curl -dH -X POST https://\$microblog-aatia:abc123@...etc`

- The command was then added to the CD pipeline

  ![L-280-Continuous-deployment](./images/L-280-ContiniousDeployment%20.png)

Kindly note, the App Service and App Service Plan have been deleted, and the link within the image is not functional. To confirm the test of the application, please see the image attached:

![L-280-testing-webapp](./images/L-280-testing-webapp.png)

## Detecting and Fixing Dependency Vulnerabilities

Snyk CLI brings the functionality of Snyk into the workflow. The CLI can be run locally or in the CI/CD pipeline to scan for vulnerabilities and license issues.

Snyk CLI is Open Source and Supports many languages and tools including Java, .NET, JavaScript, Python, Golang, PHP, C/C++, Ruby, and Scala.

This project utilises the `snyk fix` command, `snyk fix` is a new CLI command to apply the recommended updates for supported ecosystems automatically.

### Pre-requisites

- An account with Snyk
- Snyk CLI Installed
- Snyk CLI authenticated with your device

### Getting Started with Snyk CLI - Local Machine

- Install snyk cli with `npm install -g snyk`
- Authorise your Snyk account with the CLI with `snyk auth`, ensure to be logged in before authenticating - Create an account if you do not have one.
- Test your application for vulnerabilities using `snyk test`

![Snyk-Text](./images/L-252_Snyk_Test.png)

- Fix the vulnerability with `snyk fix`

![Snyk-Text](./images/L-252_Snyk_Fix.png)

The afore-attached image represents fixing 1 vulnerable path, Pin lxml@4.8.0 to lxml@4.9.1 to fix - ✗ NULL Pointer Dereference (new) [Medium Severity][https://snyk.io/vuln/SNYK-PYTHON-LXML-2940874] in lxml@4.8.0 introduced by pyspelling@2.7.3 > lxml@4.8.0.

### Using Github Actions and Snyk

Running `snyk monitor` on your machine (Any, virtual or local) sends a report to your Snyk Dashboard for further monitoring.

You can find the latest monitored as a report.  The report will show you vulnerabilities within your project, if any, and how to fix them. You can monitor projects with Snyk Container, Snyk Opensource and Snyk IaC.

For further information please visit the [Snyk Documentation](https://docs.snyk.io/) (https://docs.snyk.io/).

# Database

## Database Migration Repository

The model class created within app/models.py defines the initial database structure (or schema) for this application. 

As the application will grow, the database schema will require changes to make. Alembic is a migration framework used by Flask-Migrate and enables schema changes without the database being re-created every time a change needs to be made. 

Further to this, Alembic maintains a migration repository, which is a directory in which it stores its migration scripts. Each time a change is made to the database schema, a migration script is added to the repository with the details of the change.

Flask-Migrate exposes its commands through the `flask` command, the `flask` command is utilised through `flask run`, a sub-command native to Flask. The `flask db` sub-command is added by Flask-Migrate to manage everything related to database migrations. To enable easier and safer database migrations the `flask db` sub command was utilised.

![database-migration-repository](./images/L-252_Database_Migration_Repository.png)

## First Database Migration

Upon the development of the migration repository, the first database migration was developed overseeing the user's table that maps to the User database model.

The command utilised to create the database migration `flask db migrate -m "users table"`. Here, the table created was titled as "users" table.

![first_database_migration](./images/L-253_flask_db_migrate_-m_command.png)

Explaining what is happening above:

 The first two lines are informational and can be ignored. A user table and two indexes were then found, and then it tells you where it wrote the migration script. The `b1d826c7f739` string is an automatically generated unique code for the migration. The comment given with the -m option is optional, it adds a short descriptive text to the migration.

### Discussing what was generated:

TL DR:

Two functions `upgrade()` and `downgrade()` were used. The `upgrade()` function applies the migration, and the `downgrade()` function removes it. This allows Alembic to migrate the database to any point in the history, to older versions also, by using the downgrade path.

Once the database migration was developed, the changes were applied by evoking the `flask db upgrade` command.

![flask_db_upgrade_command](./images/L-253_flask_db_upgrade_command.png)

## Database Migration Strategy - Explained

The application is currently in its infancy stage. However, in the case of an application being on a development machine and deployed to a production server and was decided for the next release a new change to the models will be introduced, for example, a new table to be added. Without migration, one would need to figure out how to change the schema of the database, both in development and production.

However, as we have database migration support, models in the application can be modified to generate a new migration script by evoking the `flask db migrate` command. It is best to review the new model to ensure automatic generation did the right thing. Changes are then applied to the development database by running the `flask db upgrade` command.

Once the new version is ready to be released to the production environment, one would need to run the `flask db upgrade` command. Alembic will detect that the production database is not updated to the latest revision of the schema, and run all the new migration scripts that were created after the previous release.

To undo the last migration, the `flask db downgrade` command is to be utilised. This command is unlikely to be used during production, however, it can become useful during development should one need to downgrade, delete a migration script then continue to generate a new script to replace it.

## Database Relationship - Explained

Relational databases are good to categorise and storing data which then can be queried and filtered to extract information.

In the case of a user writing a blog post, the user will have a record in the users' table, where the post will have a record in the posts table. An efficient method to record who wrote a given post is to link two related records.

Once a relationship is established, one can perform complex queries such as reversing relationships; finding out which user wrote a certain blog post. Flask-SQLAlchemy can help with both types of queries.

In commit [b5aaf13](https://github.com/abdulraoufatia/microblog/pull/32/commits/b5aaf13caaba9402361a88ccf3a700f2dc3e7be6), app/models.py was modified, and a schema for a new posts table was developed:

![L-255_Schema_for_new_posts_table](./images/L-255_Schema_for_new_posts_table.png)

Describing the attached image, the database diagram above shows foreign keys as a link between the `user_id` and the `id` fields of the table it refers to. This kind of relationship is called one-to-many because "one" user writes "many" posts.

The `user_id` field is called a *foreign key* as it is the child key, where as mentioned, the `id` is the primary key. Further describing the image attached, The posts table contains a required `id`, the `body` of the post and the `timestamp`. In addition to these expected fields, a `user_id` field was added, linking the post to its author.

Finally, as updates to the application models were made, a new database migration was needed to be generated by running the `flask db migrate -m "posts table"` command:

![L-255_posts_table_db_migrate](./images/L-255_posts_table_db_migrate.png)

The migration was then applied with `flask db upgrade`.

![L-255_posts_table_db_upgrade](./images/L-255_posts_table_db_upgrade.png)

## Interacting with the Database

Start with importing the database instance with:

`from app import db`

and with the two model classes:
`from app.models import User, Post`

### How to create a new user

`u = User(username='john', email='john@example.com')`
The next step would be to write the user to the database, to this, it will be done to the db.session(), db.session represents active sessions which changes can made to:
`db.session.add(u)`

Multiple changes can be accumulated in a session and once all the changes have been registered you can issue a single `db.session.commit()`, which writes all the changes atomically.

`db.session.commit`

 If at any time while working on a session there is an error, a call to db.session.rollback() will abort the session and remove any changes stored in it. From the PR fill-in blank, the database contains two users. Queries can be made to the database to answer desired questions.

 ```python
>>> users = User.query.all()
>>> users
[<User john>, <User susan>]
>>> for u in users:
...     print(u.id, u.username)
...
1 john
2 susan
 ```

### Adding a blog post to the Database 

The example below illustrates the ability to add a blog post to the database, assigned to user id 1 (John), from the tutorial above. One can erase test users and posts created above. To do this, create a for loop to iterate through the users and utilise the `db.session.delete()` query, and likewise for the posts:

```
>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()
```

For further information, please visit the official [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) documentation many options that are available to query the database.

## Automated Testing
- [ ] Create a user
- [ ] Login form, confirm not registered user

Ideas:

- [ ] - testing field validation
- [ ] - closing of for loop in login.html ({% endfor %})
- [ ] - to see if all packages are installed with correct versions as stated within pyproject.toml
