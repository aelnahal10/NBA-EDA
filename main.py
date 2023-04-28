# Generate a single line of the diamond based on the given letter and index
def generate_line(letter, index, max_index):
    if letter == 'A':  # Center 'A' with respect to the max_index
        return letter.center(2 * max_index + 1)
    else:  # Place the letter on both sides of the spaces, then center it
        spaces = 2 * index - 1
        return (letter + ' ' * spaces + letter).center(2 * max_index + 1)

# Generate diamond as a list of strings according to given character
def generate_diamond(input_char):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_index = alphabet.index(input_char)  # Find index of the input character
    diamond_lines = []  # Initialize an empty list to store diamond lines

    # Iterate over range from 0 to max_index of input character
    for i in range(max_index + 1):
        line = generate_line(alphabet[i], i, max_index)  # Generate the current line
        diamond_lines.append(line)  # Add current line to diamond_lines list

    # Return the diamond_lines list concatenated with its mirror image
    return diamond_lines + diamond_lines[-2::-1]

def print_diamond(input_char):
    diamond = generate_diamond(input_char)  # Generate the diamond as a list of strings
    for line in diamond:  # Iterate over the diamond lines and print each line
        print(line)

print_diamond('E')
