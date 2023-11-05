from bottle import Bottle, request, run, template
import re

app = Bottle()

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...'
}

@app.route('/')
def index():
    return template('index')

@app.route('/convert', method='POST')
def convert():
    text = request.forms.get('text', '').upper()
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
