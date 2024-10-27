import time

from appium.webdriver import WebElement
from assertpy import assert_that
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from lesson_26.test_data import TestData


class TestFramesAlerts:
    def test_alert_frame1_with_valid_data(self, web_driver):
        web_driver.get(TestData.BESE_URL)

        frame1 = WebDriverWait(web_driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
        first_field = web_driver.find_element(By.XPATH, ".//input[@id = 'input1']")
        first_field.send_keys("Frame1_Secret")
        check_button = web_driver.find_element(By.XPATH,
                                               ".//input[@id='input1']/following-sibling::*[1]")
        check_button.click()
        time.sleep(1)
        alert = Alert(web_driver)
        (assert_that(alert.text, f"Ожидалось сообщение: 'Верифікація пройшла успішно!', но было: '{alert.text}'").
         is_equal_to("Верифікація пройшла успішно!"))
        alert.accept()


    def test_alert_frame1_with_invalid_data(self, web_driver):

        web_driver.get(TestData.BESE_URL)

        frame1 = WebDriverWait(web_driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
        first_field = web_driver.find_element(By.XPATH, ".//input[@id = 'input1']")
        first_field.send_keys("Frame1_Not_Secret")
        check_button = web_driver.find_element(By.XPATH,
                                               ".//input[@id='input1']/following-sibling::*[1]")
        check_button.click()
        time.sleep(1)
        alert = Alert(web_driver)
        (assert_that(alert.text, f"Ожидалось сообщение: 'Введено неправильний текст!', но было: '{alert.text}'").
         is_equal_to("Введено неправильний текст!"))
        alert.accept()


    def test_alert_frame2_with_valid_data(self,web_driver):
        web_driver.get(TestData.BESE_URL)

        frame2 = WebDriverWait(web_driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))

        second_field = web_driver.find_element(By.ID, "input2")
        second_field.send_keys("Frame2_Secret")
        check_button = web_driver.find_element(By.XPATH, ".//input[@id='input2']/following-sibling::*[1]")
        check_button.click()
        time.sleep(1)
        alert = Alert(web_driver)
        (assert_that(alert.text, f"Ожидалось сообщение: 'Верифікація пройшла успішно!', но было: '{alert.text}'").
         is_equal_to("Верифікація пройшла успішно!"))
        alert.accept()


    def test_alert_frame2_with_invalid_data(self, web_driver):
        web_driver.get(TestData.BESE_URL)

        WebDriverWait(web_driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))

        second_field = web_driver.find_element(By.ID, "input2")
        second_field.send_keys("Frame2_Not_Secret")
        check_button = web_driver.find_element(By.XPATH, ".//input[@id='input2']/following-sibling::*[1]")
        check_button.click()
        time.sleep(1)
        alert = Alert(web_driver)
        (assert_that(alert.text, f"Ожидалось сообщение: 'Введено неправильний текст!', но было: '{alert.text}'").
         is_equal_to("Введено неправильний текст!"))
        alert.accept()






