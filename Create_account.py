from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import tkinter as tk

import pandas as pd

data = pd.read_csv(r'self_information.csv')   
df = pd.DataFrame(data, columns=['', 'info'])
info = df['info'].to_list()

from time import sleep
def create_account(account, verify):
    try:

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(verify)
        sleep(5)
        
        actions = ActionChains(driver)
        
        acc = account
        input_email = driver.find_element(By.ID, "login_username")
        actions.move_to_element(input_email).send_keys(acc).perform()
        btn_continue = driver.find_element(By.ID, "login_password_continue")
        actions.move_to_element(btn_continue).click().perform()
        sleep(2)

        password = info[0]
        input_psw = driver.find_element(By.ID, "login_password")
        actions.move_to_element(input_psw).send_keys(password).perform()
        btn_login = driver.find_element(By.ID, "login_control_continue")
        actions.move_to_element(btn_login).click().perform()
        sleep(13)

        btn_getstart = driver.find_element(By.CSS_SELECTOR, '[data-qa="get-started-btn"]')
        actions.move_to_element(btn_getstart).click().perform()
        sleep(2)

        btn_skip1 = driver.find_element(By.CSS_SELECTOR, '[data-test="skip-button"]')
        actions.move_to_element(btn_skip1).click().perform()
        sleep(2)

        btn_skip2 = driver.find_element(By.CSS_SELECTOR, '[data-test="skip-button"]')
        actions.move_to_element(btn_skip2).click().perform()
        sleep(2)

        btn_skip3 = driver.find_element(By.CSS_SELECTOR, '[data-test="skip-button"]')
        actions.move_to_element(btn_skip3).click().perform()
        sleep(2)

        btn_upload_resume = driver.find_element(By.CSS_SELECTOR, '[data-qa="resume-upload-btn-mobile"]')
        actions.move_to_element(btn_upload_resume).click().perform()
        sleep(1)

        resume_doc = info[1]
        input_resume = driver.find_element(By.CSS_SELECTOR, '[type="file"]')
        input_resume.send_keys(resume_doc)
        sleep(7)

        btn_upload_continue = driver.find_element(By.CSS_SELECTOR, '[data-qa="resume-upload-continue-btn"]')
        actions.move_to_element(btn_upload_continue).click().perform()
        sleep(1)

        role = info[2]
        input_role = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="title-label"]')
        input_role.clear()
        actions.move_to_element(input_role).click().send_keys(role)
        btn_next1 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next1).click().perform()
        sleep(1)

        btn_next2 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next2).click().perform()
        sleep(1)
        
        btn_next3 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next3).click().perform()
        sleep(1)

        btn_next4 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next4).click().perform()
        sleep(1)

        for x in range(1,16):
            btn_skills = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="token-container-label"]')
            btn_skill = btn_skills.find_elements(By.XPATH, "*[1]")
            actions.move_to_element(btn_skill[0]).click().perform()
        sleep(1)
        btn_next5 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next5).click().perform()
        sleep(1)

        btn_next5 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next5).click().perform()
        sleep(1)

        btn_web_dev = driver.find_element(By.CSS_SELECTOR, '[aria-label="3D Modeling & CAD"]')
        actions.move_to_element(btn_web_dev).click().perform()
        sleep(1)

        btn_next6 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next6).click().perform()
        sleep(1)

        rate = info[3]
        input_rate = driver.find_element(By.CSS_SELECTOR, '[data-test="currency-input"]')
        input_rate.send_keys(rate)
        btn_next7 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next7).click().perform()
        sleep(2)

        with open("date-of-birth.txt", "r") as file:
            file_contents = file.read()
        input_birth = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="date-of-birth-label"]')
        input_birth.send_keys(file_contents)
        sleep(1)

        self_img = info[4]
        btn_upload_img = driver.find_element(By.CSS_SELECTOR, '[data-qa="open-loader"]')
        actions.move_to_element(btn_upload_img).click().perform()
        sleep(1)
        input_img = driver.find_element(By.CSS_SELECTOR, '[type="file"]')
        input_img.send_keys(self_img)
        sleep(2)
        btn_next8 = driver.find_element(By.CSS_SELECTOR, '[data-qa="btn-save"]')
        actions.move_to_element(btn_next8).click().perform()
        sleep(5)

        street = info[5]
        input_street = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="street-label"]')
        input_street.send_keys(street)

        actions.move_to_element(input_street).click().perform()
        sleep(3)
        actions\
            .click()\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .perform()

        sleep(2)
        city = info[6]
        actions.send_keys(city)
        sleep(2)
        input_city = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="city-label"]')
        actions.move_to_element(input_city).click().perform()
        sleep(2)
        actions\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .perform()
        sleep(2)
        actions\
            .key_down(Keys.ENTER)\
            .key_up(Keys.ENTER)\
            .perform()
        sleep(1)

        post_code = info[7]
        input_post_code = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="postal-code-label"]')
        input_post_code.send_keys(post_code)
        phone = info[8]
        input_phone = driver.find_element(By.CSS_SELECTOR, '[type="tel"]')
        input_phone.send_keys(phone)
        btn_next9 = driver.find_element(By.CSS_SELECTOR, '[data-test="next-button"]')
        actions.move_to_element(btn_next9).click().perform()
        sleep(2)

        btn_submit = driver.find_element(By.CSS_SELECTOR, '[data-qa="submit-profile-top-btn"]')
        actions.move_to_element(btn_submit).click().perform()
        sleep(3)

        btn_browser = driver.find_element(By.CSS_SELECTOR, '.air3-btn-primary')
        actions.move_to_element(btn_browser).click().perform()
        sleep(3)

        btn_fee = driver.find_element(By.CSS_SELECTOR, '.up-checkbox-label')
        actions.move_to_element(btn_fee).click().perform()
        sleep(2)

        actions\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .key_down(Keys.TAB)\
            .key_up(Keys.TAB)\
            .key_down(Keys.SPACE)\
            .key_up(Keys.SPACE)\
            .perform()
        sleep(2)

        btn_msg = driver.find_element(By.CLASS_NAME, 'nav-messages')
        actions.move_to_element(btn_msg).click().perform()
        sleep(3)

        btn_point = driver.find_element(By.ID, 'dropdown-secondary-label-1')
        actions.move_to_element(btn_point).click().perform()
        sleep(1)

        actions\
            .key_down(Keys.ARROW_DOWN)\
            .key_up(Keys.ARROW_DOWN)\
            .key_down(Keys.ENTER)\
            .key_up(Keys.ENTER)\
            .perform()
        sleep(1)

        btn_noti = driver.find_element(By.CSS_SELECTOR, '.air3-dropdown-toggle-label')
        actions.move_to_element(btn_noti).click().perform()
        sleep(1)

        actions\
            .key_down(Keys.ARROW_UP)\
            .key_up(Keys.ARROW_UP)\
            .key_down(Keys.ENTER)\
            .key_up(Keys.ENTER)\
            .perform()
        sleep(1)

        btn_noti_save = driver.find_element(By.CSS_SELECTOR, '[data-ev-label="save_notification_settings"]')
        actions.move_to_element(btn_noti_save).click().perform()
        sleep(1)

        btn_work = driver.find_element(By.ID, 'caret-btn-findWorkHome')
        actions.move_to_element(btn_work).click().perform()
        sleep(1)

        driver.quit()
        print(acc)
    
    except Exception as error:
        print(error)

def start():
    
    data = pd.read_csv(r'accounts.csv')   
    df = pd.DataFrame(data, columns=['Account','Verify'])
    accounts = df['Account'].to_list()
    verify = df['Verify'].to_list()
    i = 0
    for account in accounts:
        create_account(account, verify[i])
        i+=1
    print("End")
 
main = tk.Tk()
main.geometry("700x350+600+300")
tk.Button(main,text ="Start", width=15, command = start,activebackground='green',justify='center').place(x=250, y=250)

main.title("Verify")
main.mainloop()