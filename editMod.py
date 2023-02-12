
def check_item(item, allowed_symbols):
    # A10a1
    # if item.isdigit() || item.isalpha():
    ok = True
    for letter in item:
        if (letter in allowed_symbols) or\
                (allowed_symbols[0] == "num" and letter.isdigit()) or\
                (allowed_symbols[0] == "alpha" and letter.isalpha()) or\
                (allowed_symbols[0] == "alnum" and letter.isalnum()) or\
                (allowed_symbols[0] == "all"):
            ok = True
        else:
            ok = False
            break
    return ok


def edit_item(prompt, allowed_symbols):
    while True:
        item = input(prompt)
        if item == "q":
            break
        if check_item(item, allowed_symbols):
            break
    return item