from selenium import webdriver
from getpass import getpass

usr = input('Enter email: ')
pwd = getpass('Enter password: ')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

username_box = driver.find_element_by_id('pass')
username_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()
