#!/bin/sh
set -e

# Renew certificates quietly, without self-upgrade
certbot renew --quiet --no-self-upgrade

# Wait and then renew again in a loop (renew every 12 hours)
while true; do
    certbot renew --quiet --no-self-upgrade || true   # swallow 1
    sleep 12h
done
