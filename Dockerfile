# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10 as compile-image

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

FROM python:3.10-slim AS build-image

COPY --from=compile-image /opt/venv /app/venv
WORKDIR /app
COPY . /app
RUN mkdir -p /boxscores
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app /boxscores
USER appuser
VOLUME /boxscores

CMD ["/app/venv/bin/python", "-m", "celery", "-A", "boxscores",  "worker", "-Q", "boxscores", "-l", "debug"]
