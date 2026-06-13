#!/usr/bin/env python3
"""
Illustration Fetcher - Reference external images (no download)
Generates Wikimedia Commons Special:FilePath URLs for lessons.
"""

import sys
import re

def get_wikimedia_url(filename, width=640):
    """Generate Wikimedia Commons direct file URL"""
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{filename}?width={width}"

def get_unsplash_url(query, width=800, height=600):
    """Generate Unsplash source URL"""
    from urllib.parse import quote
    return f"https://source.unsplash.com/{width}x{height}/?{quote(query)}"

def suggest_images_for_concept(concept):
    """Suggest Wikimedia Commons filenames for common concepts"""
    suggestions = {
        "aristotle": "Aristotle_Altemps_Inv8575.jpg",
        "venn diagram": "Venn3.svg",
        "directed graph": "Example_of_simple_directed_graph.svg",
        "domino": "Domino_effect_(50_fps).gif",
        "euler circuit": "Eulerian_path.svg",
        "logic gates": "Logic_gates.svg",
        "truth table": "Karnaugh_map_3_variables.svg",
        "boolean algebra": "Boolean_algebra.svg",
        "quantifiers": "First-order_logic.svg",
        "induction": "Domino_effect.svg",
        "bayes": "Bayes_theorem.svg",
        "inclusion exclusion": "Inclusion-exclusion.svg",
    }

    # Find best match
    concept_lower = concept.lower()
    for key, filename in suggestions.items():
        if key in concept_lower:
            return get_wikimedia_url(filename)

    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: suggest.py <concept>")
        print("Example: suggest.py 'venn diagram'")
        sys.exit(1)

    concept = sys.argv[1]
    url = suggest_images_for_concept(concept)

    if url:
        print(f"Suggested URL for '{concept}':")
        print(url)
    else:
        print(f"No suggestion for '{concept}'")
        print("Try: aristotle, venn diagram, directed graph, domino, etc.")
