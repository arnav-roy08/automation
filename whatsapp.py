from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import itertools
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=user-data")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 60)
print("Chrome opened successfully!")


Web_whatsapp = 'https://web.whatsapp.com/'  # To go to whatsapp web
driver.get(Web_whatsapp)
print("Accessing Whatsapp web")

Number = ['8882331701' , '9999750882']

for i in zip(Number):
    try:

        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(f'https://web.whatsapp.com/send?phone=+91{i}')
        time.sleep(5)
        textbox = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
        textbox.send_keys("*Greetings from Entrepreneurship Development Cell, IIT Delhi*")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("*Congratulations!* on your successful registration for *BECon'21*. You are just a click away from experiencing a magnificent 4-day entrepreneurial extravaganza at the annual Business and Entrepreneurship Conclave BECon 2021.")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("*About BECon:* eDC IITD is hosting its *Annual Business and Entrepreneurship Conclave 2021* (BECON), from *1st to 4th April 2021*. BECon is North India’s biggest E-Summit, with numerous events, keynote lectures of eminent personalities, workshops, panel discussions, and much more! Some notable guests in the past include *Mark Zuckerberg (CEO, Facebook), Jack Dorsey (CEO, Twitter), Dara Khosrowshahi (CEO, Uber), and Elie Seidman (CEO, Tinder) and many more.* You will have an astonishing experience of *townhall sessions, panel talks, networking sessions, creators conclave, founders talk and numerous competitions.*")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("You will receive *participation certificates* for all the events you attend, along with an opportunity for *one-on-one interaction with the guest speakers.*")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("To confirm your seat for the conclave, you are kindly requested to pay the required fees of *Rs 149*. using https://rzp.io/l/becon")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Offical website of Becon 2021: https://edc.iitd.ac.in/becon")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("You may contact the undermentioned in case of any queries. For more details, you can also visit our pages.")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("https://www.facebook.com/edciitdelhi")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("https://www.linkedin.com/company/edc-iit-delhi/")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("https://www.instagram.com/edc_iitd/")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("regards,")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Arnav Sudan")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Technical Executive, eDC IIT Delhi")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Uddipan Debnath")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Coordinator, eDC IIT Delhi")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("+91 9366155938")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Ayush Pandey")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("Coordinator, eDC IIT Delhi")
        textbox.send_keys(Keys.SHIFT + Keys.ENTER)
        textbox.send_keys("+91 8290927498")







        textbox.send_keys(Keys.ENTER)

        time.sleep(5)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    except:
        print(i)
        time.sleep(5)



