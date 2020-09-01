from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path=r'C:\Users\sandhya\PycharmProjects\chrome\chromedriver.exe')
browser.implicitly_wait(5)
browser.maximize_window()

browser.get("https://www.hudl.com")

browser.find_element_by_xpath("/html/body/div[2]/header/div[2]/ul/li[3]/a").click()

browser.find_element_by_id("email").send_keys("rawoolsandhya97@gmail.com")
browser.find_element_by_id("password").send_keys("hudlsandhya03")
time.sleep(5)

browser.find_element_by_id("logIn").click()

browser.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]/span").click()
time.sleep(5)

browser.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]/span").click()
time.sleep(5)

browser.close()