#!/bin/bash

# Verifica si el script está siendo ejecutado con privilegios de administrador
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta este script como administrador (usando sudo)." >&2
  exit 1
fi

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update -y && sudo apt upgrade -y

# Verifica si conda está instalado
if ! command -v conda &> /dev/null; then
  echo "Conda no está instalado. Instalándolo ahora..."

  # Descarga el instalador de Miniconda
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

  # Ejecuta el instalador de Miniconda
  bash miniconda.sh -b -p $HOME/miniconda

  # Añade Conda al PATH temporalmente para este script
  export PATH="$HOME/miniconda/bin:$PATH"

  # Inicializa conda
  conda init
  source ~/.bashrc

  echo "Conda instalado correctamente."
else
  echo "Conda ya está instalado."
fi

# Crea un entorno conda llamado "diabetes"
echo "Creando el entorno 'diabetes'..."
conda create --name diabetes python=3.11 -y

# Activa el entorno "diabetes"
echo "Activando el entorno 'diabetes'..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate diabetes

# Instala las bibliotecas necesarias
echo "Instalando bibliotecas: pgmpy y pandas..."
pip install pgmpy pandas

echo "¡Entorno 'diabetes' configurado correctamente con Python, pgmpy y pandas!"
