#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
    echo "Usage: ./migrate-db.sh <up/down/create>"
fi

SEEDS_PATH=/srv/root/database/seeds
SEEDS_SCHEMA_TABLE=schema_seeds

DB_DSN="mysql://${DB_USER}:${DB_PASS}@tcp(${DB_HOST}:${DB_PORT})/${DB_NAME}?x-migrations-table=${SEEDS_SCHEMA_TABLE}&tls=${DB_USE_SSL}"

case "$1" in
    up)
        echo "Running seeds (up)"
        # TODO: should this be -path instead of -source?
        go-migrate -source "file://${SEEDS_PATH}" -database $DB_DSN $@
        echo "Ran seeds successfully"
    ;;

    down)
        echo "Running seeds (down)"
        yes | go-migrate -source "file://${SEEDS_PATH}" -database $DB_DSN $@
        echo "Ran seeds successfully"
    ;;

    create)
        raw_input=$2
        lower_input=${raw_input,,}
        cleaned_input=${lower_input// /_}

        echo "Creating seed"
        go-migrate create -ext sql -dir $SEEDS_PATH -seq $cleaned_input
        echo "Created seed successfully"
    ;;

    *)
        echo "'$1' is not a known value for the first parameter"
    ;;
esac
