def right_trim(text: str):
    # deletes tabs and spaces at the end of each text line
    chars_to_delete = [' ', '\t']

    if text[-1] in chars_to_delete:
        return text[:-1]

    elif text[-1] == '\n' and text[-2] in chars_to_delete:
        endline_sign = '\n'
        return text[:-2] + endline_sign

    return text
