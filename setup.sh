#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "Instalando dependências no ambiente virtual..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Para Windows
    source venv/Scripts/activate
else
    # Para Linux/Mac
    source venv/bin/activate
fi

pip install -r requirements.txt
echo "Setup concluído! Ative o ambiente virtual com: source venv/bin/activate"
