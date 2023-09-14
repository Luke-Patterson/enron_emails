def parse_email(text):
    lines = text.split('\n')
    # find when meta data stops
    blank_lines = [i for i, item in enumerate(lines) if item == '']
    assert len(blank_lines) > 0, 'No blank line presumed to delimit metadata found'
    first_blank_line = blank_lines[0]
    metadata = lines[:first_blank_line]
    metadata_dict = {}
    for m in metadata:
        # some metadata line breaks are still within the same field, if there is no colon, then add it to the previous field
        if ':' in m:
            key = m.split(':')[0]
            value = m.split(':')[1]
            metadata_dict[key] = value
        else:
            metadata_dict[prev_key] = metadata_dict[prev_key] + ' ' + m
        prev_key = key
    metadata_dict['text'] = ' '.join(lines[first_blank_line+1:])
    return metadata_dict


