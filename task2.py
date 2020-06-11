def string_alternate(text):
    return text[::2]

if __name__ == "__main__":
    text = input('enter the string:')
    output = string_alternate(text)
    print(output)