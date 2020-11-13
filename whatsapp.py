from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

k =input("PLEASE SCAN QR CODE AND SCAN  AND PRESS ANY KEY TO CONTINUE : ")

LK = driver.find_element_by_css_selector('span[title="Name of friend"]')

LK.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")


testinput.send_keys("Type your message here")
 

testinput.send_keys(Keys.RETURN)