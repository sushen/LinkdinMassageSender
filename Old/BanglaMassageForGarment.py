#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time
import random
import os



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(60)  # seconds



#Change the messages as you wish, one of them will be randomly picked
subjects = [
    "আপনার মতামত চাই",
    "আপনার পরামর্শ চাই",
    "আরও ভালো করতে সহযোগিতা চাই ",
    "আপনার পার্টনারশিপ চাই",
    "আইডিয়া সেল করতে চাই "
]


#Change the messages as you wish, one of them will be randomly picked
messages = [
    "আপনার পরামর্শ চাই, আরও ভালো করতে সহযোগিতা চাই এবং আইডিয়া সেল করতে চাই । \n \nhttps://www.sushenbiswas.com/course/business-growth/ ",
    "আমি এই টিউটরিয়াল সিরিজে আমার কাজের ধরনে বলেছি , আরও ভালো করতে সহযোগিতা চাই \n \nhttps://www.sushenbiswas.com/course/business-growth/",
    "আইডিয়া সেল করতে চাই , কি ভাবে ব্যাবসা করবো তারও একটা রুপরেখা তৈরী করেছি । \n \nhttps://www.sushenbiswas.com/course/business-growth/",
    "ভয় হিন শুরু মানেই ভাল মানুষের সাথে শুরু ।  \n \nhttps://www.sushenbiswas.com/course/business-growth/"
]



#What will be searched
search_parameter = "Garment Bangladesh"

#Time waiting for page
waiting_for_page = random.randint(9,15)

#Time per user
time_per_user = random.randint(4,9)

driver.get("https://www.linkedin.com/")

# Login

'''f = open("user.txt", "r")
data = f.read()
username = str(data).split("\n")[0]
password = str(data).split("\n")[1]
'''

# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)

# Go to leads page
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

    # Go trough the page users and check if they can be messaged
    all_people_in_page = driver.find_elements_by_class_name("pv5")

    for people in all_people_in_page:

        time.sleep(time_per_user)

        aux = 0
        while aux == 0:
            buttons = people.find_elements_by_tag_name("button")

            try:
                for b in range(len(buttons)):
                    buttons = people.find_elements_by_tag_name("button")

                    # Change to "Save" in your script
                    if "Save" in buttons[b].text:
                        buttons[b].click()
                        time.sleep(1)

                        lists = people.find_element_by_class_name("save-to-list-dropdown").find_elements_by_tag_name("li")[2].find_elements_by_tag_name("li")

                        for ls in lists:
                            # You have to change this name for your desired list
                            if "Garment Bangladesh" in ls.text:

                                ls.click()

                                time.sleep(1)

                                try:
                                    bs = driver.find_element_by_class_name("lead-cta-form__save-without-company")
                                    bs.click()
                                    break
                                except Exception as e:
                                    break

                            time.sleep(1)
                        # Change to "Send message"
                    if "Message" in buttons[b].text:
                        buttons[b].click()

                        time.sleep(2)

                        
                        try:
                            driver.find_element_by_class_name("compose-form__subject-field").send_keys(random.choice(subjects))
                            time.sleep(1)

                            driver.find_element_by_class_name("compose-form__message-field").send_keys(random.choice(messages))
                            time.sleep(3)

                            # Click send
                            main_aux = driver.find_element_by_class_name("pr3")
                            main_aux.find_element_by_class_name("ml4").click()
                        except:
                            driver.find_element_by_class_name("message-overlay").find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                            time.sleep(1)

                        aux = 1

            except:
                continue
    driver.find_element_by_class_name("search-results__pagination-next-button").click()
    time.sleep(waiting_for_page)