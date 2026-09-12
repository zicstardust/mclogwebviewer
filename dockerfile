FROM python:3.14.7-alpine

ENV PYTHONUNBUFFERED=1
ENV PUID=1000
ENV PGID=1000

ENV ICON="/server-icon.png"

WORKDIR /app

COPY requirements.txt .
COPY /src .
COPY entrypoint.sh /entrypoint.sh

RUN apk update; \
    apk upgrade -a; \
    \
    chmod +x /entrypoint.sh; \
    \
    apk add --no-cache su-exec shadow; \
    \
    addgroup mcwebserver -g ${PGID}; \
    adduser -D -u ${PUID} -G mcwebserver mcwebserver; \
    mkdir -p /home/mcwebserver; \
    chown -R mcwebserver:mcwebserver /home/mcwebserver; \
    su-exec mcwebserver pip3 install --no-warn-script-location --user --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "server.py"]
