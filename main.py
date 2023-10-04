import requests as r

from config import url, headers, json_data

from rich import print

from selectolax.parser import HTMLParser


def get_data_json():
    response = r.post(
        url,
        headers=headers,
        json=json_data,
    )
    return response.json()["result"]["data"]


def get_urls(data: list):
    return [f'https://www.volkshochschule.de{item["url"]}' for item in data]


def main():
    data = get_data_json()
    print(get_urls(data))
    print(len(data))


if __name__ == "__main__":
    main()
