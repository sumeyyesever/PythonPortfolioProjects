MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ',': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def string_to_morse(user_string):
    morse_code = ""
    for ch in user_string:
        if ch == " ":
            morse_code += " "
        else:
            morse_code += MORSE_CODE_DICT[ch] + " "
    return morse_code


# improvement-> when the user string not one word but multiple words??
# add main function

def main():
    print("Welcome")
    user_input = input("Enter a string(only english characters): ").upper()
    morse_code_ver = string_to_morse(user_input)
    print(f"Here is the morse code version of your input: {morse_code_ver} ")


if __name__ == '__main__':
    main()
