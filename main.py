import os
import logging
import selenium_test as web


def log_function(message, level):
    if level == 'info':
        logging.info(message)
    print(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ellucian = web.selenium_webpage()
    ellucian.goto_url('https://login.ellucian.com')
    ellucian.keyboard_input("mrchartier", "okta-signin-username")
    ellucian.keyboard_input(os.getenv('ellucian_pass'), "okta-signin-password")
    ellucian.keyboard_enter("okta-signin-submit")
    ellucian.browser_wait()
    ellucian.mouse_click('Resources')
    ellucian.goto_url('https://resources.elluciancloud.com/bundle/'
                      'banner_admin_common_rel_release_notes/page/c_lnd_relnotes.html')
