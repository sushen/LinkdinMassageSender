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
    "কোর্সটি সেল করতে চাই "
]


#Change the messages as you wish, one of them will be randomly picked
messages = [
    "বাংলা কোড মানে বাংলায় লেখা কোড।বাংলা পাইথন কোড মানে পাইথনের সিনট্যাক্স ব্যাবহার করেছি বাকিটা বাংলায় লিখেছি । \n \nhttps://sushenbiswas.com/course/learn-python-together/ ",
    "আমি এই টিউটরিয়াল সিরিজে বাংলা পাইথন কোড লিখেছি,  গিটহাবে সেই কোড কিভাবে সারাবিশ্বের কাছে উন্মুক্ত করা যায় দেখিয়েছি, ব্লকচেইন সমন্ধে সেটার মধ্যে বলেছি।\n \nhttps://sushenbiswas.com/course/learn-python-together/",
    "শুরুটা বাংলায় হলে, নিজের ভাষায় হলে দারুন শুরু হয় । ভয় হিন শুরু মানেই নিজের ভাষাতে শুরু । \n \nhttps://sushenbiswas.com/course/learn-python-together/",
    "ভয় হিন শুরু মানেই নিজের ভাষাতে শুরু ।  \n \nhttps://sushenbiswas.com/course/learn-python-together/"
]


#Message to send when connecting
message_to_connect = "আপনার সাথে যোগাযোগ করতে চাই ।"



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(5)  # seconds

#What will be searched

#Time waiting for page
waiting_for_page = 15



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


#Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6703506863146840064?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
people = people[1:]


for p in range(len(people)):
    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    people[p].find_elements_by_tag_name("button")[-1].click()

    menu = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")
    need_connect = False

    for m in range(len(menu)):

        time.sleep(1)

        try:
            #Change to "Send Message"
            if "Message" in menu[m].text:
                menu[m].click()

                time.sleep(3)

                try:

                    driver.find_element_by_class_name("compose-form__subject-field").send_keys(random.choice(subjects))
                    time.sleep(1)

                    driver.find_element_by_class_name("compose-form__message-field").send_keys(random.choice(messages))
                    time.sleep(3)


                    # Click send
                    main_aux = driver.find_element_by_class_name("pr3")
                    main_aux.find_element_by_class_name("ml4").click()

                    time.sleep(2)
                    break
                except:
                    driver.find_element_by_class_name("message-overlay").find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                    time.sleep(1)
                    need_connect = True


                people[p].find_elements_by_tag_name("button")[-1].click()

                menu = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")



            # Change to "connect"
            elif "Connect" in menu[m].text and need_connect == True:
                menu[m].click()
                time.sleep(1)

                driver.find_element_by_id("connect-cta-form__invitation").send_keys(message_to_connect)
                time.sleep(2)

                driver.find_element_by_class_name("connect-cta-form__send").click()
                time.sleep(2)


                break

            time.sleep(2)
        except:
            pass

        time.sleep(3)

