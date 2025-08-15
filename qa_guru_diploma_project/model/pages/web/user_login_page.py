import os
import allure
from selenium.webdriver.common.by import By


class UserLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_admin = os.getenv('LOGIN_ADMIN')
        self.password_admin = os.getenv('PASSWORD_ADMIN')
        self.login_user = os.getenv('LOGIN_USER')
        self.password_user = os.getenv('PASSWORD_USER')

    @allure.step("Переход страницу авторизации")
    def open_user_login_page(self):
        self.driver.get("https://stage.mesone.kz/user/login")
        self.driver.implicitly_wait(10)

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

    @allure.step("Получение текста из allert")
    def get_text_allert(self):
        self.driver.find_element(By.CLASS_NAME, 'ant-notification-notice-message').click()
        text_error = self.driver.find_element(By.CLASS_NAME, 'ant-notification-notice-message').text
        return text_error
