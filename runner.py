import time
from selenium import webdriver

def testSearch(driver):
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()
def createWebdriver():
    driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    return (driver)
def main():
    driver = createWebdriver()
    #testSearch(driver)
main()
