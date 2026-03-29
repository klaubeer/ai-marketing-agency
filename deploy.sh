#!/bin/bash
set -e

PROJECT_DIR="/root/projetos/ai-marketing-agency"
REPO="https://github.com/klaubeer/ai-marketing-agency"

echo "=== Verificando instância do Traefik ativa ==="
docker inspect traefik | grep "com.docker.compose.project.working_dir" || echo "[AVISO] Traefik não encontrado com nome 'traefik'"

echo ""
echo "=== Verificando rede proxy ==="
docker network inspect proxy > /dev/null 2>&1 || { echo "[ERRO] Rede 'proxy' não existe. Crie com: docker network create proxy"; exit 1; }

echo ""
echo "=== Preparando diretório do projeto ==="
if [ -d "$PROJECT_DIR" ]; then
    echo "Diretório já existe — atualizando via git pull..."
    cd "$PROJECT_DIR"
    git pull
else
    echo "Clonando repositório..."
    mkdir -p /root/projetos
    git clone "$REPO" "$PROJECT_DIR"
    cd "$PROJECT_DIR"
fi

echo ""
echo "=== Verificando .env.prod ==="
if [ ! -f ".env.prod" ]; then
    cp .env.prod.example .env.prod
    echo ""
    echo "[AÇÃO NECESSÁRIA] .env.prod criado a partir do exemplo."
    echo "Preencha o arquivo antes de continuar:"
    echo "  nano $PROJECT_DIR/.env.prod"
    echo ""
    echo "Depois rode novamente: bash deploy.sh"
    exit 0
fi

echo ""
echo "=== Subindo containers ==="
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build

echo ""
echo "=== Status dos containers ==="
docker compose -f docker-compose.prod.yml ps

echo ""
echo "=== Deploy concluído! ==="
echo "URL: https://mkto.klauberfischer.online"
