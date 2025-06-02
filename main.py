from iching import load_hexagrams, draw_hexagram, format_hexagram
def main():

    print("Welcome to Terminal I Ching!")
    input("Press [Enter] to draw a hexagram...")
    # Load hexagrams from the file
    try:
        hexagrams = load_hexagrams()
        
    except FileNotFoundError:
        print("Error: Hexagram data file not found. Please ensure the file exists.")
        return

    # Draw a hexagram (e.g., hexagram 1)
    
    hexagram = draw_hexagram(hexagrams)

    # Format the hexagram for display
    formatted_hexagram = format_hexagram(hexagram)

    # Print the formatted hexagram
    print(f' \n{formatted_hexagram}')

if __name__ == "__main__":
    main()
    print("Thank you for using Terminal I Ching!")
    # input("Press [Enter] to exit...")