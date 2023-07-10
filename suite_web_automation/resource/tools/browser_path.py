#import AutoChromedriver
import os

def use_chrome():
    return parser.get_chrome_path


# parser the chrome here
class parser:
    get_chrome_path = os.path.join(os.path.dirname(__file__),"chromedriver_linux64","chromedriver")

    ## There is an error in permission, gonna fix later
    # FIX
    # AutoChromedriver.download_chromedriver()

