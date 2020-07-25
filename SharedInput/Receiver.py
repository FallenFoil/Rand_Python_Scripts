from pynput.keyboard import Key, Controller as KeyboardController
import socket

keyboard = KeyboardController()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.130', 25566))

def get_key(key):
    if key == "q":
        return 'q'
    elif key == "w":
        return 'w'
    elif key == "e":
        return 'e'
    elif key == "r":
        return 'r'
    elif key == "t":
        return 't'
    elif key == "y":
        return 'y'
    elif key == "u":
        return 'u'
    elif key == "i":
        return 'i'
    elif key == "o":
        return 'o'
    elif key == "p":
        return 'p'
    elif key == "a":
        return 'a'
    elif key == "s":
        return 's'
    elif key == "d":
        return 'd'
    elif key == "f":
        return 'f'
    elif key == "g":
        return 'g'
    elif key == "h":
        return 'h'
    elif key == "j":
        return 'j'
    elif key == "k":
        return 'k'
    elif key == "l":
        return 'l'
    elif key == "ç":
        return 'ç'
    elif key == "z":
        return 'z'
    elif key == "x":
        return 'x'
    elif key == "c":
        return 'c'
    elif key == "v":
        return 'v'
    elif key == "b":
        return 'b'
    elif key == "n":
        return 'n'
    elif key == "m":
        return 'm'
    elif key == ",":
        return ','
    elif key == ";":
        return ';'
    elif key == ".":
        return '.'
    elif key == ":":
        return ':'
    elif key == "-":
        return '-'
    elif key == "_":
        return '_'
    elif key == "~":
        return '~'
    elif key == "^":
        return '^'
    elif key == "+":
        return '+'
    elif key == "*":
        return '*'
    elif key == "´":
        return '´'
    elif key == "`":
        return '`'
    elif key == "º":
        return 'º'
    elif key == "ª":
        return 'ª'
    elif key == "?":
        return '?'
    elif key == "'":
        return '\''
    elif key == "<":
        return '<'
    elif key == ">":
        return '>'
    elif key == "\\":
        return '\\'
    elif key == "|":
        return '|'
    elif key == "(":
        return '('
    elif key == ")":
        return ')'
    elif key == "&":
        return '&'
    elif key == "%":
        return '%'
    elif key == "#":
        return '#'
    elif key == "\"":
        return '\"'
    elif key == "!":
        return '!'
    elif key == "=":
        return '='
    elif key == "1":
        return '1'
    elif key == "2":
        return '2'
    elif key == "3":
        return '3'
    elif key == "4":
        return '4'
    elif key == "5":
        return '5'
    elif key == "6":
        return '6'
    elif key == "7":
        return '7'
    elif key == "8":
        return '8'
    elif key == "9":
        return '9'
    elif key == "0":
        return '0'
    elif key == "backspace":
        return Key.backspace
    elif key == "space":
        return Key.space
    elif key == "up":
        return Key.up
    elif key == "down":
        return Key.down
    elif key == "left":
        return Key.left
    elif key == "right":
        return Key.right
    elif key == "enter":
        return Key.enter
    elif key == "home":
        return Key.home
    elif key == "end":
        return Key.end


while True:
    key = s.recv(9).decode("ascii")
    print(key)
    if key != "none":
        keyboard.press(get_key(key))
        keyboard.release(get_key(key))