import json
import random
from pathlib import Path

def load_hexagrams():
    path = Path(__file__).parent / "assets/json/hexagrams_full.json"
    # print("Looking for:", path)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def toss_line():
    # Simulate three coin tosses and sum the results
    tosses = [random.choice([2, 3]) for _ in range(3)]
    total = sum(tosses)
    # Return the line based on the total
    if total == 6:
        return '--x'  # Old Yin (changing)
    elif total == 7:
        return '—'    # Young Yang
    elif total == 8:
        return '--'   # Young Yin
    elif total == 9:
        return '—o'   # Old Yang (changing)
    return total
    

def hex_to_binary(hexagram):
    # Reverse because json data left to right symbolizes top to bottom
    reversed_lines = hexagram[::-1]
    # Convert hexagram lines to binary representation
    binary_string = ''.join(['1' if line == '—' or line == '—o' else '0' for line in reversed_lines])
    return binary_string
    

def generate_hexagram():
    hexagram = []
    for _ in range(6):
        line = toss_line()
        hexagram.append(line)
    return hexagram

def moving_lines(hexagram):
    # Identify moving lines (changing lines)
    return [i + 1 for i, line in enumerate(hexagram) if line in ['--x', '—o']]


def draw_hexagram(hexagrams):
    hexagram_lines = generate_hexagram()
    hexagram_binary = hex_to_binary(hexagram_lines)
    
    for h in hexagrams.values():
        if h['binary'].replace(" ", "").strip() == hexagram_binary.replace(" ", "").strip():
            return h, hexagram_lines

    raise ValueError(f"No match found for binary: {hexagram_binary}")

def format_hexagram(hexagram, lines):
    moving = moving_lines(lines)
    if not moving:
        moving = "None"
    else:
        moving = ', '.join(map(str, moving))
    return (
        f"Hexagram Number {hexagram['hex']}: {hexagram['english']} {hexagram['hex_font']}\n\n"
        f"Moving Lines: {moving}\n\n"
        f"Hexagram Binary: {hexagram['binary']}\n"
        f"Image Description: {hexagram.get('wilhelm_image', {}).get('text', 'No image description available')}\n\n"
        f"Symbolic Interpretation: {hexagram['wilhelm_symbolic']}\n\n"
        f"Thanks you for using Terminal I Ching! \n"
    )