# Imagen Base
FROM python:3.10.4-slim-bullseye

#Seteamos las variable de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Setear el directorio de trabajo
WORKDIR /code

#INSTALAR DEPENDENCIAS
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .