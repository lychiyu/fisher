def is_isbn_or_key(q):
    """
    根据q来判断是isbn还是普通搜索关键字
    :param q:
    :return:
    """
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():  # isbn13
        isbn_or_key = 'isbn'
    temp_q = q.replace('-', '')
    if '-' in q and len(temp_q) == 10 and temp_q.isdigit():  # isbn10
        isbn_or_key = 'isbn'
    return isbn_or_key
