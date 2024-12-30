from seleniumwire import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import json , requests

req_url = "https://api.ssyoutube.com/api/convert"
def get_js(link):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless') 
    driver = webdriver.Firefox(options=options)
    print('Operating website ...')
    driver.get("https://ssyoutube.com")
    btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_url')))
    print('Typing link ..')
    btn.send_keys(link)
    btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))
    sleep(1)
    btn.click()
    sleep(2)
    print('Getting data ..')
    for request in driver.requests:
        url = request.url
        if url == req_url :
            js = request.body.decode('utf-8')
            break
    return js


def download(url) :
    js = get_js(url)
    print('Sending request ...')
    res = requests.post(req_url,json=json.loads(js))
    response = res.json()
    name = response['meta']['title']
    download_link = response['url'][0]['url']
    return name ,download_link



