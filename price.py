import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    sort = "standard"
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={}&sort={}&applicationId=1019079537947262807".format(
        keyword, sort)
    responses = get_api(url)
    for response in responses['Products']:
        print('商品名：{}'.format(response['Product']['productName']))
        print('最安価格：{}円'.format(response['Product']['minPrice']))
        print('最高価格：{}円'.format(response['Product']['maxPrice']))

main()
