from selenium import webdriver
import os
import os.path as path

class Headless:
    def __init__(self, agent,  headless: bool = False):

        filepath = os.getcwd() + '/chromedriver/chromedriver'

        if path.isfile(filepath) is False:
            error_string = f"Couldn\'t locate chromedriver at: {os.getcwd()}/chromedriver/"
            raise FileNotFoundError(error_string)

        if agent is None:
            raise Exception("Couldn\'t find its user agente, if you don't know yours, google \"My user agent.\"")

        if type(headless) is not bool:
            raise AttributeError(f'Expected boolean type on headless, got {type(headless)}')

        print(f"FILEPATH = {filepath}")
        self.webdriver_path = filepath
        self.headless = headless

        if headless is True:
            self.user_agent = agent
            self.options = webdriver.ChromeOptions()

            self.options.headless = headless
            self.options.add_argument(f'user-agent={self.user_agent}')
            self.options.add_argument('--window-size=1920,1080')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument('--allow-running-insecure-content')
            self.options.add_argument('--disable-extensions')
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument('--proxy-bypass-list=*')
            self.options.add_argument('--start-maximized')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')

            print(self.options)
        else:
            self.options = ''
        pass

    def web_driver(self):
        if self.headless is True:
            return webdriver.Chrome(executable_path=self.webdriver_path, options=self.options)
        else:
            return webdriver.Chrome(self.webdriver_path)
        pass
    pass

