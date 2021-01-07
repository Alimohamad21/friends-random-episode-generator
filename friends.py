import time
from random import randint

from selenium import webdriver

driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')


def close_second_tab():
    while True:
        if len(driver.window_handles) == 2:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            break


series = "friends"
season = randint(1, 10)
episode = randint(1, 24)
driver.get("https://esco.egybest.network/episode/{}-season-{}-ep-{}/#download".format(series, season, episode))
player = driver.find_element_by_xpath("//iframe[@class='auto-size']")
while len(driver.window_handles) != 2:
    player.click()
close_second_tab()
player.click()
time.sleep(1)
while len(driver.window_handles) != 2:
    player.click()
close_second_tab()
player.click()
driver.find_element_by_xpath("//*[text()='لاحقاً']").click()
close_second_tab()
