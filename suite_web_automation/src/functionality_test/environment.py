from selenium import webdriver
from resource.tools import browser_path
import datetime

def before_all(context):
    context.tester_name     = "Tomi"
    # context.config.format   = context.config.userdata['formatter']
    # context.config.outfiles = 'E:\Project\BehavePythonProject\suite_web_automation\\results'
    context.browser = context.config.userdata["browser"].lower()
    match context.browser:
        case "chrome":
            context.driver = webdriver.Chrome(browser_path.use_chrome())
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
    pass

def before_scenario(context,scenario):
    pass

def after_scenario(context,scenario):
    pass

def before_step(context,step):
    pass

def after_step(context,step):
    pass
