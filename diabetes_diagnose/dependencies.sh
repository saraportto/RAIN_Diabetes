#!/bin/bash

# Verifica si el script está siendo ejecutado con privilegios de administrador
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta este script como administrador (usando sudo)." >&2
  exit 1
fi

echo "Actualizando lista de paquetes..."
sudo apt update && sudo apt upgrade -y

echo "Instalando Python 3.11..."
sudo apt install -y python3.11 python3.11-venv python3.11-dev

echo "Configurando Python 3.11 como predeterminado..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --set python3 /usr/bin/python3.11

echo "Instalando pip para Python 3.11..."
sudo apt install -y python3-pip

echo "Instalando bibliotecas necesarias: pgmpy, pandas, y time..."
pip install pgmpy pandas time

echo "¡Instalación completada!"

