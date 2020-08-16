import scrapy

from ..items import AmzscraperItem

class AmzSpider(scrapy.Spider):
    name = 'AmzScrape'
    start_urls= [
        'https://www.amazon.in/s?k=books&ref=nb_sb_noss'
        ]
    pageNumber = 2

    def parse(self,response):

        items = AmzscraperItem()

        title = response.css('.a-size-medium::text').extract()
        price = response.css('.sg-col-20-of-28 .a-spacing-top-small .a-price-whole::text').extract()
        author = response.css('.sg-col-12-of-28 .a-size-base.a-link-normal::text').extract()

        items['title'] = title
        items['price'] = price
        items['author'] = author

        yield items

        nextpage = 'https://www.amazon.in/s?k=books&page=' + str(AmzSpider.pageNumber) + '&qid=1597588536&ref=sr_pg_2'
        if (nextpage <= 4):
            yield response.follow(nextpage , callback = self.parse )
            AmzSpider.pageNumber += 1