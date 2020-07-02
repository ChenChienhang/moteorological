import scrapy
import json
from scrapy import Request
from scrapy.http import FormRequest
from meteorological.items import MeteorologicalItem

class MoteorologicalSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["catalogDetail.htm"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'content-type':'x-www-form-urlencoded'
    }
    url = 'https://data.gz.gov.cn/dataanaly/data/CatalogDetail.do?method=GetDataListForGrid'

    def start_requests(self):
        pages = 3594
        for page in range(1,5):
            params = {
                "cata_id": "49390",
                "conf_type": "2",
                "where": "[]",
                "_search": "false",
                "nd": "1593690565177",
                "rows": "10000",
                "page": str(page),
                "sidx": "",
                "sord": "asc"
            }
            try:
                yield scrapy.FormRequest(self.url,formdata=params, callback=self.parse, dont_filter=True)
            except:
                print("FormRequest报错")
                pass

    def parse(self, response):
        print("*" * 50)
        datas = json.loads(response.body)
        item = MeteorologicalItem()
        data = datas.get('rows')
        try:
            for row in data:
                if row['SFZPJFX']:
                    item['average_wind_direction_in_ten_minutes'] = row['SFZPJFX']
                if row['LFZPJFX']:
                    item['average_wind_direction_in_two_minutes'] = row['LFZPJFX']
                if row['SFZPJFS']:
                    item['average_wind_speed_in_ten_minutes'] = row['SFZPJFS']
                if row['LFZPJFS']:
                    item['average_wind_speed_in_two_minutes'] = row['LFZPJFS']
                if row['RYL']:
                    item['daily_rainfall'] = row['RYL']
                if row['XSYL']:
                    item['hourly_rainfall'] = row['XSYL']
                if row['SSFX']:
                    item['instantaneous_wind_direction'] = row['SSFX']
                if row['SSFS']:
                    item['instantaneous_wind_speed'] = row['SSFS']
                if row['ZDSZJD']:
                    item['longitude'] = row['ZDSZJD']
                if row['ZDSZWD']:
                    item['latitude'] = row['ZDSZWD']
                if row['QY']:
                    item['pressure'] = row['QY']
                if row['XDSD']:
                    item['relative_humidity'] = row['XDSD']
                if row['WD']:
                    item['temperature'] = row['WD']
                if row['SJSC']:
                    item['time'] = row['SJSC']
                if row['UPDATE_TIME']:
                    item['update_time'] = row['UPDATE_TIME']
                if row['XMNDTZJD']:
                    item['weather_station_name'] = row['XMNDTZJD']
                if row['QXZZH']:
                    item['weather_station_symbol'] = row['QXZZH']
                yield item
        except:
            print('response 为空')
            pass
        
