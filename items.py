# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeteorologicalItem(scrapy.Item):
    # 数据时次
    time = scrapy.Field()
    # 气象站符号
    weather_station_symbol = scrapy.Field()
    # 气象站名称
    weather_station_name = scrapy.Field()
    # 经度
    longitude = scrapy.Field()
    # 纬度
    latitude = scrapy.Field()
    # 瞬时风速
    instantaneous_wind_speed = scrapy.Field()
    # 瞬时风向
    instantaneous_wind_direction = scrapy.Field()
    # 两分钟平均风速
    average_wind_speed_in_two_minutes = scrapy.Field()
    # 两分钟平均风向
    average_wind_direction_in_two_minutes = scrapy.Field()
    # 十分钟平均风速
    average_wind_speed_in_ten_minutes = scrapy.Field()
    # 十分钟平均风向
    average_wind_direction_in_ten_minutes = scrapy.Field()
    # 温度
    temperature = scrapy.Field()
    # 相对湿度
    relative_humidity = scrapy.Field()
    # 气压
    pressure = scrapy.Field()
    # 小时降雨量
    hourly_rainfall = scrapy.Field()
    # 日降雨量
    daily_rainfall = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
