# volkswagen_data
volkswagen_de collect all data, locations, adress and email adresses from this site.

## Task
Hi. Please collect all data, locations, adress and email adresses from this site. Please export data in excel file.
# url
```bash
https://www.volkshochschule.de/verbandswelt/volkshochschulen/alle-standorte.php?form=search-1.form&sp%3Afulltext%5B%5D=&sp%3Acategories%5B7679%5D%5B%5D=-&sp%3Acategories%5B7679%5D%5B%5D=__last__&action=submit
```
# header
```bash
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Cache-Control': 'no-cache',
    'Origin': 'https://www.volkshochschule.de',
    'Connection': 'keep-alive',
    'Referer': 'https://www.volkshochschule.de/verbandswelt/volkshochschulen/alle-standorte.php?form=search-1.form&sp%3Afulltext%5B%5D=&sp%3Acategories%5B7679%5D%5B%5D=-&sp%3Acategories%5B7679%5D%5B%5D=__last__&action=submit',
    # 'Cookie': '_pk_id.6.2dcd=2481bcd8ec1e7bf5.1696438485.; _pk_ses.6.2dcd=1; mtm_consent=1696438485392; cookies-accepted=true',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
```
# response
```bash
response = requests.post(
    'https://www.volkshochschule.de/WEB-IES/sitekit-module/php/SP/SiteKit/Rpc/Server/Port.php',
    headers=headers,
)
```
## Libraries
```bash
pip install requests, pandas, selectolax, XlsxWriter, pydantic
```
