#!/usr/bin/env bash
set -euo pipefail

trap "{ exit 0; }" TERM INT

cd /srv/root

/scripts/init-db.sh

/scripts/migrate-db.sh up
/scripts/seed-db.sh up

/scripts/run-service.sh
