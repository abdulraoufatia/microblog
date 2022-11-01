FROM python:3.11.0-slim as base

WORKDIR /app

ENV PATH="${PATH}:/root/.poetry/bin" 

ARG DEV_PORT=4000

RUN apt-get update \
    && apt-get -y install curl \
    && apt-get -y install openssl \
    && curl -sSL https://install.python-poetry.org | python3 -

EXPOSE ${DEV_PORT}  

COPY . /app/

RUN poetry config virtualenvs.create false --local && poetry install

ENV PATH="${PATH}:/root/.local/bin"

FROM base as development

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as production

CMD poetry run gunicorn -b 0.0.0.0:$PORT "app.routes:app"