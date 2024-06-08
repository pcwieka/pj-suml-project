ARG BASE_IMAGE=python:3.10-slim
FROM $BASE_IMAGE as runtime-environment
RUN apt-get update && apt-get install -y build-essential
COPY docker/kedro/requirements.txt /tmp/requirements.txt
RUN pip install 'kedro[all]'
RUN pip install --no-cache -r /tmp/requirements.txt && \
rm -f /tmp/requirements.txt
ARG KEDRO_UID=999
ARG KEDRO_GID=1001
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker
WORKDIR /home/kedro_docker
USER kedro_docker
COPY --chown=${KEDRO_UID}:${KEDRO_GID} . .
EXPOSE 8888
CMD ["tail", "-f", "/dev/null"]
