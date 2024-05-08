import requests

base_url = "http://127.0.0.1:8000/"


def path_test():
    url = base_url + "path/"

    payload = {"startX": "126.9246033",
               "startY": "33.45241976",
               "endX": "126.9041895",
               "endY": "33.4048969",
               "method": "bus"}

    res = requests.post(url=url, json=payload)

    return res


def main():
    res = path_test()
    print(res.content)


if __name__ == '__main__':
    main()
