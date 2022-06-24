def right_trim(text: str):
    # deletes tabs and spaces at the end of every line
    if text[-1] == ' ':
        return text[:-1]
    return text
