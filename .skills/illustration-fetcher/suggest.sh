#!/usr/bin/env bash
# Reference external images for lessons (no download needed)

CONCEPT="$1"

if [ -z "$CONCEPT" ]; then
    echo "Usage: $0 <concept>"
    echo "Example: $0 'venn diagram'"
    exit 1
fi

python3 "$(dirname "$0")/suggest.py" "$CONCEPT"
