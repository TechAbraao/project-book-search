#!/bin/bash

if [ ! -f .env ]; then
    echo "❌ Arquivo .env não encontrado! Certifique-se de que ele existe."
    exit 1
fi

export $(grep -v '^#' .env | xargs)

if [[ -z "$FLASK_RUN_HOST" || -z "$FLASK_RUN_PORT" ]]; then
    echo "❌ As variáveis FLASK_RUN_HOST ou FLASK_RUN_PORT não estão definidas no .env!"
    exit 1
fi

flask run --host=$FLASK_RUN_HOST --port=$FLASK_RUN_PORT