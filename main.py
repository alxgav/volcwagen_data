import requests as r

from config import url, headers, json_data, logger

from rich import print

from selectolax.parser import HTMLParser

from models import Item
import pandas as pd


def get_data_json():
    response = r.post(
        url,
        headers=headers,
        json=json_data,
    )
    return response.json()["result"]["data"]


def get_urls(data: list):
    return [f'https://www.volkshochschule.de{item["url"]}' for item in data]


def get_content(resp):
    return HTMLParser(resp.text)


def load_data(url) -> HTMLParser:
    resp = r.get(url, headers=headers)
    return get_content(resp)


def parser(data: list):
    data_volk = []
    id = 1
    for url in data:
        print(url, id)
        html = load_data(url)
        # contact_text = html.css_first("div.SP-Contact__locality__text").text()
        title = html.css_first(
            ".SP-Contact__locality__text > p:nth-child(1) > strong:nth-child(1)"
        ).text(strip=True)
        try:
            surname = html.css_first(
                ".SP-Contact__locality__text > p:nth-child(2) > strong:nth-child(1)"
            ).text(strip=True)
        except:
            surname = ""
        address = html.css_first(".SP-Contact__locality__text > p:nth-child(3)").text(
            strip=True
        )
        if len(surname) > 0:
            address2 = (
                html.css_first(".SP-Contact__locality__text > p:nth-child(2)")
                .text(strip=True)
                .split(surname)[1]
            )
        telefon = html.css_first(
            "ul.SP-Contact__locality__links > li:nth-child(1) > a:nth-child(1) > span:nth-child(3) > span:nth-child(1)"
        ).text()
        try:
            email = (
                html.css_first(
                    "li.SP-Contact__link--fullWidth:nth-child(2) > a:nth-child(1)"
                )
                .attributes["href"]
                .split(":")[1]
                .replace("%E2%9A%B9", "@")
                .replace("%E2%97%A6", ".")
            )
        except:
            email = ""
        try:
            web = html.css_first(
                "li.SP-Contact__link--fullWidth:nth-child(3) > a:nth-child(1)"
            ).attributes["href"]
        except:
            web = ""
        google_map = html.css_first(
            "div.SP-LinkList > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)"
        ).attributes["href"]
        open_street_map = html.css_first(
            "div.SP-LinkList > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)"
        ).attributes["href"]
        data = {
            "title": title,
            "surname": surname,
            "address": f"{address2} {address}",
            "telefon": telefon,
            "email": email,
            "url": web,
            "google_map": google_map,
            "open_street_map": open_street_map,
        }
        # print(Item(**data))

        data_volk.append(data)
        id += 1
        # if id == 5:
        #     break
    return data_volk


@logger.catch
def main():
    data = parser(get_urls(get_data_json()))
    df = pd.DataFrame(data=data)
    df.to_excel("t.xlsx", index=False)


if __name__ == "__main__":
    main()
