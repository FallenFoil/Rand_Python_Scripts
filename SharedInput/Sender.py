from pynput.keyboard import Key, KeyCode, Controller as KeyboardController, Listener
import socket
import time

keyboard = KeyboardController()
sending = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.130', 25566))


def get_key(key):
    if key == KeyCode.from_char("q"):
        return 'q'
    elif key == KeyCode.from_char("w"):
        return 'w'
    elif key == KeyCode.from_char("e"):
        return 'e'
    elif key == KeyCode.from_char("r"):
        return 'r'
    elif key == KeyCode.from_char("t"):
        return 't'
    elif key == KeyCode.from_char("y"):
        return 'y'
    elif key == KeyCode.from_char("u"):
        return 'u'
    elif key == KeyCode.from_char("i"):
        return 'i'
    elif key == KeyCode.from_char("o"):
        return 'o'
    elif key == KeyCode.from_char("p"):
        return 'p'
    elif key == KeyCode.from_char("a"):
        return 'a'
    elif key == KeyCode.from_char("s"):
        return 's'
    elif key == KeyCode.from_char("d"):
        return 'd'
    elif key == KeyCode.from_char("f"):
        return 'f'
    elif key == KeyCode.from_char("g"):
        return 'g'
    elif key == KeyCode.from_char("h"):
        return 'h'
    elif key == KeyCode.from_char("j"):
        return 'j'
    elif key == KeyCode.from_char("k"):
        return 'k'
    elif key == KeyCode.from_char("l"):
        return 'l'
    elif key == KeyCode.from_char("ç"):
        return 'ç'
    elif key == KeyCode.from_char("z"):
        return 'z'
    elif key == KeyCode.from_char("x"):
        return 'x'
    elif key == KeyCode.from_char("c"):
        return 'c'
    elif key == KeyCode.from_char("v"):
        return 'v'
    elif key == KeyCode.from_char("b"):
        return 'b'
    elif key == KeyCode.from_char("n"):
        return 'n'
    elif key == KeyCode.from_char("m"):
        return 'm'
    elif key == KeyCode.from_char(","):
        return ','
    elif key == KeyCode.from_char(";"):
        return ';'
    elif key == KeyCode.from_char("."):
        return '.'
    elif key == KeyCode.from_char(":"):
        return ':'
    elif key == KeyCode.from_char("-"):
        return '-'
    elif key == KeyCode.from_char("_"):
        return '_'
    elif key == KeyCode.from_char("~"):
        return '~'
    elif key == KeyCode.from_char("^"):
        return '^'
    elif key == KeyCode.from_char("+"):
        return '+'
    elif key == KeyCode.from_char("*"):
        return '*'
    elif key == KeyCode.from_char("´"):
        return '´'
    elif key == KeyCode.from_char("`"):
        return '`'
    elif key == KeyCode.from_char("º"):
        return 'º'
    elif key == KeyCode.from_char("ª"):
        return 'ª'
    elif key == KeyCode.from_char("?"):
        return '?'
    elif key == KeyCode.from_char("'"):
        return '\''
    elif key == KeyCode.from_char("<"):
        return '<'
    elif key == KeyCode.from_char(">"):
        return '>'
    elif key == KeyCode.from_char("\\"):
        return '\\'
    elif key == KeyCode.from_char("|"):
        return '|'
    elif key == KeyCode.from_char("("):
        return '('
    elif key == KeyCode.from_char(")"):
        return ')'
    elif key == KeyCode.from_char("&"):
        return '&'
    elif key == KeyCode.from_char("%"):
        return '%'
    elif key == KeyCode.from_char("#"):
        return '#'
    elif key == KeyCode.from_char("\""):
        return '\"'
    elif key == KeyCode.from_char("!"):
        return '!'
    elif key == KeyCode.from_char("="):
        return '='
    elif key == KeyCode.from_char("1"):
        return '1'
    elif key == KeyCode.from_char("2"):
        return '2'
    elif key == KeyCode.from_char("3"):
        return '3'
    elif key == KeyCode.from_char("4"):
        return '4'
    elif key == KeyCode.from_char("5"):
        return '5'
    elif key == KeyCode.from_char("6"):
        return '6'
    elif key == KeyCode.from_char("7"):
        return '7'
    elif key == KeyCode.from_char("8"):
        return '8'
    elif key == KeyCode.from_char("9"):
        return '9'
    elif key == KeyCode.from_char("0"):
        return '0'
    elif key == Key.backspace:
        return "backspace"
    elif key == Key.space:
        return "space"
    elif key == Key.up:
        return "up"
    elif key == Key.down:
        return "down"
    elif key == Key.left:
        return "left"
    elif key == Key.right:
        return "right"
    elif key == Key.enter:
        return "enter"
    elif key == Key.home:
        return "home"
    elif key == Key.end:
        return "end"
    else:
        return "none"


def on_press(key):
    global sending
    if sending:
        time.sleep(0.2)
        s.send(get_key(key).encode())

    print(f"{key}")


def on_release(key):
    global sending
    if key == Key.esc:
        sending = False
        print("stop sending")
    elif key == Key.print_screen:
        print("start sending")
        sending = True

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()