FROM python:3.10.6-slim-bullseye as base

WORKDIR /app

ENV PATH="${PATH}:/root/.poetry/bin" 

ARG DEV_PORT=4000

RUN apt-get update \
    && apt-get -y install curl \
    && apt-get -y install openssl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

EXPOSE ${DEV_PORT}  

COPY . /app/

RUN poetry config virtualenvs.create false --local && poetry install

FROM base as development

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as production

CMD poetry run gunicorn -b 0.0.0.0:$PORT "app.routes:app"