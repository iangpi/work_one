from selenium import webdriver
ff=webdriver.Firefox()
ff.get("http://www.baidu.com")
els=ff.find_elements_by_class_name("mnav")
res=[]
for el in els:
    res.append(el)
print res[0].text
print res[1].text
print res[2].text
print res[3].text
print res[4].text
print res[5].text