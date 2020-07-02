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
                    item['average_wind_direction_in_ten_minutes'] = row['SFZPJFX']
                    item['average_wind_direction_in_two_minutes'] = row['LFZPJFX']
                    item['average_wind_speed_in_ten_minutes'] = row['SFZPJFS']
                    item['average_wind_speed_in_two_minutes'] = row['LFZPJFS']
                    item['daily_rainfall'] = row['RYL']
                    item['hourly_rainfall'] = row['XSYL']
                    item['instantaneous_wind_direction'] = row['SSFX']
                    item['instantaneous_wind_speed'] = row['SSFS']
                    item['longitude'] = row['ZDSZJD']
                    item['latitude'] = row['ZDSZWD']
                    item['pressure'] = row['QY']
                    item['relative_humidity'] = row['XDSD']
                    item['temperature'] = row['WD']
                    item['time'] = row['SJSC']
                    item['update_time'] = row['UPDATE_TIME']
                    item['weather_station_name'] = row['XMNDTZJD']
                    item['weather_station_symbol'] = row['QXZZH']
                    yield item
        except:
            print('response 为空')
            pass
        
