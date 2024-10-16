#!/bin/bash

# 设置变量
INSTALLATION_DIRECTORY="/home/DebianNas"
ADMIN_USERNAME="admin"
ADMIN_PASSWORD="DebianNasPassword1."
TZ="Asia/Shanghai"
STORAGE_PATH="/home/storage"
PHOTOS_PATH="/home/storage/photos"
VIDEOS_PATH="/home/storage/videos"
MUSICS_PATH="/home/storage/musics"
NOTES_PATH="/home/storage/notes"
DOWNLOAD_PATH="/home/storage/download"

# 创建安装目录
mkdir -p "$INSTALLATION_DIRECTORY"
cd "$INSTALLATION_DIRECTORY"

# 安装docker compose
# curl -SL https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose
# sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
# docker-compose --version

# 服务端口定义
PORTAINER_HTTP_PORT=1001
PORTAINER_HTTPS_PORT=1002
PORTAINER_TCP_PORT=1003
ALIST_PORT=1006
MT_PHOTOS_WEBUI_PORT=1011
QBITTORRENT_PORT=1016
ARIA2_PORT=1021
ARIANG_PORT=1026
NAVIDROME_WEBUI_PORT=1031
BAIDUNETDISK_WEBUI_PORT=1036
BAIDUNETDISK_WEBUI_PORT2=1037
FRESHRSS_WEBUI_PORT=1041

# 创建.env文件
cat > .env <<EOF
INSTALLATION_DIRECTORY=$INSTALLATION_DIRECTORY
GLOBAL_USER=$ADMIN_USERNAME
GLOBAL_PASSWORD=$ADMIN_PASSWORD
PORTAINER_HTTP_PORT=$PORTAINER_HTTP_PORT
PORTAINER_HTTPS_PORT=$PORTAINER_HTTPS_PORT
PORTAINER_TCP_PORT=$PORTAINER_TCP_PORT
ALIST_PORT=$ALIST_PORT
MT_PHOTOS_WEBUI_PORT=$MT_PHOTOS_WEBUI_PORT
QBITTORRENT_PORT=$QBITTORRENT_PORT
ARIA2_PORT=$ARIA2_PORT
ARIANG_PORT=$ARIANG_PORT
NAVIDROME_WEBUI_PORT=$NAVIDROME_WEBUI_PORT
BAIDUNETDISK_WEBUI_PORT2=$BAIDUNETDISK_WEBUI_PORT2
FRESHRSS_WEBUI_PORT=$FRESHRSS_WEBUI_PORT
EOF

# 定义compose文件夹路径
COMPOSE_FOLDER="$INSTALLATION_DIRECTORY/compose"

# 遍历compose文件夹中的yaml文件
for filename in "$COMPOSE_FOLDER"/*docker-compose-*.yaml; do
    if [ -f "$filename" ]; then
        service_name=$(echo "$filename" | sed 's/.*docker-compose-\(.*\)\.yaml/\1/')
        service_folder="$INSTALLATION_DIRECTORY/$service_name"

        # 创建服务文件夹
        mkdir -p "$service_folder"
        #cp .env "$service_folder/.env"

        # 进入服务文件夹并启动docker容器
        cd "$service_folder"
        docker compose -f "$filename" --env-file=$INSTALLATION_DIRECTORY/.env up -d
        cd "$INSTALLATION_DIRECTORY"
    fi
done