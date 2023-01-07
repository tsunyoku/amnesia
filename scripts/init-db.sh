#!/usr/bin/env bash
set -euo pipefail

execDBStatement() {
  if [[ "$DB_USE_SSL" == "true" ]]; then
    EXTRA_PARAMS="--ssl"
  else
    EXTRA_PARAMS=""
  fi

  mysql \
  --host=$DB_HOST \
  --port=$DB_PORT \
  --user=$DB_USER \
  --password=$DB_PASS \
  --protocol=tcp \
  $EXTRA_PARAMS \
  --execute="$1"
}

execDBStatement "CREATE DATABASE IF NOT EXISTS ${DB_NAME}"
