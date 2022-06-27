def right_trim(text: str):
    # deletes tabs and spaces at the end of each text line
    result = ""
    for index in range(len(text)):
        if not should_be_skipped(text, index):
            result += text[index]
    return result


def should_be_skipped(text, index):
    if text[index] in ['\t', ' ']:
        if is_char_at_the_end_of_line(text, index):
            return True
        return should_be_skipped(text, index + 1)
    return False


def is_char_at_the_end_of_line(text, index):
    return (is_last_character(text, index) or
            is_followed_by_unix_end_of_line(text, index) or
            is_followed_by_windows_end_of_line(text, index))


def is_last_character(text, index):
    return index == len(text) - 1


def is_followed_by_unix_end_of_line(text, index):
    return text[index + 1] == '\n'


def is_followed_by_windows_end_of_line(text, index):
    return text[index + 1] == '\r' and text[index + 2] == '\n'
