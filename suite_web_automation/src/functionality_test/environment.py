from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from resource.tools import browser_path
from selenium_stealth import stealth

import datetime

from fake_useragent import UserAgent

def before_all(context):
    context.tester_name     = "Tomi"
    context.browser = context.config.userdata["browser"].lower()

    # random user agent
    # ua         = UserAgent()
    # user_agent = ua.random
    # options.add_argument(f'user-agent={user_agent}')

    # fixing some issue
    # https://stackoverflow.com/questions/56528631/is-there-a-version-of-selenium-webdriver-that-is-not-detectable/56529616#56529616
    # https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec/53040904#53040904
    # https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

    match context.browser:
        case "chrome":
            # Fixing some cookies/cache issue
            options = Options()
            options.add_argument("start-maximized")

            # deactivate automated test software, to by pass security
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            service        = Service(browser_path.use_chrome())
            context.driver = webdriver.Chrome(service=service,options=options)
            context.action = ActionChains(context.driver)
            stealth(context.driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )
        case "firefox":
            pass
        case "opera":
            pass
        case _:
            raise Exception("Cannot find suitable webdriver for the test")

def before_feature(context,feature):
    print(f"Currently running feature test of :{context.feature.name}")
    print(f"Desc\t:{context.feature.description}")
    print(f"Tester\t:{context.tester_name}")
    print(f"Browser\t:{context.browser}")
    print(f"Date\t:{datetime.datetime.now()}\n\n")

def after_feature(context,feature):
    context.driver.quit()

def before_scenario(context,scenario):
    pass

def after_scenario(context,scenario):
    pass

def before_step(context,step):
    pass

def after_step(context,step):
    pass
