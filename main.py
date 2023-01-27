import time
import pyautogui

morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}

def translate(word):
    code = ""
    word = word.lower()
    for letter in word:
        code += morze.get(letter)
    return code

def dot():
    pyautogui.press('capslock')
    time.sleep(0.7)
    pyautogui.press('capslock')

def dash():
    pyautogui.press('capslock')
    time.sleep(2)
    pyautogui.press('capslock')

def get_light_code(word):
    code = translate(word)
    for i in code:
        if i == "•":
            dot()
        elif i == "—":
            dash()

get_light_code(input("Введите слово для кодирования: "))