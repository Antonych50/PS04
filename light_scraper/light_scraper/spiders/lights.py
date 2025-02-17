
import scrapy


class LightSpider(scrapy.Spider):
    name = 'light_spider'
    page = 0
    start_urls = ['https://svetmarket23.ru/shop']

    def parse(self, response):

        #Находим все товары на странице
        #products = response.css('div.desc')

        for product in response.css('div.desc'):
            item = {
                'name': product.css('h4 a::text').get(),
                'price': product.css('span.price bdi::text').get().strip(),
                'link': product.css('a::attr(href)').get()
            }
            #print (f'{item["name"]} - {item["price"]} - {item["link"]}')
            yield item

        # Переход к следующей странице, если есть
        next_page = response.css('span.page-numbers.current + a.page-numbers::attr(href)').get()
        if next_page=='https://svetmarket23.ru/shoppage/1/':
            pass
        elif next_page:
            yield response.follow(next_page, callback=self.parse)