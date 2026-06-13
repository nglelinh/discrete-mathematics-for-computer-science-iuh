#!/usr/bin/env python3
"""
Illustration Fetcher - Download and validate educational images
Supports: Wikimedia Commons, Unsplash, Placeholder
Validates image content before saving.
"""

import sys
import os
import requests
from urllib.parse import quote
import time

def is_valid_image(content, content_type=None):
    """Check if content is a valid image"""
    if len(content) < 1024:
        return False

    # Check magic bytes
    if content.startswith(b'<?xml') or content.startswith(b'<svg'):
        return True
    if content.startswith(b'\x89PNG'):
        return True
    if content.startswith(b'\xFF\xD8'):
        return True
    if content.startswith(b'GIF8'):
        return True

    # Check if it's HTML error page
    if b'<!DOCTYPE' in content[:100] or b'<html' in content[:100]:
        return False

    return True

def download_wikimedia(query, output_path):
    """Try to find and download from Wikimedia Commons"""
    # Common educational diagram filenames
    common_files = [
        f"{query.replace(' ', '_')}.svg",
        f"{query.replace(' ', '_')}.png",
    ]

    base_url = "https://commons.wikimedia.org/wiki/Special:FilePath/"

    for filename in common_files:
        url = f"{base_url}{quote(filename)}?width=800"
        try:
            resp = requests.get(url, timeout=10, allow_redirects=True)
            if resp.status_code == 200 and is_valid_image(resp.content):
                with open(output_path, 'wb') as f:
                    f.write(resp.content)
                print(f"✓ Downloaded from Wikimedia: {filename}")
                return True
        except:
            continue

    return False

def download_unsplash(query, output_path):
    """Download from Unsplash source"""
    url = f"https://source.unsplash.com/800x600/?{quote(query)}"

    try:
        resp = requests.get(url, timeout=15, allow_redirects=True)
        if resp.status_code == 200 and is_valid_image(resp.content):
            with open(output_path, 'wb') as f:
                f.write(resp.content)
            print(f"✓ Downloaded from Unsplash: {query}")
            return True
    except Exception as e:
        print(f"Unsplash error: {e}")

    return False

def download_placeholder(query, output_path):
    """Create placeholder as last resort"""
    # Use via.placeholder.com
    text = quote(query[:30])
    url = f"https://via.placeholder.com/800x600/3498db/ffffff?text={text}"

    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(resp.content)
            print(f"⚠ Created placeholder: {query}")
            return True
    except:
        pass

    return False

def fetch_illustration(query, output_path, prefer_diagram=True):
    """
    Try multiple sources to find a valid illustration.
    Returns True if successful.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"\nSearching for: {query}")

    # Try Wikimedia first (best for diagrams)
    if download_wikimedia(query, output_path):
        return True

    time.sleep(1)

    # Try Unsplash
    if download_unsplash(query, output_path):
        return True

    time.sleep(1)

    # Fallback to placeholder
    if download_placeholder(query, output_path):
        return True

    print(f"✗ Could not find image for: {query}")
    return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: illustration_fetcher.py <query> <output_path>")
        sys.exit(1)

    query = sys.argv[1]
    output = sys.argv[2]

    success = fetch_illustration(query, output)
    sys.exit(0 if success else 1)
