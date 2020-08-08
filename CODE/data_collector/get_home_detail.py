#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 23:50
# @Author  :  Yanli Sun
# @Site    : 
# @File    : get_home_detail.py
# @Software: PyCharm

import requests
import time
from requests.exceptions import SSLError

from get_detail_url_list import get_detail_url_list
import re
import csv
import os
import random
# user_agent list
user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

class get_home_detail():
    def __init__(self):
        self.detail_url_list = get_detail_url_list()
        self.list_url = []
        self.list_url.append(self.detail_url_list.list1)
        self.list_url.append(self.detail_url_list.list2)
        self.list_url.append(self.detail_url_list.list3)
        self.list_url.append(self.detail_url_list.list4)
        self.list_url.append(self.detail_url_list.list5)
        # print(self.list_url)
        self.detail_url_list.print_list()

    def detail_url_requests_1(self):
        for x in range(0,len(self.list_url)):
            for i in range(0,len(self.list_url[x])):
                try:
                    time.sleep(random.random() * 10)
                    detail_url = "https://www.zillow.com" + self.list_url[x][i]
                    # print("current URL is"：",detail_url)
                    headers = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'user-agent': random.choice(user_agent_list)
                        }
                    res = requests.get(url=detail_url, timeout=5, headers=headers)
                    print(res.status_code)
                    # print(type(res))
                    content = res.content.decode("utf-8")
                    # print(content)


                    # /b tag is for rent
                    print(type(self.list_url))
                    if self.list_url[x][i][1] == 'b':
                        pat = '"fullAddress":"(.*?)"'
                        # get address
                        Address = re.compile(pat,re.S).findall(content)
                        info_pat = '"adTargets":{(.*?)},'
                        info = re.compile(info_pat,re.S).findall(content)
                        if info:
                            dict_info = eval('{'+info[0]+'}')
                            self.write_to_csv_apartment(dict_info,Address)
                        else:
                            print("info of current house does not exist")
                    else:
                        house_dict = {}
                        add_pat = '\\\\"streetAddressOnly\\\\":\\\\"(.*?)\\\\"'
                        streetAddressOnly = re.compile(add_pat, re.S).findall(content)
                        house_dict['Address'] = streetAddressOnly

                        price_pat = '\\\\"priceForHDP\\\\":(.*?),'
                        priceForHDP = re.compile(price_pat, re.S).findall(content)
                        house_dict['Price'] = priceForHDP

                        livingArea_pat = '\\\\"livingArea\\\\":(.*?),'
                        livingArea = re.compile(livingArea_pat, re.S).findall(content)
                        house_dict['livingArea'] = livingArea

                        bedrooms_pat = '\\\\"bedrooms\\\\":(.*?),'
                        bedrooms = re.compile(bedrooms_pat, re.S).findall(content)
                        house_dict['bedrooms'] = bedrooms

                        bathroom_pat = '\\\\"bathrooms\\\\":(.*?),'
                        bathroom = re.compile(bathroom_pat, re.S).findall(content)
                        house_dict['bathroom'] = bathroom

                        self.write_to_csv_homedetail(house_dict)


                except requests.exceptions.ConnectionError as e:
                    print("current list, the",i,"th has error",e)
                except requests.exceptions.ReadTimeout as e:
                    print("current list, the", i, "th has error", e)
                else:
                    pass

    def write_to_csv_homedetail(self,house_dict):
        fieldnames = ["Address", "Price", "livingArea", "bedrooms", "bathroom"]
        with open("House_info.csv", "a", encoding="utf-8", newline='') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            if os.path.getsize("House_info.csv") == 0:
                writer.writeheader()
            # writer.writerow([house_list[0],house_list[1],house_list[2],house_list[3],house_list[4]])
            writer.writerow({'Address': house_dict['Address'],
                             'Price': house_dict['Price'],
                             'livingArea': house_dict['livingArea'],
                             'bedrooms': house_dict['bedrooms'],
                             'bathroom': house_dict['bathroom']})
        csv_file.close()




    def write_to_csv_apartment(self,home_info,Address):
        home_info['Address'] = Address[0]
        fieldnames = ["Address","price","sqft","bd","ba"]
        with open("Apartment_info.csv","a",encoding="utf-8",newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if os.path.getsize("Apartment_info.csv") == 0:
                writer.writeheader()
            writer.writerow({'Address':home_info['Address'],
                            'price':home_info['price'],
                            'sqft':home_info['sqft'],
                            'bd':home_info['bd'],
                            'ba':home_info['ba']})
            csv_file.close()

if __name__ == '__main__':
    try:
        zillow = get_home_detail()
        zillow.detail_url_requests_1()
    except Exception as e:
        print(e)
