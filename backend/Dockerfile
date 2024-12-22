FROM python:3.12.2-slim

ARG ENV

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    BASE_DIR=/code \
    POETRY_VERSION=1.8.0

RUN pip install psycopg2-binary

WORKDIR $BASE_DIR

# System deps:
RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml $BASE_DIR

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-root

COPY . $BASE_DIR

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
