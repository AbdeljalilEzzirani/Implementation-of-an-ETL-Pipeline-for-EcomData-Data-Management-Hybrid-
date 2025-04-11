# FROM apache/airflow:2.9.0
# USER airflow
# RUN pip install --no-cache-dir pandas faker

FROM apache/nifi:latest

USER root
# RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean
# USER nifi

# # Copie des fichiers de configuration personnalisés
# COPY ./conf/nifi.properties /opt/nifi/nifi-current/conf/nifi.properties

# # Création des répertoires nécessaires
# RUN mkdir -p /opt/nifi/nifi-current/python_extensions /opt/nifi/nifi-current/nar_extensions /opt/nifi/nifi-current/staging