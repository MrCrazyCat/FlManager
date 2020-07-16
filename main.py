import time
import sqlite3
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://kwork.ru/"

db = sqlite3.connect('Account.db')
cur = db.cursor()

x = 1

while(True):

	cur.execute(f"SELECT EMAIL FROM Account WHERE ID = '{x}'")
	email = str(cur.fetchone()[0])

	cur.execute(f"SELECT PASS FROM Account WHERE ID = '{x}'")
	password = str(cur.fetchone()[0])

	driver = webdriver.Chrome()
	driver.get(url)
	time.sleep(2)

	entery = driver.find_element_by_link_text("Вход")
	entery.click()

	time.sleep(2)

	login_input = driver.find_element_by_id("l_username")
	login_input.send_keys(email)

	time.sleep(3)

	pass_input = driver.find_element_by_id("l_password")
	pass_input.send_keys(password)

	time.sleep(2)

	ent_btn = driver.find_element_by_css_selector("button.js-inPopup")
	ent_btn.click()

	time.sleep(5)

	driver.get('https://kwork.ru/inbox')
	requiredHtml = driver.page_source
	soup = BeautifulSoup(requiredHtml, features="html.parser")

	time.sleep(2)
	#mydivs = soup.find_all("ul", class_="chat__list")
	uname = soup.find_all("div", class_="chat__list-user")
	print(uname)
	#text_order = soup.find_all("a")
	driver.quit()

	#print(text_order)
	name_order_for_bot = uname
	#text_order_for_bot = text_orer
	
	if x == 2:
		break
	x = x+1