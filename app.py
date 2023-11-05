from bottle import Bottle, request, run, template
import re
import pygame
import sound_generator

app = Bottle()

morse_code_dict = {
    'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...'
}

#reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

@app.route('/')
def index():
    return template('index.html')

@app.route('/convert', method='POST')

def convert():
    text = request.forms.get('text', '').upper()
    morse_code = ''

    text = re.sub(r'\s+', ' ', text)
    
    for c in text:
        if c in morse_code_dict:
            morse_code += morse_code_dict[c] + ' '
        elif c == ' ':
            morse_code += '/'
    return morse_code

@app.route('/play_sound', method='POST')

def play_sound():
    morse_code = request.forms.get('morse_code', '').strip()
    
    pygame.mixer.init()
    pygame.mixer.music.load('beep.wav')
    pygame.mixer.music.set_volume(0.1)

    for char in morse_code:
        if char == '.':
            pygame.mixer.music.play()
            pygame.time.delay(300)
        elif char == '-':
            pygame.mixer.music.play()
            pygame.time.delay(900) 
        elif char == ' ':
            pygame.time.delay(300)  
        elif char == '/':
            pygame.time.delay(900)  

    pygame.mixer.quit()
    
    return template('index.html', morse_code=morse_code, text='', button_style='width: 150px; height: 60px;')

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
