#!/usr/bin/env python
# coding: utf-8

import os
import time
import random
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(30)  # seconds

#What will be searched
search_parameter = "Nokia"

#Time waiting for page
waiting_for_page = random.randint(4,9)

#Time per user
time_per_user = random.randint(4,9)

driver.get("https://www.linkedin.com/")

# Action 1 : Login.
# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)

# Action 2 : Go to leads page
driver.find_element_by_class_name("nav-item__wormhole").click()# seconds
driver.switch_to.window(driver.window_handles[1])
time.sleep(waiting_for_page)
# Search Education
driver.find_element_by_id("global-typeahead-search-input").send_keys(search_parameter)
time.sleep(2)

try:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[2].click()
except:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[1].click()


time.sleep(waiting_for_page)

pages = int(
    driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
        "…")[-1])


driver.implicitly_wait(10)  # seconds
for i in range(pages):

    # Action 3: Go trough the page users and check if they can be messaged
    all_people_in_page = driver.find_elements_by_class_name("pv5")

    for people in all_people_in_page:

        time.sleep(time_per_user)

        aux = 0
        while aux == 0:
            buttons = people.find_elements_by_tag_name("button")

            try:
                for b in range(len(buttons)):
                    buttons = people.find_elements_by_tag_name("button")

                    # Action 4 : Find Save Button
                    # Change to "Save" in your script
                    if "Save" in buttons[b].text:
                        buttons[b].click()
                        time.sleep(1)

                        lists = people.find_element_by_class_name("save-to-list-dropdown").find_elements_by_tag_name("li")[2].find_elements_by_tag_name("li")

                        for ls in lists:
                            # Action 5: Save contact ina lide list . You have to change this name for your desired list
                            if "TestList" in ls.text:

                                ls.click()

                                time.sleep(1)

                                try:
                                    bs = driver.find_element_by_class_name("lead-cta-form__save-without-company")
                                    bs.click()
                                    break
                                except Exception as e:
                                    break

                            time.sleep(1)
                        # Action 6 : Send Massage .Change to "Message"
                    if "Message" in buttons[b].text:
                        buttons[b].click()

                        time.sleep(2)

                        # Send message
                        # Subject
                        subject = "I love nokia."

                        # Message
                        message = "I have a plan. \nTarget those people who still use Nokia 1100 ."

                        # Attachment

                        try:
                            driver.find_element_by_class_name("compose-form__subject-field").send_keys(subject)
                            time.sleep(1)

                            driver.find_element_by_class_name("compose-form__message-field").send_keys(message)
                            time.sleep(3)

                            # Click send
                            main_aux = driver.find_element_by_class_name("pr3")
                            main_aux.find_element_by_class_name("ml4").click()
                        except:
                            pass

                        aux = 1
            except:
                continue




    driver.find_element_by_class_name("search-results__pagination-next-button").click()
    time.sleep(waiting_for_page)