import scrapy
from scrapy.http import FormRequest
from time import sleep

class QuotesSpider(scrapy.Spider):
    url='https://schools.kundelik.kz/birthdays.aspx?school=1000001828992&group=all&page={0}'
    name='q'
    x=0
    login='https://login.kundelik.kz/login/'
    def start_requests(self):
        yield scrapy.Request(self.login, callback=self.log_in,
                            errback=self.errhand,
                            dont_filter=True)

    def log_in(self,response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        self.log('logging')
        return FormRequest.from_response(response, formdata={'csrf_token': token,
                                                             'password': '12345678910111Mk',
                                                             'login': 'kembaevmukhamedzhan'},
                                         callback=self.pagenator)
    def pagenator(self,response):
        for x in range(1,3):
            self.log(x)
            sleep(5)
            yield scrapy.Request(self.url.format(x), callback=self.parse,
                            errback=self.err0,
                            dont_filter=True)

    def parse(self, response):
        self.log('--scrape--')
        r=response.xpath("//tr/td[2]/a/@href").getall()
        self.log(r)
        self.log('Finalmente!')

    def parse_person(self,response):


    def errhand(self):
        self.log("---Error1---")
    def err0(self):
        self.log("---Error2---")

