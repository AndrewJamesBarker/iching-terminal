# iching/__main__.py

from .hexagram import load_hexagrams, draw_hexagram, format_hexagram

def main():
    print("🎴 Terminal I Ching \n")
    question = input("Enter your question (or press Enter to skip): ")

    try:
        hexagrams = load_hexagrams()
        hexagram, lines = draw_hexagram(hexagrams)
        formatted = format_hexagram(hexagram, lines)


        if question:
            print(f'\nIn reply to your question "{question}", you have drawn:\n')
        else:
            print("\nYou have drawn:\n")

        print(formatted)

    except FileNotFoundError:
        print("Error: Hexagram data file not found.")

if __name__ == "__main__":
    main()
