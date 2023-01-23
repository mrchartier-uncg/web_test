from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup


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

    def goto_url_new_tab(self, url):
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(f"{url}")

    def page_scrape(self):
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        return soup

    def find_div_class(self, class_id):
        soup = self.page_scrape()
        try:
            search_item = soup.find_all("div", {"class": f"{class_id}"})
        except:
            search_item = None
        return search_item

    def find_td_class(self, class_id):
        soup = self.page_scrape()
        try:
            search_item = soup.find_all("td", {"class": f"{class_id}"})
        except:
            search_item = None
        return search_item

    def list_html_table(self):
        table_data = []
        header_row = []
        soup = self.page_scrape()
        header = soup.find_all("table")[0].find("tr")
        for items in header:
            try:
                header_row.append(items.get_text())
            except:
                continue
        for element in header_row:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element)
                except:
                    sub_data.append('')
        table_data.append(header_row)
        html_data = soup.find_all("table")[0].find_all("tr")[1:]
        for element in html_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    sub_data.append('')
            table_data.append(sub_data)
        for row in table_data:
            for i, item in enumerate(row):
                item = item.replace('\n', '')
                item = item.replace('\t', '')
                row[i] = item
        return table_data


if __name__ == '__main__':
    ellucian_webpage = selenium_webpage()
    ellucian_webpage.goto_url('https://login.ellucian.com')
    ellucian_webpage.keyboard_input("mrchartier", "okta-signin-username")
    ellucian_webpage.keyboard_input(os.getenv('ellucian_pass'), "okta-signin-password")
    ellucian_webpage.keyboard_enter("okta-signin-submit")
    ellucian_webpage.browser_wait()
    ellucian_webpage.goto_url('https://resources.elluciancloud.com/')
    ellucian_webpage.goto_url('https://resources.elluciancloud.com/category/banner')
