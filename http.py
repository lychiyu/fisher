import requests


class Http:
    @staticmethod
    def get(url, json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if json else ''
        return res.json() if json else res.text

    @staticmethod
    def post(url):
        pass
