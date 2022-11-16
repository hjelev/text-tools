import base64
import translate


def remove_empty_lines(text):
    lines = []
    for line in text.splitlines():
        if line.rstrip():
            lines.append(line)

    return '\n'.join(lines)


def remove_duplicate_lines(text):
    lines = text.splitlines()
    # Remove duplicates
    lines = list(set(lines))

    return '\n'.join(lines)


def sort(text): 
    lines = text.splitlines()
    lines.sort()

    return '\n'.join(lines)


def sort_reversed(text): 
    lines = text.splitlines()
    lines.sort(reverse=True) 

    return '\n'.join(lines)


def base64_encode(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode("utf-8")


def base64_decode(text):
    decoded = base64.b64decode(text.encode())
    return decoded.decode("utf-8")


def strip_text(text):
    lines = text.splitlines()
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    return '\n'.join(stripped_lines)


def cyr_to_latin(text):
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
    tr = {ord(a):ord(b) for a, b in zip(*symbols)}

    return(text.translate(tr)) 


def latin_to_cyr(text):
    symbols = (u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA",
               u"абвгдеёжзийклмнопрстуфхцчшщъыьэюаАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    tr = {ord(a):ord(b) for a, b in zip(*symbols)}

    return(text.translate(tr)) 


print(latin_to_cyr('i a'))