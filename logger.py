from time import sleep
from selenium import webdriver
import sys
import getopt


class Log:
    def __init__(self, url, user_field, pass_field, user, pword, redirect):
        self.url = url
        self.user_field = user_field
        self.pass_field = pass_field
        self.username = user
        self.password = pword
        self.redirect = redirect


def main(argv):
    # file = open("logs.xyz", "r")
    opts = []
    args = []
    try:
        opts, args = getopt.getopt(argv, "f:", ["file="])
    except getopt.GetoptError:
        print('logger.py -f <filename>')
        sys.exit(2)

    file = None
    for opt, arg in opts:
        if opt in ("-f", "--file"):
            file = open(arg, "r")

    if file is None:
        sys.exit(1)

    log_list = []
    getLogs(file, log_list)
    driver = setChromeOptions()
    logIn(driver, log_list)


def getLogs(file, log_list):
    # Format of each line in file is: Site Username_Field Password_Field username password redirect
    for line in file:
        info = line.split(" ")
        if info is not None:
            redirect_url = (None if len(info) < 6 else info[5])
            log_list.append(Log(info[0], info[1], info[2], info[3], info[4], redirect_url))


def setChromeOptions():
    chrome_options = webdriver.ChromeOptions()
    # Add extensions below. Make sure you've have the .crx of each extension you want and send .add_extension() its
    # path
    chrome_options.add_extension('extension1.crx')
    chrome_options.add_extension('extension2.crx')
    # Suppress silly error
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Keep chrome open
    chrome_options.add_experimental_option("detach", True)
    # Change everything after 'r' to be the path of your chromedriver.exe
    driver = webdriver.Chrome(options=chrome_options, executable_path=r'chromedriver.exe')
    return driver


def logIn(driver, log_list):
    next_tab = 1
    for log in log_list:
        driver.get(log.url)

        username = driver.find_element_by_name(log.user_field)
        username.send_keys(log.username)

        password = driver.find_element_by_name(log.pass_field)
        password.send_keys(log.password + "\n")

        if log.redirect is not None:
            sleep(2)
            driver.get(log.redirect)

        driver.execute_script("window.open()")
        tabs = driver.window_handles
        driver.switch_to.window(tabs[next_tab])
        next_tab += 1


if __name__ == "__main__":
    main(sys.argv[1:])
