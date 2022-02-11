"""
Hossein Jalili
feb-11-2022
version 1.0.0

Sending an automatic message in the student system of 
Sobhe Sadegh Non-Profit Higher Education Institute

"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import jdatetime


clear=lambda : os.system("cls")
now = jdatetime.datetime.now()


print("--------------------")
user_name=input("Enter your username: \t")
user_pass=input("Enter your password: \t")
print("--------------------")
user_reciver=input("Enter Number_Student your reciver: \t")
title=input("Enter title: \t")
body=input("Enter body: \t")
print("--------------------")
# list_massage=[]
# list_massage.append(user_name)
# list_massage.append(user_pass)
# list_massage.append(user_reciver)
# list_massage.append(title)
# list_massage.append(body)
# print(list_massage)
clear()

now = jdatetime.datetime.now()
print("time start is: ",now)

path = os.path.dirname(os.path.abspath(__file__))
address=os.path.join(path, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=address)
driver.get('http://91.240.61.58:8080/Default.aspx')
print("\n\n**** open web page **** \n\n")
time.sleep(5)
clear()

try:
    login_user=driver.find_element_by_xpath('//*[@id="username"]')
    login_user.send_keys(user_name)
    print("\n\n**** entered username **** \n\n")
except:
    print("can't find user input bax")
time.sleep(1)
clear()
try:
    login_pass=driver.find_element_by_xpath('//*[@id="password"]')
    login_pass.send_keys(user_pass)
    print("\n\n**** entered password **** \n\n")
except:
    print("can't find pass input bax")
time.sleep(1)
clear()
try:
    login_button=driver.find_element_by_xpath('//*[@id="btnLogin"]')
    login_button.click()
    print("\n\n**** clicked login **** \n\n")
except:
    print("can't find login button bax")
clear()
print("\n\n**** entered username **** \n\n")
print("\n\n**** entered password **** \n\n")
print("\n\n**** clicked login **** \n\n")
time.sleep(5)
clear()
#----------------------------------------------
try:
    payam_button=driver.find_element_by_xpath('//*[@id="ctl00_HyperLink4"]/span')
    payam_button.click()
    print("\n\n**** finded payam botton **** \n\n")
except:
    print("can't find payam button bax")
clear()
print("\n\n**** entered username **** \n\n")
print("\n\n**** entered password **** \n\n")
print("\n\n**** clicked login **** \n\n")
print("\n\n**** finded payam botton **** \n\n")
time.sleep(5)
clear()

try:
    payam_button1=driver.find_element_by_xpath('//*[@id="ctl00_content_lstReciver_chosen"]/ul/li/input')
    payam_button1.click()
    time.sleep(2)
    clear()
    payam_button1.send_keys(user_reciver)
    print("\n\n**** entered receiver **** \n\n")
    time.sleep(2)
    payam_button1.send_keys(Keys.ENTER)
except:
    print("can't find payam button 1 bax")
time.sleep(1)

try:
    payam_button2=driver.find_element_by_xpath('//*[@id="ctl00_content_txtTitle"]')
    payam_button2.send_keys(title)
    print("\n\n**** entered title **** \n\n")
except:
    print("can't find payam button 2 bax")
clear()
print("\n\n**** entered username **** \n\n")
print("\n\n**** entered password **** \n\n")
print("\n\n**** clicked login **** \n\n")
print("\n\n**** finded payam botton **** \n\n")
print("\n\n**** entered receiver **** \n\n")
print("\n\n**** entered title **** \n\n")
time.sleep(3)
clear()

#----------------------
try:
    payam_button3=driver.find_element_by_xpath('//*[@id="cke_13_label"]')
    payam_button3.click()
    time.sleep(2)
    clear()
    payam_button4=driver.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea')
    payam_button4.click()
    payam_button4.send_keys(body)
    print("\n\n**** entered body **** \n\n")
    time.sleep(1)
except:
    print("can't find payam button 3 and 4 bax")
clear()
print("\n\n**** entered username **** \n\n")
print("\n\n**** entered password **** \n\n")
print("\n\n**** clicked login **** \n\n")
print("\n\n**** finded payam botton **** \n\n")
print("\n\n**** entered receiver **** \n\n")
print("\n\n**** entered title **** \n\n")
print("\n\n**** entered body **** \n\n")
time.sleep(2)
clear()

try:
    payam_button5=driver.find_element_by_xpath('//*[@id="ctl00_content_btnSend"]')
    payam_button5.click()
    print("\n\n**** clicked send **** \n\n")
    # time.sleep(1)

except:
    print("can't find payam button 5 bax")
clear()

now2 = jdatetime.datetime.now()
print("--------------------------------")
print("time start is: ",now)
print("**** entered username **** ")
print("**** entered password **** ")
print("**** clicked login **** ")
print("**** finded payam botton **** ")
print("**** entered receiver **** ")
print("**** entered title **** ")
print("**** entered body **** ")
print("**** clicked send **** ")
print("time end is: ",now2)

print("--------------------------------")
print("your username:\t",user_name)
print("your password:\t","********")
print("your receiver:\t",user_reciver)
print("your title:\t",title)
print("your body:\t",body)

time.sleep(2)
driver.quit()
# clear()
















