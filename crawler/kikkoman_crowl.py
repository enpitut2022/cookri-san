import re
import requests
import pandas as pd
from bs4  import BeautifulSoup
import time
import json
from logging import getLogger, config

class kikkoman:
    def __init__(self, url):
        self.url = url
        self.path = './recipe.json'
        self.data = {}
    def crowl(self):
        """キッコーマンのクローラ
        Returns
        --------
        data
            title: タイトル
            url: URL
            tags: 材料
            thmbnail_url : 写真URL
            time: 時間
            cal: カロリー
            solt: 塩分
        """
        # 初期設定
        logger.info(self.url)
        data = {}
        title, time, cal, solt = "", "", "", ""
        ing = []
        thumb = 'https://www.kikkoman.co.jp/homecook/search/recipe/img/'
        header={"User-Agent":'recipe-crowl-bot'}
        res = requests.get(self.url, header)
        if not res.status_code == requests.codes.ok:
            return 'Error'
        soup = BeautifulSoup(res.text, "html.parser")

        # h1タグにレシピ名
        elm = soup.find('h1')
        title = elm.span.contents[0]
        # labelタグに材料が格納される
        elms = soup.find_all('label')
        for i in elms:
            if i.span!=None:
                #print(i.span.contents[0])
                ing.append(i.span.contents[0])
            else:
                #print(i.a.contents[0])
                ing.append(i.a.contents[0])
        # サムネイルの取得
        thumb = thumb + self.url.split("/")[-2] + '.jpg'

        # その他情報の取得
        #pjax-area > div > div > div > div > div > div > div > div > div > main > div.main-column > div > div > div > div > div.elem-pic-block--recipe-overview > div > div > div > div > div.txt-container > div > div.txt-body > div.recipe-overview-list > div > div > div > div > dl:nth-child(1) > dd > b
        
        time = soup.select('#pjax-area > div > div > div > div > div > div > div > div > div > main > div.main-column > div > div > div > div > div.elem-pic-block--recipe-overview > div > div > div > div > div.txt-container > div > div.txt-body > div.recipe-overview-list > div > div > div > div > dl:nth-child(1) > dd > b')[0].contents[0]
        cal = soup.select('#pjax-area > div > div > div > div > div > div > div > div > div > main > div.main-column > div > div > div > div > div.elem-pic-block--recipe-overview > div > div > div > div > div.txt-container > div > div.txt-body > div.recipe-overview-list > div > div > div > div > dl:nth-child(2) > dd > b')[0].contents[0]
        solt = soup.select('#pjax-area > div > div > div > div > div > div > div > div > div > main > div.main-column > div > div > div > div > div.elem-pic-block--recipe-overview > div > div > div > div > div.txt-container > div > div.txt-body > div.recipe-overview-list > div > div > div > div > dl:nth-child(3) > dd > b')[0].contents[0]
        data["title"] = title; data['url'] = self.url;  data["tags"] = ing
        data["thumbnail_url"] = thumb; data['time'] = time; data['cal']=cal
        data['solt'] = solt
        self.data = data
        logger.debug(self.url+"\n===============succesed=====================")
        return self.data
    
    def to_json(self):
        """クロール⇒recipe.jsonに追記
        """
        data = self.crowl()
        path = self.path
        with open(path, 'r+', encoding='utf-8') as f:
            save_data = json.load(f)
        save_data.append(data)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
            
    
if __name__ == "__main__":
    with open('log_config.json', 'r') as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    logger = getLogger(__name__)

    urls = [
        "https://www.kikkoman.co.jp/homecook/series/chicken02.html",
        "https://www.kikkoman.co.jp/homecook/series/aburaage02.html",
        "https://www.kikkoman.co.jp/homecook/series/edamame02.html",
        "https://www.kikkoman.co.jp/homecook/series/cabbage02.html",
        "https://www.kikkoman.co.jp/homecook/series/kyuuri02.html",
        "https://www.kikkoman.co.jp/homecook/series/konnyaku02.html",
        "https://www.kikkoman.co.jp/homecook/series/jagaimo02.html",
        "https://www.kikkoman.co.jp/homecook/series/tamago02.html",
        "https://www.kikkoman.co.jp/homecook/series/tamanegi02.html",
        "https://www.kikkoman.co.jp/homecook/series/toufu02.html",
        "https://www.kikkoman.co.jp/homecook/series/ninjin02.html",
        "https://www.kikkoman.co.jp/homecook/series/piment02.html",
        "https://www.kikkoman.co.jp/homecook/series/pork02.html",
        "https://www.kikkoman.co.jp/homecook/series/pork_komagire02.html"
    ]
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        tmp = soup.find_all(href=re.compile("/search/recipe"))
        test_url = []
        for i in tmp:
            test_url.append("https://www.kikkoman.co.jp"+i.attrs['href'])
        test_url = set(test_url)
        for j in test_url:
            kikkoman(j).to_json()
            time.sleep(60)