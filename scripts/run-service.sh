#!/usr/bin/env bash
set -euo pipefail

exec uvicorn \
    --host $APP_HOST \
    --port $APP_PORT \
    --no-access-log \
    app.api_boot:api
