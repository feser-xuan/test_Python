# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/11/12 14:12
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm

# import requests
# import time
# import aiohttp
# import asyncio
# URL = "https://morvanzhou.github.io/"
#
# def normal():
#     for i in range(2):
#         r = requests.get(URL)
#         url = r.url
#         print(url)
#
# t1 = time.time()
# normal()
# print("Normal total time:",time.time()-t1)



# async def job(session):
#     response = await session.get(URL)
#     return str(response.url)
#
# async def main(loop):
#     async with aiohttp.ClientSession() as session:
#         tasks = [loop.create_task(job(session)) for _ in range(2)]
#         finished,unfinished = await asyncio.wait(tasks)
#         all_results = [r.result() for r in finished]
#         print(all_results)
#
# t1 = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
#
# print("Async total time: ",time.time()-t1)


import scrapy

class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = ["https://morvanzhou.github.io/",]

    def parse(self,response):
        yield{
            'title':response.css('h1::text').extract_first(default='Missing').strip().replace('"',""),
            'url':response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url,callback = self.parse)
