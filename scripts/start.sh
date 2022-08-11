#!/usr/bin/env bash
set -euo pipefail

. /amnesia/scripts/init_db.sh
. /amnesia/scripts/run_migrations.sh up

echo "Starting server"
python /amnesia/main.py
