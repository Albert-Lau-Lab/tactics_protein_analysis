# syntax=docker/dockerfile:1
FROM pegi3s/pymol

WORKDIR /tactics_docker_dir

COPY vmd-1.9.3.bin.LINUXAMD64.text.tar .
COPY docker_install_script.sh .
RUN chmod +x docker_install_script.sh
RUN ./docker_install_script.sh
