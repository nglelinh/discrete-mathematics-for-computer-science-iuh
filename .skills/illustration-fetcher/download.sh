#!/usr/bin/env bash
# Wrapper script for illustration-fetcher skill

QUERY="$1"
OUTPUT="$2"

if [ -z "$QUERY" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: $0 <search_query> <output_path>"
    exit 1
fi

python3 "$(dirname "$0")/fetch.py" "$QUERY" "$OUTPUT"
