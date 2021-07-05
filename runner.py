import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import shuffle
import os
import sys
def testSearch(driver):
    driver = createWebdriver()
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user see something
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()
def createWebdriver():
    #Set path of Driver to the one in Local Dir
    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    #Generate a FirefoxProfile
    profile = FirefoxProfile()
    #for that profile Disable- Web Push Notifications
    profile.set_preference("permissions.default.desktop-notification", 1)
    #Hopefully incorporate uBlock
    absolutePathHack = os.environ['PWD'] #Not ideal, but she WORKS!
    ublockfile = os.path.normpath(os.path.join(absolutePathHack, 'uBlock0@raymondhill.net'))
    #Create a driver with the above settings
    try:
        driver = Firefox(profile, executable_path=gecko+'.exe')
    except:
                print ("[*] Could not locate < geckodriver.exe >")
                print ("[*] Exiting..")
    try:
        #Try to add local ublock.xpi to the browser; don't crash if that fails though.
        driver.install_addon(ublockfile+'.xpi', temporary=True)
    except:
        print ("Could not install uBlock Origin. Is uBlock0@raymondhill.net.xpi in the same folder as the script? ")
        print ("Try running the script from the directory it is located in, used a PWD hack for the Required AbsolutePath for AddonInstallation.")
        print ("Will function anyway, but do you REALLY want to do this without an AdBlocker?")
    return (driver)
def sanitizeTextFromHTML(htmlToPrint):
    f = open(os.devnull, 'w') #for writing garbage print-check text to null
    htmlText = htmlToPrint.text
    output = ""
    for chara in htmlText:
        try:
            f.write(chara) #Makes sure character is printable, but writes to <null> as so not to make a mess of the CLI
            output = output + chara
        except:
            #Replace char which couldn't be encoded (ie unicode error) with the string <?>
            #Prevents interpreter crash trying to print.
            output = output + "<?>"
    f.close()
    #print (output)
    #sys.stdout.flush()
    return (output)
def getVideoDetails(driver):
    try:
        wait = WebDriverWait(driver, 10)
        song = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"yt-formatted-string.ytd-video-primary-info-renderer:nth-child(1)")))
    except:
        song = "ERROR"
    try:
        wait = WebDriverWait(driver, 10)
        chan = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"ytd-channel-name.ytd-video-owner-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1) > a:nth-child(1)")))
    except:
        chan = "ERROR"
    print ("Now Playing: ")
    print ( sanitizeTextFromHTML(song) )
    print ( "on Channel: " + sanitizeTextFromHTML(chan) )
    sys.stdout.flush()
    print ("")
def playVideo(driver, url):
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_id("movie_player").click() #No AutoPlay, smei-Auto workaround
        time.sleep(1)
        try:
            #Not sure why but this added try/except block seemed to improve the success rate of the nested statements?, makes no sense but SURE why not.
            getVideoDetails(driver)
        except:
            print ("Call to 'getVideoDetails(driver)' failed.")
            sys.stdout.flush()
        vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        while vidStatus != 0:
            #according to <https://developers.google.com/youtube/js_api_reference?csw=1> state == 0 is when a video has ended
            vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            time.sleep(1) #Wait a second and check again.
    except:
        print("Encountered an error trying to play from < ")
        print (url + "> skipping item." )
        print ("")
        sys.stdout.flush()

def getPlaylist():
        playlistFile = open(os.path.join('playlist.txt'))
        playlist = playlistFile.readlines()
        playlistFile.close()
        shuffle(playlist)
        return(playlist)
def main():
    driver = createWebdriver()
    playlist = getPlaylist()
    for url in playlist:
        playVideo(driver, url)
    print ("End of Playlist. Goodbye.")
main()
#testSearch()
