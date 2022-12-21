# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11 as compile-image

RUN python -m venv /opt/venv

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

FROM python:3.8-slim AS build-image

COPY --from=compile-image /opt/venv /opt/venv
WORKDIR /app
COPY . /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "venv/lib/python3.11/site-packages/_distutils_hack/override.py"]
