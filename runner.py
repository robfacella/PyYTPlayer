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
    #for url in list:
    #    driver.get()url
    #    driver.find_element_by_id("movie_player").click()
    #    vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    #    while vidStatus != 0:
    #        vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            #according to <https://developers.google.com/youtube/js_api_reference?csw=1>
            #state == 0 is when a video has ended
            #time.sleep(1)
    #testSearch(driver)
main()
