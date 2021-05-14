morse_code = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--..",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----",
              ".": ".-.-.-",
              ",": "--..--",
              "?": "..--..",
              "!": "-.-.--",
              "'": ".----."}


def encoding(paragraph):
    """Loops through every character in the phrase supplied to find corresponding morse code.
     Returns the translation in string format.
     """
    translation = ""

    for char in paragraph:
        if char in morse_code:
            translation += morse_code[char] + ","
        elif char == " ":
            translation += "......." + ","
        else:
            print(f"Illegal character entered: {char}")

    return translation


def decoding(paragraph):
    """Loops through the morse code string to find the corresponding letters. Returns everything in lower
    case since Morse Code does not differentiate between Capital and Lower case."""
    translation = ""

    for split in paragraph.split(","):
        for key, value in morse_code.items():
            if split == value:
                translation += key
        if split == ".......":
            translation += " "

    return translation


encode = input("Please enter a phrase to translate in Morse Code:\n").lower()

print(encoding(encode))

decode = input("Please enter Morse Code to decode. Every letter's code must be followed by a comma(,):\n")

print(decoding(decode))
