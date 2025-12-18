FROM python:3.14.2-alpine

ENV PYTHONUNBUFFERED=1
ENV PUID=1000
ENV PGID=1000

WORKDIR /app

COPY requirements.txt .
COPY /src .

RUN apk add --no-cache su-exec shadow; \
    addgroup mcwebserver -g ${PGID}; \
    adduser -D -u ${PUID} -G mcwebserver mcwebserver; \
    mkdir -p /home/mcwebserver; \
    chown -R mcwebserver:mcwebserver /home/mcwebserver; \
    su-exec mcwebserver pip3 install --user --no-cache-dir -r requirements.txt

ENV PATH="/home/mcwebserver/.local/bin:${PATH}"

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
#CMD ["waitress-serve", "--port=5000", "--call", "app:app"]
CMD ["python", "server.py"]