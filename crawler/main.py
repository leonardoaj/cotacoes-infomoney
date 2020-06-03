# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import pickle
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()

options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("disable-infobars")
options.add_argument("--window-size=1920x1080")

options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True
})

path = os.path.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.path.sep)[:-1])
driver = webdriver.Chrome(
    chrome_options=options,
    executable_path=os.path.sep.join([path, "drivers", "chromedriver"])
)

actions = ActionChains(driver)

input_file = open("input.dat", "r").readlines()
datas = input_file[0].split(" ")
tickets = [x.strip() for x in input_file[1:]]

for ticket in tickets:

    driver.get("https://www.infomoney.com.br/cotacoes/")
    time.sleep(1)
    driver.find_element_by_css_selection("#select2-cotacoes-search-container").click()
    time.sleep(1)
    driver.find_element_by_css_selection("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(ticket)

    results = driver.find_elements_by_css_selection("#select2-cotacoes-search-results > li")
    for result in results:
        if ticket in result.text:
            result.click()

    driver.find_element_by_css_selection("body > div.fill-lightgray.border-b > div > div.quotes-options > a:nth-child(3)").click()
    driver.find_element_by_css_selection("#dateMin").send_keys(datas[0])
    driver.find_element_by_css_selection("#dateMax").send_keys(datas[1])
    driver.find_element_by_css_selection("#quotes_history_wrapper > div > button").click()
