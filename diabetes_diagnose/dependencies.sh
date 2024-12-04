#!/bin/bash

# Ejecución con SUDO 
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta este script como administrador (con sudo)." >&2
  exit 1
fi

# Actualizar apt
echo "Actualizando el sistema..."
sudo apt update -y && sudo apt upgrade -y

# CONDA
if ! command -v conda &> /dev/null; then
  echo "Conda no está instalado. Instalándolo ahora..."

  # Instalador miniconda
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

  # Ejecutar instalador miniconda
  bash miniconda.sh -b -p $HOME/miniconda

  # Añadir Conda al PATH temporalmente para este script
  export PATH="$HOME/miniconda/bin:$PATH"

  # Inicializar conda
  conda init
  source ~/.bashrc

  echo "Conda instalado correctamente."
else
  echo "Conda ya está instalado."
fi

# Crear entorno diabetes
echo "Creando el entorno 'diabetes'..."
conda create --name diabetes python=3.11 -y

# Activar entorno diabetes
echo "Activando el entorno 'diabetes'..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate diabetes

# Instalar librerías
echo "Instalando librerías: pgmpy y pandas..."
pip install pgmpy pandas

# Mensaje éxito
echo "¡Entorno 'diabetes' configurado correctamente con Python, pgmpy y pandas!"
