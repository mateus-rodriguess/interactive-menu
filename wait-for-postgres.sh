#!/bin/bash
# wait-for-postgres.sh

# Stop execution if we have an error
set -e

# Get host:port from parameters list
host="$1"

# Remove first argument from list of parameters (host)
shift

# Try to connect to PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "... Postgres is unavailable - sleeping ..."
  sleep 3
done

>&2 echo "... Postgres is up - executing command ..."

# Execute given other parameters (commands)
exec "$@"