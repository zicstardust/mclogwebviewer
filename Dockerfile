FROM python:3.15.2-alpine3.24

ENV PYTHONUNBUFFERED=1
ENV PATH="/home/mcwebserver/.local/bin:${PATH}"

ENV ICON="/server-icon.png"

WORKDIR /app

COPY pyproject.toml .
COPY /src .
COPY entrypoint.sh /entrypoint.sh

RUN apk update; \
    apk upgrade -a; \
    \
    chmod +x /entrypoint.sh; \
    \
    apk add --no-cache su-exec shadow; \
    \
    adduser -D -u 1000 -s /bin/nologin -h /home/mcwebserver mcwebserver; \
    chown -R mcwebserver:mcwebserver /home/mcwebserver; \
    chown -R mcwebserver:mcwebserver /app; \
    \
    su-exec mcwebserver pip3 install --no-cache-dir --user .

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "server.py"]
