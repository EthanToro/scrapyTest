import scrapy
from pip._vendor.html5lib.constants import EOF


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://ethantoro.dev']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)


EOF
