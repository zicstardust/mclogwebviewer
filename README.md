# MC Log Web Viewer

Log Web Viewer to Minecraft Servers

[GitHub](https://github.com/zicstardust/mclogwebviewer)

[Docker Hub](https://hub.docker.com/r/zicstardust/mclogwebviewer)


## Tags

| Tag | Description |
| :----: |--- |
| [`latest`](https://github.com/zicstardust/mclogwebviewer/blob/main/Dockerfile) | Default tag |

### Supported Architectures

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| 386 | ✅ | latest |
| amd64 | ✅ | latest |
| arm/v6 | ✅ | latest |
| arm/v7 | ✅ | latest |
| arm64 | ✅ | latest |
| ppc64le | ✅ | latest |
| s390x | ✅ | latest |


## Usage
### Compose
```
services:
  mclogwebviewer:
    container_name: mclogwebviewer
    image: docker.io/zicstardust/mclogwebviewer:latest
    restart: unless-stopped
    environment:
      TZ: America/New_York
    ports:
      - 8080:8080/tcp #Web port
    volumes:
      - <Minecraft Server Logs Path>:/logs:ro
      - <Minecraft Server Icon Path>:/server-icon.png:ro #Opcional
```

## Environment variables

| variables | Function | Default |
| :----: | --- | --- |
| `TZ` | Set Timezone | |
| `PUID` | Set UID with read permission on log files | 1000 |
| `PGID` | Set GID with read permission on log files | 1000 |
| `HIDE_GITHUB_ICON` | Hide GitHub icon | False |
| `MAX_LOGS` | Maximum number of old logs. If `0` displays all logs. | 0 |
