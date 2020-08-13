import scrapy
from scrapy.http import Request
import os,time
import datetime

InsurerName = "IciciLombard"
folderyear="2019-20"
# Project Requirement keep next year financial year with same formate
year = "2019-2020"
QuarterQ1 = "Quarter-1"
QuarterQ2 = "Quarter-2"
QuarterQ3 = "Quarter-3"
QuarterQ4 = "Quarter-4"

class QuoteSpider(scrapy.Spider):
    name = 'icici'
    start_urls = [
        'https://www.icicilombard.com/about-us/public-disclosure'
    ]
    def parse(self,response):
        for i in range(1,5):
            id= "//*[@id='"+year+"']/div/div["+str(i)+"]/h5/text()"
            text = response.xpath(id).extract()
            Q1value = ['Q1 '+ year[5:9]]
            Q2value = ['H1 ' + year[5:9]]
            Q3value = ['Q3 ' + year[5:9]]
            Q4value = ['FY ' + year[5:9]]
            if text == Q1value:
                for i in range(19):
                    id_val= "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_0_lvfiles_0_viewlk_"+str(i)+"']"
                    link= response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l1= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l1)
                    yield Request(absolute_url_l1, callback=self.save_pdf, meta={'quarter': QuarterQ1})
                for i in range(41):
                    id_val = "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_0_lvfiles_1_viewlk_"+str(i)+"']"
                    link = response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l2= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l2)
                    yield Request(absolute_url_l2, callback=self.save_pdf, meta={'quarter': QuarterQ1})
            elif text ==  Q2value:
                for i in range(19):
                    id_val= "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_1_lvfiles_0_viewlk_"+str(i)+"']"
                    link= response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l1= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l1)
                    yield Request(absolute_url_l1, callback=self.save_pdf, meta={'quarter': QuarterQ2})
                for i in range(41):
                    id_val = "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_1_lvfiles_1_viewlk_"+str(i)+"']"
                    link = response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l2= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l2)
                    yield Request(absolute_url_l2, callback=self.save_pdf, meta={'quarter': QuarterQ2})
            elif text == Q3value:
                for i in range(19):
                    id_val= "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_2_lvfiles_0_viewlk_"+str(i)+"']"
                    link= response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l1= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l1)
                    yield Request(absolute_url_l1, callback=self.save_pdf, meta={'quarter': QuarterQ3})
                for i in range(41):
                    id_val = "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_2_lvfiles_1_viewlk_"+str(i)+"']"
                    link = response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l2= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l2)
                    yield Request(absolute_url_l2, callback=self.save_pdf, meta={'quarter': QuarterQ3})
            elif text ==Q4value:
                for i in range(19):
                    id_val= "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_3_lvfiles_0_viewlk_"+str(i)+"']"
                    link= response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l1= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l1)
                    yield Request(absolute_url_l1, callback=self.save_pdf, meta={'quarter': QuarterQ4})
                for i in range(41):
                    id_val = "// *[ @ id = 'innerPg_C004_lvQuarter_lvinnerType_3_lvfiles_1_viewlk_"+str(i)+"']"
                    link = response.xpath(id_val)
                    relative_url =link.xpath(".//@href").extract_first()
                    absolute_url_l2= response.urljoin(relative_url)
                    self.logger.info(absolute_url_l2)
                    yield Request(absolute_url_l2, callback=self.save_pdf, meta={'quarter': QuarterQ4})

    def store_exceptData(self,methodName, exception):
        BasePath = os.getcwd()
        todaydate = datetime.date.today().strftime('%d%m%Y')
        data = os.path.isdir(BasePath + '\\' + 'Module_Exceptions')
        if data is False:
            os.mkdir(BasePath + '\\' + 'Module_Exceptions')
        path = BasePath + '\\' + 'Module_Exceptions\\' + 'Keyword-Exp_' + todaydate + '.txt'
        timestr = time.strftime("%Y%m%d-%H%M%S")
        txt = open(path, 'a')
        txt.write(str(timestr) + '[Method Name]:' + methodName + ' [Error Discription]: ' + str(exception) + '\n\n')
        txt.close()

    def FilesFolderPath(self,BankName, year):
        try:
            BasePath = os.getcwd()
            pdfdata = os.path.isdir(BasePath + '\\' + BankName)
            if pdfdata is False:
                os.mkdir(BasePath + '\\' + BankName)
            yearfolder = os.path.isdir(BasePath + '\\' + BankName + '\\' + year)
            if yearfolder is False:
                os.mkdir(BasePath + '\\' + BankName + '\\' + year)
            PdfPath = BasePath + '\\' + BankName + '\\' + year
            path_dict = {'PdfPath': PdfPath}
            return path_dict
        except Exception as e:
            QuoteSpider.store_exceptData(self,"FilesFolderPath", e)

    def save_pdf(self,response):
        try:
            Quarter = response.meta.get('quarter')
            urlpdfpath = response.url.split('/')[-1]
            filename=urlpdfpath.split('?')[0]
            val = "nl" in filename
            if val==True:
                self.logger.info('Saving PDF %s', filename)
                folderPath = QuoteSpider.FilesFolderPath(self,InsurerName, folderyear)
                InsureFolderpath = folderPath['PdfPath']
                pdfpath = InsureFolderpath + '\\' + Quarter
                if not os.path.exists(pdfpath):
                    os.makedirs(pdfpath)
                path = pdfpath + '\\' + filename
                with open(path, 'wb') as f:
                    f.write(response.body)
                    f.close()
                yield Quarter
            else:
                pass
        except Exception as e:
            QuoteSpider.store_exceptData(self,"DownloadPdfFile", e)