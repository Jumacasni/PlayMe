FROM python:3.8-alpine

LABEL maintainer ="Juan Manuel Castillo Nievas <jumacasni@correo.ugr.es>"

RUN apk update \
	&& apk add bash \
	&& adduser -D -h /home/playme -s /bin/bash playme \
	&& mkdir -p /app/test \
	&& chown playme /app/test

WORKDIR /app/test

COPY requirements.txt .

RUN pip3 install -r requirements.txt \
	&& rm requirements.txt

USER playme

CMD ["invoke", "test"]