# Backend Engine

Backend Engine serves REST APIs for Sakinah Wedding Platform

## Prerequisite
The following version of programming language or tools are needed to run this service smoothly in your local machine (Unix Based)

- Python 3.10.10
- [Docker 10.10.8](https://docs.docker.com/engine/install/)
- [docker-compose 1.29.2](https://docs.docker.com/compose/install/)
- pip 22.3.1

To avoid conflict between any python projects in your machine and this service, it is recommended to use `pyenv` to install the
required python version. Please check [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv) documentation for further information.

## Dev Set-up

### Environment Set-up
Once you clone this repository and all prerequisites are satisfied, you can create a python [virtualenv](https://docs.python.org/3/library/venv.html) before installing the required python packages in `requirements.txt`. This recommendation of using python virtual environment is to avoid package version conflict between this service and the existing packages in your machine.

Prior virtual environment initalization, copy the environment variable example and set their values accordingly. To copy and rename the environment variable file, run the following command terminal.

```shell
cp .env.example .env
```

To initiate python virtualenv, run the following command.

```shell
python -m venv venv_django
```
After virtualenv and environment variables are set, run the following command to also load the environment variables to python virtualenv.

```shell
source venv_django/bin/activate && set -a; source .env; set +a
```
Then, you can install python packages by executing.
```shell
pip install -r requirements.txt 
```
### Database Set-up

We are using postgres to store data of Backend Engine service. To set your postgres up and running without any conflict with your local postgres, we use docker to isolate the database development from other projects. To run the postgres container, execute the following command.

```shell
docker-compose up -d db   
```

To check whether your postgres database is running in the docker container, run this command.

```shell
docker ps
```

Before running server in your local, you need to run db migration by executing the following command
```shell
python manage.py migrate
```

When you edit models, if you want to make new migration of the new model changes, run this command
```shell
python manage.py makemigrations <app>
```

To show all migrations applied, run this command
```shell
python manage.py showmigrations
```

To rollback migration, run this command and specify the migration state
```shell
python manage.py migrate <app> <000X_expected migration state>
```
To rollback to the very first state, run
```shell
python manage.py migrate <app> zero
```

Once development is done in your local machine, you can shut down your database (or any container service in Backend Engine) by running this command.

```shell
docker-compose down
```

### Run Server

Finally, to run Backend Engine, run the following command.
```shell
python manage.py runserver
```
Backend Engine should be running in your machine and can be accessed at your `localhost:8000`.

## Test, Code Coverage, and Linter

To run tests, run the following command
```shell
python manage.py test 
```

To check code coverage, run
```shell
coverage report -m --skip-covered
```

To check linter violation, run
```shell
flake8 <app>
```

And finally, to fix any linter violation, run
```shell
autopep8 --in-place --recursive <app>
```

## API Doc
The list of available APIs can be found at `localhost:8000/`.
