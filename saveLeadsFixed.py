#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("chromedriver", chrome_options=options)
driver.implicitly_wait(25)  # seconds

#What will be searched
search_parameter = "Education"

#Time waiting for page
waiting_for_page = 5

#Time per user
time_per_user = 2

driver.get("https://www.linkedin.com/")

# Login
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
driver.implicitly_wait(waiting_for_page)  # seconds
driver.find_element_by_id("global-typeahead-search-input").send_keys(search_parameter)
time.sleep(2)

try:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[2].click()
except:
    driver.find_elements_by_class_name("artdeco-button--tertiary")[1].click()


input("Enter something to continue the script : \n")

time.sleep(waiting_for_page)

pages = int(
    driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
        "…")[-1])


for i in range(pages):

    # Go trough the page users and check if they can be messaged
    all_people_in_page = driver.find_elements_by_class_name("pv5")

    for people in all_people_in_page:
        actions = ActionChains(driver)
        actions.move_to_element(people).perform()

        time.sleep(time_per_user)

        buttons = people.find_elements_by_tag_name("button")

        try:
            for b in range(len(buttons)):
                buttons = people.find_elements_by_tag_name("button")

                # Change to "Save" in your script
                if "Salvar" in buttons[b].text:
                    time.sleep(2)
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


        except Exception as e:
            print(e)
            pass




    driver.find_element_by_class_name("search-results__pagination-next-button").click()
    time.sleep(waiting_for_page)