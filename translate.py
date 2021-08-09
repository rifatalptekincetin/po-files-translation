from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from poreader import get_po,save_po

translate="https://translate.google.com/"

browser = webdriver.Chrome()

browser.get(translate)

waitfor=input("set 'from' and 'to' languages and press enter")


def trans(text):
    ti=browser.find_elements_by_tag_name("textarea")[0]
    ti.click()
    ti.send_keys(Keys.CONTROL, 'a')
    ti.send_keys(text)
    time.sleep(3),
    return browser.find_elements_by_xpath("//c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]")[0].text.replace("\n","")

po = get_po("homeradar-add-ons-tr_TR.po")

lenpo=len(po)
count=0

for i in po:
    count+=1
    if i.id and "%" not in i.id and "<" not in i.id:
        i.string=trans(i.id)
        print(count,"/",lenpo)

save_po(po,"out.po")
