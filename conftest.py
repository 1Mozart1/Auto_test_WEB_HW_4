import pytest
import requests
import yaml
# from webdriver.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser1 = testdata["browser"]
    site_login = testdata["site_login"]
    site_post = testdata["site_post"]


@pytest.fixture(scope="session")
def browser():
    global driver
    if browser1 == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    # else:
    #     service = Service(executable_path=ChromeDriverManager().install())
    #     options = webdriver.ChromeOptions()
    #     driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# @pytest.fixture()
# def user_title_list():
#     result = requests.post(url=site_login, data={"username": testdata["username"], "password": testdata["password"]})
#     token = (result.json()["token"])
#     res_get = requests.get(url=site_post, headers={"X-Auth-Token": token}, params=testdata["owner"])
#     title_list = [item["title"] for item in res_get.json()["data"]]
#     return title_list
#
#
# @pytest.fixture()
# def user_description_list():
#     result = requests.post(url=site_login, data={"username": testdata["username"], "password": testdata["password"]})
#     token = (result.json()["token"])
#     res_get = requests.get(url=site_post, headers={"X-Auth-Token": token}, params=testdata["owner"])
#     description_list = [item["description"] for item in res_get.json()["data"]]
#     return description_list
