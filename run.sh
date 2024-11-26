#!/bin/bash

# Garantir que o script não rode Docker no ambiente local
if [ "$1" == "local" ]; then
  echo "==== Iniciando o ambiente LOCAL ===="

  # Verifica se o Docker está instalado no ambiente local
  if command -v docker &>/dev/null; then
    echo "ALERTA: Docker foi detectado no ambiente local!"
    echo "Este script não permite o uso de Docker localmente por motivos de segurança."
    echo "Por favor, remova o Docker localmente ou utilize o ambiente 'codespace' para rodar com Docker."
    exit 1
  fi

  # Comandos para rodar o ambiente local
  echo "Iniciando Postgres localmente..."
  pg_ctl -D /usr/local/var/postgres start || {
    echo "Erro ao iniciar o Postgres localmente. Verifique se ele está instalado e configurado corretamente."
    exit 1
  }

  echo "Iniciando PgAdmin localmente..."
  pgadmin4 || {
    echo "Erro ao iniciar o PgAdmin localmente. Verifique se ele está instalado corretamente."
    exit 1
  }

  echo "Ambiente LOCAL iniciado com sucesso!"

elif [ "$1" == "codespace" ]; then
  echo "==== Iniciando o ambiente CODESPACE ===="

  # Garante que as variáveis de ambiente para Codespaces estão configuradas
  export ENV_FILE=.env.codespace

  # Comandos para rodar o ambiente com Docker no Codespaces
  docker-compose up -d || {
    echo "Erro ao iniciar os containers no Codespaces. Verifique o arquivo docker-compose.yml e o ambiente Codespaces."
    exit 1
  }

  echo "Ambiente CODESPACE iniciado com sucesso!"

else
  echo "Uso incorreto do script."
  echo "Sintaxe: ./run.sh [local|codespace]"
  echo "  local     - Inicia o ambiente localmente (sem Docker)."
  echo "  codespace - Inicia o ambiente no Codespaces (com Docker)."
  exit 1
fi
