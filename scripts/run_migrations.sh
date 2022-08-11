#!/usr/bin/env bash
set -euo pipefail

MIGRATIONS_PATH=/amnesia/migrations
MIGRATIONS_SOURCE=file://$MIGRATIONS_PATH

DB_DSN="postgresql://$WRITE_DB_USER:$WRITE_DB_PASS@$WRITE_DB_HOST:$WRITE_DB_PORT/$WRITE_DB_NAME?sslmode=disable"

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <up/down/create> <args ...>"
    exit 1
fi

case "$1" in
    up)
        migrate -source $MIGRATIONS_SOURCE -database $DB_DSN $@
        echo "Migrate up completed."
        ;;
    down)
        yes | migrate -source $MIGRATIONS_SOURCE -database $DB_DSN $@
        echo "Migrate down completed."
        ;;
    create)
        raw=$2
        lower=${raw,,}
        cleaned=${lower// /_}
        migrate create -ext sql -dir $MIGRATIONS_PATH -seq $cleaned
        echo "Created migrations."
        ;;
    *)
        echo "Usage: $0 <up/down/create> <args ...>"
        exit 1
        ;;
esac
