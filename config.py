headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Cache-Control": "no-cache",
    "Origin": "https://www.volkshochschule.de",
    "Connection": "keep-alive",
    "Referer": "https://www.volkshochschule.de/verbandswelt/volkshochschulen/alle-standorte.php?form=search-1.form&sp%3Afulltext%5B%5D=&sp%3Acategories%5B7679%5D%5B%5D=-&sp%3Acategories%5B7679%5D%5B%5D=__last__&action=submit",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
}

url = "https://www.volkshochschule.de/WEB-IES/sitekit-module/php/SP/SiteKit/Rpc/Server/Port.php"

json_data = {
    "action": "SP\\SiteKit\\Rpc\\Map\\Service",
    "method": "findByCategory",
    "type": "rpc",
    "tid": 1,
    "version": "1.0",
    "data": [
        {
            "searchId": "siteSearch",
            "searchUrl": "/suche.php",
            "categories": [
                "10860",
            ],
        },
    ],
}
