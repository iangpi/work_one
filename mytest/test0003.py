from selenium import webdriver
ff=webdriver.Firefox()
ff.get("http://www.baidu.com")
els=ff.find_elements_by_class_name("mnav")
res=[]
for el in els:
    res.append(el)
print len(res)
n=len(res)
for i in xrange(n):
    print res[i].text
#print res[0].text,res[1].text,res[2].text,res[3].text,res[4].text,res[5].text