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

# Instalar pip si no está disponible
if ! command -v pip &> /dev/null; then
  echo "Pip no está instalado. Instalándolo ahora..."
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  echo "Pip instalado correctamente."
else
  echo "Pip ya está instalado."
fi

# Instalar librerías
echo "Instalando librerías: pgmpy y pandas..."
pip install --upgrade pip
pip install pgmpy pandas

# Comprobaciones finales
echo "Verificando las instalaciones..."

# Verificar Python
if command -v python &> /dev/null; then
  PYTHON_VERSION=$(python --version 2>&1)
  echo "Python instalado: $PYTHON_VERSION"
else
  echo "Error: Python no está instalado correctamente."
  exit 1
fi

# Verificar pip
if command -v pip &> /dev/null; then
  PIP_VERSION=$(pip --version)
  echo "Pip instalado: $PIP_VERSION"
else
  echo "Error: Pip no está instalado correctamente."
  exit 1
fi

# Verificar pgmpy
if python -c "import pgmpy" &> /dev/null; then
  echo "pgmpy instalado correctamente."
else
  echo "Error: pgmpy no está instalado."
  exit 1
fi

# Verificar pandas
if python -c "import pandas" &> /dev/null; then
  echo "pandas instalado correctamente."
else
  echo "Error: pandas no está instalado."
  exit 1
fi

# Mensaje final solo si todo está correcto
echo "¡Entorno 'diabetes' configurado correctamente con Python, pip, pgmpy y pandas!"
