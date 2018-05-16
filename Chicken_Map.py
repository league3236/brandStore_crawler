import folium
import json
import urllib.request
import datetime
import pandas as pd
import webbrowser

#code1
def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id","Ch0vdY0HM6SPOidkt02i")
    req.add_header("X-Naver-Client-Secret","ANmaZHqA8m")
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None

#code2
def getGeoData(address):

    base = "https://openapi.naver.com/v1/map/geocode"
    node = ""
    parameters = "?query=%s" % urllib.parse.quote(address)
    url = base + node + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    #code3
    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    #code4
    filename = 'pericana_modify.csv'
    df = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                print(geoData['result']['items'][0]['point']['x'])
                print(geoData['result']['items'][0]['point']['y'])
                folium.Marker([geoData['result']['items'][0]['point']['y'],geoData['result']['items'][0]['point']['x']], popup=row['store'], icon=folium.Icon(color='blue')).add_to(map)

    filename2 = 'goobne_modify.csv'
    df2 = pd.read_csv(filename2, encoding='CP949', index_col=0, header=0)
    geoData2 = []
    for index, row in df2.iterrows():
        if row['sido'] == '서울특별시':
            geoData2 = getGeoData(row['store_address'])
            if geoData2 != None:
                print(geoData2['result']['items'][0]['point']['x'])
                print(geoData2['result']['items'][0]['point']['y'])
                folium.Marker([geoData2['result']['items'][0]['point']['y'],geoData2['result']['items'][0]['point']['x']], popup=row['store'], icon=folium.Icon(color='red')).add_to(map)


    #code5
    svFilename = 'Chicken_Map-1.html'
    map.save(svFilename)
    webbrowser.open(svFilename)


if __name__ == '__main__':
    main()
