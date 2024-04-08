FROM python:3.10.12-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # PIP
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    POETRY_VERSION=1.8.1 \
    # Set local instalation from poetry
    POETRY_HOME="/opt/poetry" \
    # Set poetry virtual enviroment in project root
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # Paths
    # settings of project requirements and virtual enviroment
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Using `builder-base` to build dependences and poetry's virtual enviroment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install -y \
        # deps for installing poetry and building python deps
        curl \
        build-essential

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# setting virtual enviroment path and dependences for poetry
WORKDIR $PYSETUP_PATH
# copy of poetry's dependences
COPY poetry.lock pyproject.toml README.md ./

# install runtime deps - using $POETRY_VIRTUALENVS_IN_PROJECT
RUN poetry install --no-root

WORKDIR /app

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]