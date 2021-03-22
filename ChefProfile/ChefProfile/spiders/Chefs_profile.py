import scrapy

class ChefsProfileSpider(scrapy.Spider):

    x = int(input("How many pages do you want to scrape?"))

    name = 'Chefs_profile'
    allowed_domains = ['meetachef.com']
    start_urls = ['https://meetachef.com/chefs/?page=%s'% page for page in range(1,x)]

    def parse(self, response):
        resp = response.xpath("//div[@class='HomePageComponents__BaseDiv-sc-13amrf6-6 jDqYnR']/a")
        for profile in resp:
            Name = profile.xpath(".//h2[@class='Styled__ListingHeadingH2-sc-1nslgi0-6 khsIQU']/text()").get()
            Profile_qoute = profile.xpath(".//span[@class='Styled__ListingSpan-sc-1nslgi0-8 dzTRrj']/text()").get()
            location = profile.xpath(".//span[@class='Styled__LocationNameSpan-sc-1nslgi0-10 cAUUyt']/text()").get()
            Experience = profile.xpath(".//span[@class='Styled__ListingDetailsExpSpan-sc-1nslgi0-17 hbSbBB']/text()").get()
            Payment = profile.xpath(".//span[@class='Styled__ListingDetailsPaySpan-sc-1nslgi0-20 loPvDQ']/text()").get()

            yield {
                "Profile_name" : profile.xpath(".//h2[@class='Styled__ListingHeadingH2-sc-1nslgi0-6 khsIQU']/text()").get(),
                "Profile_qoute": profile.xpath(".//span[@class='Styled__ListingSpan-sc-1nslgi0-8 dzTRrj']/text()").get(),
                "Location": profile.xpath(".//span[@class='Styled__LocationNameSpan-sc-1nslgi0-10 cAUUyt']/text()").get(),
                "Experience": profile.xpath(".//span[@class='Styled__ListingDetailsExpSpan-sc-1nslgi0-17 hbSbBB']/text()").get(),
                "Payment": profile.xpath(".//span[@class='Styled__ListingDetailsPaySpan-sc-1nslgi0-20 loPvDQ']/text()").get()
            }

