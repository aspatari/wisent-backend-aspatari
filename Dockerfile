FROM python:3.8.5-alpine

WORKDIR /app
ARG ENV
ENV ENV=${ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.0.0

RUN addgroup -S wisent \
  && adduser -S -G wisent wisent

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev git make\
  && apk add postgresql-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  # LDAP dependencies
  && pip install "poetry==$POETRY_VERSION"

# Requirements are installed here to ensure they will be cached.
COPY ./poetry.lock ./pyproject.toml /app/
RUN  poetry config virtualenvs.create false \
  && poetry install $(test "$ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app

CMD ["python3","main.py"]
