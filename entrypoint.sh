#!/bin/sh
set -e
PUID="${PUID:-1000}"
PGID="${PGID:-1000}"

if [ "$(id -g mcwebserver)" != "${PGID}" ]; then
    groupmod -o -g "${PGID}" mcwebserver
fi


if [ "$(id -u mcwebserver)" != "${PUID}" ]; then
    usermod -o -u "${PUID}" mcwebserver
fi

mkdir -p /data /logs
chown -R mcwebserver:mcwebserver /home/mcwebserver /data /app

exec su-exec mcwebserver "$@"
