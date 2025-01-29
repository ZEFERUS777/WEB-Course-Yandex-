def human_read_format(size):
    units = ['Б', 'КБ', 'МБ', 'ГБ']
    index = 0

    while size >= 1024 and index < 3:
        size /= 1024
        index += 1

    size = round(size)

    if size > 1024 and index < 3:
        size /= 1024
        index += 1
        size = round(size)

    return f"{int(size)}{units[index]}"
