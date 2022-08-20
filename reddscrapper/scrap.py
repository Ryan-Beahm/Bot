# selenium 4
import reddscrapper.constants as Const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# selenium4 reddit scrapper class

class scrapper(ChromeDriverManager, webdriver.Chrome):
    # constructor
    def __init__(self, teardown=False):
        super(scrapper, self).__init__()
        self.teardown = teardown
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        print(self.teardown)

# destructor (might be redundant)
    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown == True:
            self.driver.quit()

# open url function, takes url as parameter
    def open_url(self):
        self.driver.get(Const.BASE_URL)

# get links function, returns list of links
    def get_links(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            print(link.get_attribute("href"))


# get all links with a k value

    def get_all_links(self):
        values = self.driver.find_elements(
            By.CSS_SELECTOR, 'span[data-testid="post_timestamp"]'
        )

# fuck it all start with selenium base tomorrow
