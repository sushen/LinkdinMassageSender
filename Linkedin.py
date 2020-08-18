#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(60)  # seconds

driver.get("https://www.linkedin.com/")

# Login
'''
f = open("user.txt", "r")
data = f.read()

username = str(data).split("\n")[0]
password = str(data).split("\n")[1]'''


# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)
driver.implicitly_wait(60)  # seconds

driver.find_element_by_class_name("sign-in-form__submit-button").click()

# Go to leads page
driver.find_element_by_class_name("nav-item__wormhole").click()
driver.implicitly_wait(60)  # seconds
driver.switch_to.window(driver.window_handles[1])

# Search Education
driver.implicitly_wait(60)  # seconds

driver.find_element_by_id("global-typeahead-search-input").send_keys("Education")
time.sleep(1)
try:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[2].click()
except:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[1].click()

pages = int(
    driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
        "…")[-1])

time.sleep(3)

pages = int(
    driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
        "…")[-1])

for i in range(pages):

    # Go trough the page users and check if they can be messaged
    all_people_in_page = driver.find_elements_by_class_name("pv5")

    for people in all_people_in_page:

        time.sleep(3)

        buttons = people.find_elements_by_tag_name("button")

        for b in buttons:

            # Change to "Send message"
            if "Enviar mensagem" in b.text:
                b.click()

                time.sleep(2)

                # Send message
                # Subject
                subject = "I"

                # Message
                message = "I"

                driver.find_element_by_class_name("compose-form__subject-field").send_keys(subject)
                time.sleep(1)

                driver.find_element_by_class_name("compose-form__message-field").send_keys(message)
                time.sleep(4)

                # Click send
                main_aux = driver.find_element_by_class_name("pr3")
                main_aux.find_element_by_class_name("ml4").click()

            # Change to "Save" in your script
            if "Salvar" in b.text:
                b.click()
                time.sleep(2)

                lists = people.find_element_by_class_name("save-to-list-dropdown").find_elements_by_tag_name("li")

                for ls in lists:

                    # You have to change this name for your desired list
                    if "Lista de leads de Pedro" in ls.text:
                        ls.click()

                        time.sleep(1)

                        try:
                            driver.find_element_by_class_name("lead-cta-form__save-without-company").click()
                            break
                        except:
                            break


    driver.find_element_by_class_name("search-results__pagination-next-button").click()
