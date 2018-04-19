import urllib.request
import pandas as pd
import json
import datetime
import time
from itertools import count

def GetText_Json(url):
    text_data = urllib.request.urlopen(url).read().decode('utf-8')

    return text_data



def DominoAddress(result):
    url = 'https://web.dominos.co.kr/branch/listAjax'
    text_data = GetText_Json(url)
    domino_stores = json.loads(text_data)

    for domino_store in domino_stores['resultData']['branchList']:
        result.append([str(domino_store['branch_name']),str(domino_store['road_addr_ba']),str(domino_store['addr_ba'])])

        print(result)

    return




def main():
    result = []
    print('DOMINO ADDRESS CRAWLING START')
    DominoAddress(result)
    domino_table = pd.DataFrame(result, columns=('store','sidogungu','store_address'))
    domino_table.to_csv("domino.csv",encoding="cp949",mode='w',index=True)
    print('DOMINO ADDRESS CRAWLING FINISH')
if __name__ == '__main__':
    main()
