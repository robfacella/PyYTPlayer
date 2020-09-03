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
def playVideo(driver, url):
    driver.get(url)
    driver.find_element_by_id("movie_player").click()
    vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    while vidStatus != 0:
       #according to <https://developers.google.com/youtube/js_api_reference?csw=1> state == 0 is when a video has ended
        vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        time.sleep(1) #Wait a second and check again.
def main():
    driver = createWebdriver()
    #for url in list:
    playVideo(driver, "https://www.youtube.com/watch?v=80RzZkMCLOY")
    #testSearch(driver)
main()
