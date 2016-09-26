def translate_line_to_dict(line):
    post_data = {}
    for pos in range(0, len(line.headings)):
        if len(line.cells[pos]) > 0:
            post_data[line.headings[pos]] = line.cells[pos]

    return post_data
