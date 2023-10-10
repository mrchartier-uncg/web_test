
# You will need to pull the current version of edge on this machine from the edge web driver page:
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# ----------
# Selenium is used along with BeautifulSoup due to the javascript tables used
# in both the ESM and Ellucian documentation pages.
# https://www.selenium.dev/documentation/

import os
import logging
import selenium_test as web
import config
import sys
import csv


def csv_writer(filename, data):
    with open(filename, 'w+', newline='') as csv_file:
        table_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        table_writer.writerows(data)


logging.basicConfig(level='DEBUG',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    handlers=[logging.FileHandler("test.log"),
                                logging.StreamHandler(sys.stdout)])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ellucian = web.selenium_webpage()
    # ellucian.goto_url('https://login.ellucian.com')
    # ellucian.keyboard_input("mrchartier", "okta-signin-username")
    # ellucian.keyboard_input(os.getenv('ellucian_pass'), "okta-signin-password")
    # ellucian.keyboard_enter("okta-signin-submit")
    # ellucian.browser_wait()
    ellucian.goto_url_new_tab("https://esm.uncg.edu/admin/login/auth")
    ellucian.keyboard_input("mis_developer", "username")
    ellucian.keyboard_input(os.getenv('esm_password'), "password")
    ellucian.keyboard_enter("submit")
    ellucian.goto_url("https://esm.uncg.edu/admin/adminEnv/products?envName=BANPRD")
    # page_output = ellucian.list_html_table()
    # table_data = []
    # for row in page_output:
    #     clean_row = [row[1], row[3], row[5], row[7], row[9]]
    #     table_data.append(clean_row)
    # csv_writer('ellucian_products.csv', table_data)
    page_buttons = ellucian.find_buttons()
    for item in page_buttons:
        print(item)
