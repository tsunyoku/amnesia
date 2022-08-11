#!/usr/bin/env bash
set -euo pipefail

execDBStatement() {
  PGPASSWORD=$WRITE_DB_PASS psql \
  --dbname=postgres \
  --username=$WRITE_DB_USER \
  --host=$WRITE_DB_HOST \
  --port=$WRITE_DB_PORT \
  --command="$1"
}

execDBStatement "CREATE DATABASE ${WRITE_DB_NAME};" > /dev/null 2>&1 || true
