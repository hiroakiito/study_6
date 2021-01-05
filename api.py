import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    responses = get_api(url)
    for response in responses['Items']:
        print('商品名：{}'.format(response['Item']['itemName']))
        print('価格：{}円'.format(response['Item']['itemPrice']))

main()
