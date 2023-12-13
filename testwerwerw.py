import scrapy

class OpGGSpider(scrapy.Spider):
    name = 'opgg_spider'
    start_urls = ['https://www.op.gg/leaderboards']

    def parse(self, response):
        for rank in response.css('.ranking-table__cell--rank'):
            position = rank.css('::text').get()
            summoner_name = rank.xpath('./following-sibling::td/a/text()').get()
            if position and summoner_name:
                yield {
                    'Position': position.strip(),
                    'Summoner Name': summoner_name.strip()
                }

            # Stop scraping after rank 3
            if position == '3':
                break
