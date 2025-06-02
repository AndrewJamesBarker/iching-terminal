import json
import random
from pathlib import Path

def load_hexagrams():
    
    path = Path(__file__).parent / "assets/json/hexagrams_full.json"
    # print("Looking for:", path)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    

def draw_hexagram(hexagrams):
    hexagram_num = random.randint(1, 64)
    # Ensure the hexagram number is within the valid range
    if 1 <= hexagram_num <= 64:
        return hexagrams[str(hexagram_num)]
    else:
        raise ValueError("Hexagram number must be between 1 and 64.")

def format_hexagram(hexagram):
    return (
        f"Hexagram {hexagram['hex']}: {hexagram['english']} {hexagram['hex_font']}\n\n"
        f"Image Description: {hexagram.get('wilhelm_image', {}).get('text', 'No image description available')}\n\n"
        f"Symbolic Interpretation: {hexagram['wilhelm_symbolic']}\n"
    )