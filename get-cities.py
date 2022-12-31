from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import json

def getCities():
    edgeBrowser = webdriver.Edge(EdgeChromiumDriverManager().install())
    url = "https://goturkiye.com/turkiye-destinations"
    edgeBrowser.get(url)
    time.sleep(1)
    slider = edgeBrowser.find_element_by_xpath("/html/body/div[1]/main/section/div[2]/div/div/div")
    codes = slider.get_attribute("outerHTML")
    time.sleep(1)
    edgeBrowser.close()
    splitted = codes.split("<div class=\"col-lg-2 col-xs-6 col-sm-4 col-md-3 col-xl-2\">")
    splitted = splitted[1:]
    cities = {}
    for code in splitted:
        code = code.replace("</div>","")
        code = code.split('<a href="')[1]
        url = code[:code.index('"')]
        imgCode = code.split('img src="')[1]
        img = imgCode[:imgCode.index('"')]
        city = url.split("go")[1]
        name = city.replace("turkiye.com","")
        name = name.replace("/","")
        name = name.replace("homepage","")
        if(name != ""):
            cities[name] = {"img": img, "url": url}
    return cities

def writejson(dic):
    json_object = json.dumps(dic, indent= 4)
    with open("cities-data.json", "w") as outfile:
        outfile.write(json_object)

cities = getCities()
writejson(cities)