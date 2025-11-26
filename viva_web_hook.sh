#!/bin/bash

# GITHUB: instead of `source .env`` file, we pass the env variables as arguments
source .env
# Environment variables are passed from GitHub Actions workflow
CREDS="$VIVA_MERCHANT_ID:$VIVA_API_KEY"
# encoded=$(echo -n "$creds" | base64)
# echo "Encoded credentials: $encoded"

# the quotes around $CREDS are important
# ensuere that it is treated as a single string
# because of the colon : - it would be split otherwise
encoded=$(echo -n "$CREDS" | base64)
curl -L 'https://demo.vivapayments.com/api/messages/config/token' \
--header "Authorization: Basic  $(echo -n $encoded)" \
--header 'Content-Type: application/json' \
--output response_hook.json

