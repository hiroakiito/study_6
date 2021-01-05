import requests
import urllib
import numpy as np
import pandas as pd
import datetime

def get_api(url):
    param={"format":"json",
           "applicationId":"1019079537947262807",
           "age":"20",
           "sex":"1"}
    result = requests.get(url,param)
    return result.json()

def make_csv(responses):
    # リストに使用する項目のみ抽出
    item_key = ['rank', 'itemName', 'catchcopy', 'itemCode', 'itemPrice', 'itemCaption', 'itemUrl', 'imageFlag', 'availability', 'creditCardFlag', 'shipOverseasFlag', 'shipOverseasArea', 'asurakuFlag', 'asurakuArea', 'shopName', 'shopCode', 'shopUrl']
    item_list = []
    for i in range(0, len(responses['Items'])):
        tmp_item = {}
        item = responses['Items'][i]['Item']
        for key, value in item.items():
            if key in item_key:
                tmp_item[key] = value
                print("{}:{}".format(key, value))
        item_list.append(tmp_item)
    # CSV出力
    items_df = pd.DataFrame(item_list)
    items_df = items_df.reindex(columns=['rank', 'itemName', 'catchcopy', 'itemCode', 'itemPrice', 'itemCaption', 'itemUrl', 'imageFlag', 'availability', 'creditCardFlag', 'shipOverseasFlag', 'shipOverseasArea', 'asurakuFlag', 'asurakuArea', 'shopName', 'shopCode', 'shopUrl'])
    items_df.columns = ['ランキング順位', '商品名', 'キャッチコピー', '商品コード', '商品価格', '商品説明文', '商品URL', '商品画像有無', '販売可否', 'クレジットカード利用可否', '海外配送可否', '海外配送対象地域', 'あす楽可否', 'あす楽配送対象地域', '店舗名', '店舗コード', '店舗URL']
    items_df.index = np.arange(1, len(items_df)+1)
    now = datetime.datetime.now().strftime('%Y%m%d')
    items_df.to_csv("./rakuten_ranking_{}.csv".format(now), encoding='utf_8_sig')

def main():
    age= "20"
    sex = "1"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    responses = get_api(url)
    make_csv(responses)

main()


	
    
    
    
    
    	
        
        
        
        
        
        
        
        	
            
            	

