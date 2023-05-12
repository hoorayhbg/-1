def center_align(text, width, fillchar=' '):
    fill_len = width - len(text)
    fill_half = fill_len // 2
    return fillchar * fill_half + text + fillchar * (fill_len - fill_half)