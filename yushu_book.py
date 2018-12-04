from http import Http


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        # 根据isbn来查询书籍
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        # 关键字来查询书籍
        url = cls.keyword_url.format(keyword, count, start)
        result = Http.get(url)
        return result
