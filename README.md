# MC Log Web Viewer

Log Web Viewer to Minecraft Servers

[GitHub](https://github.com/zicstardust/mclogwebviewer)

## Container
### Tags

| Tag | Description |
| :----: | :----: |
| [`latest`](https://github.com/zicstardust/mclogwebviewer/blob/main/dockerfile) | Default Tag |

### Registries
| Registry | Full image name | Description |
| :----: | :----: | :----: |
| [`docker.io`](https://hub.docker.com/r/zicstardust/mclogwebviewer) | `docker.io/zicstardust/mclogwebviewer` | Docker Hub |
| [`ghcr.io`](https://github.com/zicstardust/mclogwebviewer/pkgs/container/mclogwebviewer) | `ghcr.io/zicstardust/mclogwebviewer` | GitHub |


### Supported Architectures

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| 386 | ✅ | latest |
| amd64 | ✅ | latest |
| arm/v6 | ✅ | latest |
| arm/v7 | ✅ | latest |
| arm64 | ✅ | latest |
| ppc64le | ✅ | latest |
| riscv64 | ✅ | latest |
| s390x | ✅ | latest |


## Usage
### Compose
``` yml
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
| `APP_TITLE` | Set Page Title | MC Log Web Viewer  |
| `FILTER_TEXT` | Lines containing the text of this variable will not appear, separator "," | |
| `SCHEDULE_INTERVAL` | Time to generate a new scan of the log files. Example: `30s`: 30 seconds, `5m`: 5 minutes, `1d`: 1 day, `1w`: 1 week, `0`: Will scan every time the application is accessed. | 0 |
