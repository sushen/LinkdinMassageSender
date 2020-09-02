#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time
import random
import os



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


#Message to send when connecting
message_to_connect = [
    "আপনার সাথে যোগাযোগ করতে চাই ।",
    "আপনার এপয়েন্টমেন্ট চাই। বিষয় ইনভেষ্টমেন্ট",
    "মেন্টরের মত আপনার পরামর্শ চাই ।"
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

'''f = open("user.txt", "r")
data = f.read()
username = str(data).split("\n")[0]
password = str(data).split("\n")[1]'''


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


    for p in range(len(people)):
        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]
        people[p].find_elements_by_tag_name("button")[-1].click()
        time.sleep(2)

        menu = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")
        need_connect = False

        for m in range(len(menu)):
            driver.implicitly_wait(3)
            driver.find_element_by_id("content-main").click()
            time.sleep(1)
            people[p].find_elements_by_tag_name("button")[-1].click()

            try:
                aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")
            except:
                people[p].find_elements_by_tag_name("button")[-1].click()
                time.sleep(1)
                aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")


            time.sleep(1)

            if m == 2:
                driver.find_element_by_id("content-main").click()

                break

            #Change to "Send Message"
            elif "Message" in aux[m].text:
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



            # Change to "connect"
            elif "Connect" in aux[m].text and need_connect:
                aux[m].click()
                time.sleep(1)

                driver.find_element_by_id("connect-cta-form__invitation").send_keys(random.choice(message_to_connect))
                time.sleep(2)

                driver.find_element_by_class_name("connect-cta-form__send").click()

                did_everything = True
                break

            time.sleep(3)
            driver.find_element_by_id("content-main").click()

        driver.find_element_by_id("content-main").click()

    try:
        driver.find_element_by_class_name("search-results__pagination-next-button").click()
    except:
        pass
    time.sleep(10)
