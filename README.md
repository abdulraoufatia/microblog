# My Microblog

## Guidance

This README is structured like this:

- A repository map 
- Flask concepts used
- Devops practices exercised 
- How you can use this for personal use 

### Repository Map

The concepts covered are :

- Templates
- Conditional Statements
- Loops
- Templates
- Web Forms

The DevOps Topics Covered:

- Package Management: Poetry
- Continious Integration: GitHub Actions

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

Once Poetry is installed, it does not need activating. It can be used in the different ways, see [documetnation](https://python-poetry.org/docs/cli/). 

### Virtualenv installation and activation

The project also utalises a virtualenv for Python to create isolated environemtns. 

```bash
pip install virtualenv
```

You would then need to create a virtual env. for the project:

```
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