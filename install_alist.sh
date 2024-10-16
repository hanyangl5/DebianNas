curl -fsSL "https://alist.nn.ci/v3.sh" | bash -s install

curl -fsSL "https://alist.nn.ci/v3.sh" | bash -s update

docker exec -it alist ./alist admin set NEW_PASSWORD