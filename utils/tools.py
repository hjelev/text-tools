import base64

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

# base64.b64decode(a)