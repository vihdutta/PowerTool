import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

runamount = 0
gradelist1 = []
gradelist2 = []
classlist = []
quarterDict = {'1': 13, '2': 14, '3': 15, '4': 16}

def powerScrape(username, password, quarterinput):
    global gradelist1
    global gradelist2
    global runamount
    runamount += 1

    #initiates driver/driver preferences
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #supresses errors (IMPORTANT)
    options.headless = True
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get('https://sis.henrico.k12.va.us/public/home.html')

    #waits at most 10 seconds to find an element (which indicates the website has loaded)
    try:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'login-inputs')))
    except:
        print('Loading took too long!')

    #finds username, password, and login boxes
    login_button = driver.find_element_by_id('btn-enter-sign-in')
    user_input = driver.find_element_by_name('account')
    pass_input = driver.find_element_by_name('pw')
    #fills boxes with cresidentials
    user_input.send_keys(username)
    pass_input.send_keys(password)
    #attempts login
    login_button.click()

    #finds grades and classnames by xpath
    grades = driver.find_elements_by_xpath('//*[starts-with(@id, "ccid")]/td[%s]/a'%quarterDict[quarterinput])
    classnames = driver.find_elements_by_xpath('//*[starts-with(@id, "ccid")]/td[12]')

    gradelist1.clear()
    #appends cached grade data if it exists
    try:
        if runamount == 1:
            with open('gradelist.json','r') as f:
                gradelist1 = json.load(f)
    except FileNotFoundError:
        pass
    gradelist1.extend(gradelist2)
    gradelist2.clear()

    #copies cached grade data into gradelist1
    with open('gradelist.json', 'w+') as f:
        json.dump(gradelist1, f)

    #iterates through all grade data found
    for grade in grades:
        gradeinfo = grade.text.split()[-1] #split removes the letter grade from the string
        gradelist2.append(gradeinfo)
    #gradelist2.append(runamount)
    
    #iterates through all classname data found
    classlist.clear()
    for classname in classnames:
        classinfo = classname.text.split('\n', 1)[0] #removes information after the new line
        classlist.append(classinfo)

    driver.quit()

#returns your grade/class
def statementReturner():
    statement = [f'For {c.rstrip()}, you have a {g}.\n' for c, g in zip(classlist, gradelist2)]
    comma_delete = ','.join(statement)
    return comma_delete.replace(',', '')

#gets the difference of grades from x-1 and x times running.
def gradeChangeShow():
    gradelist1_change = [x for x in gradelist1 if x != '--']
    gradelist2_change = [x for x in gradelist2 if x != '--']
    difference = []
    for i in range(len(gradelist1)): #gradelist1 here can be gradelist 2 as well.
        difference = ["{:.1f}".format(float(a) - float(b)) for a, b in zip(gradelist2_change, gradelist1_change)]
    difference = [x for x in difference if x != '0']
    statement = [f'\n{c.rstrip()}: {d}'
               for c, d in zip(classlist, difference) if float(d) != 0]
    comma_delete = ','.join(statement)
    if difference:
        return comma_delete.replace(',', '')
    else:
        return ('\nNo grade changes.')