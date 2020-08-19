#coding:gbk
import codecs
import json
import re
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from bs4 import BeautifulSoup
import time
class HtmlParser(object):

    def parser_url(self,page_url,response):
        soup=BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find_all(id,attrs={'data-category':'nowplaying'})
        urls=[]

        for link in links:
            url='https://movie.douban.com/subject/%s/?from=playing_poster'%link['id'] 
            urls.append(url)
        
        if urls!=None :
            # 将urls进行去重
            return list(set(urls))
        else:
            return None





    def parser_release(self,page_url,content):
        '''
        解析已经上映的影片
        var result_201611132231493282 = { "value":{"isRelease":true,"movieRating":{"MovieId":108737,"RatingFinal"
        :7.7,"RDirectorFinal":7.7,"ROtherFinal":7,"RPictureFinal":8.4,"RShowFinal":10,"RStoryFinal":7.3,"RTotalFinal"
        :10,"Usercount":4067,"AttitudeCount":4300,"UserId":0,"EnterTime":0,"JustTotal":0,"RatingCount":0,"TitleCn"
        :"","TitleEn":"","Year":"","IP":0},"movieTitle":"奇异博士","tweetId":0,"userLastComment":"","userLastCommentUrl"
        :"","releaseType":1,"boxOffice":{"Rank":1,"TotalBoxOffice":"5.66","TotalBoxOfficeUnit":"亿","TodayBoxOffice"
        :"4776.8","TodayBoxOfficeUnit":"万","ShowDays":10,"EndDate":"2016-11-13 22:00","FirstDayBoxOffice":"8146
        .21","FirstDayBoxOfficeUnit":"万"}},"error":null};var movieOverviewRatingResult=result_201611132231493282
        :param page_url:电影链接
        :param value:json数据
        :return:
        '''
        movie={}
        soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        
        movie['Name'] = soup.find('span',property="v:itemreviewed").text
        movie['Directors'] = ''                                         
        directors = soup.find_all('a', rel="v:directedBy")
        for director in directors:
            movie['Directors'] += director.text
            movie['Directors'] += '  '
        movie['Stars'] = ''                                             
        stars = soup.find_all('a', rel="v:starring")
        for star in stars:
            movie['Stars'] += star.text
            movie['Stars'] += '  '
        movie['Category'] = ''                                          
        categorys = soup.find_all('span', property="v:genre")
        for category in categorys:
            movie['Category'] += category.text
            movie['Category'] += '  '
        
        
        movie['Year'] = soup.find('span',class_='year').text
        movie['Rate'] = soup.find('strong', property="v:average").text
        movie['Runtime'] = soup.find('span', property="v:runtime").text
        #movie['IMDb'] = soup.find(href=re.compile(r'(https://www.imdb.com/title/*)'))['href']
        movie['Ticket']=soup.find(class_='ticket-btn')['href']
     
        
        
        #将提取其中的内容进行返回
        return movie


