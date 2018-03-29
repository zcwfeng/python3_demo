# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy import Item
import json
import codecs
from scrapy.log import logger

class JsonWithEncodingTencentPipeline(object):

    def __init__(self):
        self.file = codecs.open('tencent.json', 'w', encoding='utf-8')

    # def item2dict(self,obj):
    #     return {'name': self.obj.name,
    #             'catalog': self..catalog,
    #             'workLocation': self..workLocation,
    #             'recruitNumber': self..recruitNumber,
    #             'detailLink': self..detailLink,
    #             'publishTime': self..publishTime}

    def process_item(self, item, spider):
        # dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        # allow_nan=True, cls=None, indent=None, separators=None,
        # default=None, sort_keys=False, **kw)


        # dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        # allow_nan=True, cls=None, indent=None, separators=None,
        # default=None, sort_keys=False, **kw)
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        logger.info(line + "==zcw==="*10)
        return item

    def spider_closed(self, spider):
        self.file.close()


