#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time
import os

# Start Browser
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.linkedin.com/")
time.sleep(4)

# Login part -> Reads data from user.txt and sends it to the website
# # f = open("user.py", "r")
# # data = f.read()
# #
# # username = str(data).split("\n")[0]
# # password = str(data).split("\n")[1]

# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)
driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(4)

# Go to leads page
driver.find_element_by_class_name("nav-item__wormhole").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])

# Search Education in the leads page
driver.find_element_by_id("global-typeahead-search-input").send_keys("Education")
time.sleep(1)
try:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[2].click()
except:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[1].click()

time.sleep(3)

# Find how many pages it has
pages = int(
    driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
        "…")[-1])

# Goes trhough all the pages
for i in range(pages):

    # Go trough each user in the page and check if they can be messaged
    all_people_in_page = driver.find_elements_by_class_name("pv5")

    for people in all_people_in_page:

        try:
            people.find_element_by_class_name("result-lockup__action-item").find_elements_by_tag_name("button")[
                1].click()
        except:
            continue

        time.sleep(2)

        options = people.find_elements_by_tag_name("ul")[-1].find_elements_by_tag_name("li")

        for option in options:

            # Replace "Enviar Mensagem" for the equivalent in your language eg. "Send Message"
            if "Send Message" in option.text:
                option.click()
                time.sleep(2)

                # Send message
                # Subject
                subject = "Custom Subject"

                # Message
                message = "Custom Message"

                driver.find_element_by_class_name("compose-form__subject-field").send_keys(subject)
                time.sleep(1)

                driver.find_element_by_class_name("compose-form__message-field").send_keys(message)
                time.sleep(1)

                # Click send
                main_aux = driver.find_element_by_class_name("pr3")
                main_aux.find_element_by_class_name("ml4").click()

                time.sleep(3)
                # exit and go to another
                try:
                    main = driver.find_element_by_class_name("message-overlay")
                    header = main.find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                    time.sleep(5)
                except:
                    pass

                break

    driver.find_element_by_class_name("search-results__pagination-next-button").click()






