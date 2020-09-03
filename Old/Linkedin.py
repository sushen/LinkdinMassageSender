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
    "Subject 1",
]


#Change the messages as you wish, one of them will be randomly picked
messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Message 4",
    "Message 5"
]



#What will be searched
search_parameter = "Education"

#Time waiting for page
waiting_for_page = 15

#Time per user
time_per_user = 4

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
driver.find_element_by_class_name("global-nav__content").find_elements_by_tag_name("a")[-1].click()
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

input("Enter something to continue the script : \n")


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
                    if "Salvar" in buttons[b].text:
                        buttons[b].click()
                        time.sleep(1)

                        lists = people.find_element_by_class_name("save-to-list-dropdown").find_elements_by_tag_name("li")[2].find_elements_by_tag_name("li")

                        for ls in lists:
                            # You have to change this name for your desired list
                            if "Lista de leads de Pedro" in ls.text:

                                ls.click()

                                time.sleep(1)

                                try:
                                    bs = driver.find_element_by_class_name("lead-cta-form__save-without-company")
                                    bs.click()
                                    break
                                except Exception as e:
                                    break

                            time.sleep(1)

                aux = 1
            except:
                aux = 1
                continue




    driver.find_element_by_class_name("search-results__pagination-next-button").click()
    time.sleep(waiting_for_page)