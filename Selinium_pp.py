from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

url1 = "qqq"
url2 = "www"
sleep_time = 5
sleep_time_2 = 3
# team_locator = "2021-05-24_team_1"
n = int(input("Enter number of days:"))
i=1

while i < n:
    print(i)
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait_variable = W(driver,sleep_time)
    driver.get(url1)
    driver.find_element_by_name("user").send_keys("username")
    driver.find_element_by_name("pass").send_keys("safdsaf")
    time.sleep(sleep_time)
    driver.find_element_by_name("login").send_keys(Keys.ENTER)
    time.sleep(sleep_time)
    driver.get(url2)
    time.sleep(sleep_time)


    val1 = driver.find_element_by_id("entry_date")
    val = val1.get_attribute("data-date")

    #Select team
    team= val+"_team_1"
    team_select = driver.find_element_by_id(team)
    drop = Select(team_select)
    drop.select_by_visible_text("Non Functional regression")
    time.sleep(sleep_time_2)

    #Select Task
    task= val+"_task_1"
    task_select = driver.find_element_by_id(task)
    drop = Select(task_select)
    drop.select_by_visible_text("Whitebox")
    time.sleep(sleep_time_2)

    #Enter hours
    hours=val+"_execution-hours_1"
    driver.find_element_by_id(hours).send_keys("8")

    #Select Taskid
    taskid=val+"_task-ids_1"
    task_select = driver.find_element_by_id(taskid)
    drop = Select(task_select)
    drop.select_by_visible_text("Functional Automation - Execution & Analysis")
    time.sleep(sleep_time_2)

    #Enter count
    hours=val+"_count_1"
    driver.find_element_by_id(hours).send_keys("1")
    button = val+"_update-entry"
    driver.find_element_by_id(button).send_keys(Keys.ENTER)
    i=i+1


    driver.close()
