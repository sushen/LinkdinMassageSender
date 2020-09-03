#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains



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




options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(5)  # seconds

#What will be searched

#Time waiting for page
waiting_for_page = 10



driver.get("https://www.linkedin.com/")

# Login

f = open("user.txt", "r")
data = f.read()
username = str(data).split("\n")[0]
password = str(data).split("\n")[1]


# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')


driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
time.sleep(1)

driver.find_element_by_class_name("sign-in-form__submit-button").click()
time.sleep(waiting_for_page)


#Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6706420163950055424?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split("…")[-1])
except:
    pages = 1



for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    aux_count = 0
    for p in range(len(people)):

        driver.execute_script("window.scrollTo(0, {})".format(aux_count))

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        for m in range(len(aux)):

            # Change to "Message"
            if "Message" in aux[m].text:

                aux[m].click()

                time.sleep(2)

                try:

                    driver.find_element_by_class_name("compose-form__subject-field").send_keys(random.choice(subjects))
                    time.sleep(1)

                    driver.find_element_by_class_name("compose-form__message-field").send_keys(random.choice(messages))
                    time.sleep(2)

                    # Click send

                    main_aux = driver.find_element_by_class_name("pr3")
                    main_aux.find_element_by_class_name("ml4").click()

                    time.sleep(2)
                    break
                except:
                    driver.find_element_by_class_name("message-overlay").find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                    time.sleep(2)
                    need_connect = True

        time.sleep(1)

        driver.find_element_by_id("content-main").click()

        aux_count += 80

    try:
        driver.find_element_by_class_name("search-results__pagination-next-button").click()
    except:
        pass
    time.sleep(10)
