FROM python:3.8-alpine

LABEL maintainer ="Juan Manuel Castillo Nievas <jumacasni@correo.ugr.es>"

ENV PATH="/home/playme/.local/bin:${PATH}"

RUN apk update \
	&& apk add bash \
	&& adduser -D playme

WORKDIR /app/test

USER playme

RUN pip3 install invoke pytest assertpy fastapi requests loguru

CMD ["invoke", "test"]