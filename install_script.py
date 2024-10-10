
INSTALLATION_DIRECTORY = "/home/Debian12Nas"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "DebianNasPassword1."
TZ = "Asia/Shanghai"
STORAGE_PATH = "/home/storage"
PHOTOS_PATH = "/home/storage/photos"
VIDEOS_PATH = "/home/storage/videos"
MUSICS_PATH = "/home/storage/musics"
NOTES_PATH = "/home/storage/notes"
DOWNLOAD_PATH = "/home/storage/download"

import os
os.makedirs(INSTALL_FOLDER, exist_ok=True)
os.chdir(INSTALL_FOLDER)

# install docker compose
import subprocess
subprocess.run("curl -SL https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose", shell=True)
# permission
subprocess.run("sudo chmod +x /usr/local/bin/docker-compose", shell=True)
# ln
subprocess.run("sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose", shell=True)
# test install
subprocess.run("docker-compose --version", shell=True)
# Services

# Portainer
PORTAINER_HTTP_PORT=1001
PORTAINER_HTTPS_PORT=1002
PORTAINER_TCP_PORT=1003
# Alist
ALIST_PORT=1006
# subprocess.run("docker exec -it alist ./alist admin set GLOBAL_PASSWORD", shell=True)
# MT Photos
MT_PHOTOS_WEBUI_PORT=1011
# qBittorrent
QBITTORRENT_PORT=1016
# Aria2
ARIA2_PORT=1021
# AriaNg
ARIANG_PORT=1026
# Navidrome
NAVIDROME_WEBUI_PORT=1031
# Baidu Netdisk
BAIDUNETDISK_WEBUI_PORT=1036
BAIDUNETDISK_WEBUI_PORT=1037
# FreshRSS
FRESHRSS_WEBUI_PORT=1041


# Create .env file
with open('.env', 'w') as env_file:
	env_file.write(f"INSTALL_FOLDER={INSTALL_FOLDER}\n")
	env_file.write(f"GLOBAL_USER={GLOBAL_USER}\n")
	env_file.write(f"GLOBAL_PASSWORD={GLOBAL_PASSWORD}\n")
	env_file.write(f"PORTAINER_PORT={PORTAINER_PORT}\n")
	env_file.write(f"ALIST_PORT={ALIST_PORT}\n")
	env_file.write(f"MT_PHOTOS_PORT={MT_PHOTOS_PORT}\n")
	env_file.write(f"QBITTORRENT_PORT={QBITTORRENT_PORT}\n")
	env_file.write(f"ARIA2_PORT={ARIA2_PORT}\n")
	env_file.write(f"ARIANG_PORT={ARIANG_PORT}\n")
	env_file.write(f"NAVIDROME_PORT={NAVIDROME_PORT}\n")
	env_file.write(f"BAIDUNETDISK_PORT={BAIDUNETDISK_PORT}\n")
	env_file.write(f"FRESHRSS_PORT={FRESHRSS_PORT}\n")

import os
import yaml

compose_folder = os.path.join(INSTALL_FOLDER, "compose")

for filename in os.listdir(compose_folder):
	if filename.startswith("docker-compose-") and filename.endswith(".yaml"):
		service_name = filename[15:-5]  # Extract service name from filename
		service_folder = os.path.join(INSTALL_FOLDER, service_name)
		
		# Create folder for the service
		os.makedirs(service_folder, exist_ok=True)
		
		# Read the docker-compose file
		# with open(os.path.join(compose_folder, filename), 'r') as file:
		# 	compose_data = yaml.safe_load(file)
		
		# Create docker container
		os.chdir(service_folder)
		subprocess.run(f"docker-compose -f {os.path.join(compose_folder, filename)} up -d", shell=True)
		os.chdir(INSTALL_FOLDER)

