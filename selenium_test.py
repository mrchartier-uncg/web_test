from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


class selenium_webpage():
    service = Service(executable_path="C:/path/edge_driver/msedgedriver.exe")
    browser = webdriver.Edge(service=service)

    def goto_url(self, url, wait_time=3):
        self.browser.get(url)
        self.browser.implicitly_wait(wait_time)

    def keyboard_input(self, value, element_id):
        element = self.browser.find_element(by=By.ID, value=element_id)
        element.send_keys(value)

    def keyboard_enter(self, element_id):
        element = self.browser.find_element(by=By.ID, value=element_id)
        element.send_keys(Keys.ENTER)

    def mouse_click(self, link_text):
        element = self.browser.find_element(by=By.LINK_TEXT, value=link_text)
        element.click()

    def browser_wait(self, wait_time=3):
        self.browser.implicitly_wait(wait_time)


if __name__ == '__main__':
    ellucian_webpage = selenium_webpage()
    ellucian_webpage.goto_url('https://login.ellucian.com')
    ellucian_webpage.keyboard_input("mrchartier", "okta-signin-username")
    ellucian_webpage.keyboard_input(os.getenv('ellucian_pass'), "okta-signin-password")
    ellucian_webpage.keyboard_enter("okta-signin-submit")
    ellucian_webpage.browser_wait()
    ellucian_webpage.mouse_click('Resources')
    ellucian_webpage.goto_url('https://resources.elluciancloud.com/bundle/banner_admin_common_rel_release_notes/page/c_lnd_relnotes.html')
