import os

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.path_utils import get_picture_path



class UserLoginPage:


    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход страницу авторизации")
    def open_user_login_page(self):
        """Открытие страницы авторизации"""
        self.driver.get("https://stage.mesone.kz/user/login") #
        self.driver.implicitly_wait(10)
        #self.driver.execute_script("document.body.style.zoom = '60%'")

    @allure.step("Ввод логина")
    def filling_login(self, username):
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.send_keys(username)

    @allure.step("Ввод пароля")
    def filling_password(self, password):
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

    @allure.step("Клик Вход")
    def click_login_btn(self):
        login_btn = self.driver.find_element(By.CLASS_NAME, 'anticon-login')
        login_btn.click()

        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located(
        #         locator=(By.CLASS_NAME, 'ant-pro-global-header')
        #     )
        # )