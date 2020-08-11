from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager( ).install())
driver = webdriver.Chrome("C:\\seleniumDriver\\chromedriver.exe")
driver.get("https://sushenbiswas.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.quit()


# class LinkdinMassageBot():
#     def __init__(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome("C:\\seleniumDriver\\chromedriver.exe")
#         driver.get("https://sushenbiswas.com")
