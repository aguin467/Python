import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://downloads.pwnedpasswords.com/passwords/pwned-passwords-sha1-ordered-by-count-v4.7z',
            'https://downloads.pwnedpasswords.com/passwords/pwned-passwords-sha1-ordered-by-count-v4.7z',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




