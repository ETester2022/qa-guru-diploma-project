import os

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.path_utils import get_picture_path



class PegistrationStudentPage12:


    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на форму студента")
    def open_main_page(self):
        """Заполнение формы студента"""
        self.driver.get("https://demoqa.com/automation-practice-form") #https://stage.mesone.kz/user/login
        self.driver.implicitly_wait(10)
        self.driver.execute_script("document.body.style.zoom = '60%'")

    @allure.step("Заполнение First Name")
    def fill_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(f"{first_name}")

    @allure.step("Заполнение Last Name")
    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID, "lastName").send_keys(f"{last_name}")

    @allure.step("Заполнение Email")
    def fill_user_email(self, user_email):
        self.driver.find_element(By.ID, "userEmail").send_keys(f"{user_email}")

    @allure.step("Выбор Gender=Male")
    def radio_btn_male(self):
        self.driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()

    @allure.step("Заполнение Mobile")
    def fill_phone(self, phone):
        self.driver.find_element(By.ID, "userNumber").send_keys(f"{phone}")

    @allure.step("Выбор Date of Birth")
    def select_date(self, date):
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        self.driver.find_element(By.XPATH, f'//div[contains(@aria-label, "{date}th")]').click()

    @allure.step("Заполнение Subjects")
    def fill_subject(self, subject):
        self.driver.find_element(By.ID, "subjectsInput").send_keys(f"{subject}")

    @allure.step("Выбор Hobbies=Sports")
    def radio_btn_sports(self):
        self.driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()


    @allure.step("Загрузка Picture")
    def upload_picture(self, filename):
        file_path = get_picture_path(filename)
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    # @allure.step("Загрузка Picture")
    # def upload_picture(self, picture):
    #     file_path = os.path.abspath(f"{picture}")
    #     self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)



    @allure.step("Заполнение Current Address")
    def fill_adress(self, adress):
         self.driver.find_element(By.ID, "currentAddress").send_keys(f"{adress}")

    @allure.step("Выбор State")
    def select_state(self, state):
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{state}"]').click()

    @allure.step("Выбор City")
    def select_city(self, city):
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{city}"]').click()

    @allure.step("Клик Submit")
    def submit_btn(self):
        self.driver.find_element(By.ID, "submit").click()

    @allure.step("Проверка соответствия заголовка")
    def should_be_header(self, text_header):
        # Ожидание появления модального окна
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="modal-content"]')
            )
        )
        # Проверка отображеня заголовка в модальном окне
        element = self.driver.find_element(By.CLASS_NAME, "modal-header")
        assert element.text == text_header

    @allure.step("Проверка соответствия отображаемых данных в полях")
    def should_be_result(self, expected_result):
        # Сравнение полученных и ожидаемых value в соответствии с их Label
        rows = self.driver.find_elements(By.XPATH, '//tbody//tr')
        list_labels = []
        list_values = []

        for row in rows:
            label = row.find_element(By.XPATH, './td[1]').text
            value = row.find_element(By.XPATH, './td[2]').text
            list_labels.append(label)
            list_values.append(value)

        actual_res = dict(zip(list_labels, list_values))

        assert actual_res["Student Name"] == expected_result[0], \
            f"Значение поля 'Student Name': ОР '{expected_result[0]}', ФР '{actual_res["Student Name"]}'"
        assert actual_res["Student Email"] == expected_result[1], \
            f"Значение поля 'Student Email': ОР '{expected_result[1]}', ФР '{actual_res["Student Email"]}'"
        assert actual_res["Gender"] == expected_result[2], \
            f"Значение поля 'Gender': ОР '{expected_result[2]}', ФР '{actual_res["Gender"]}'"
        assert actual_res["Mobile"] == expected_result[3], \
            f"Значение поля 'Mobile': ОР '{expected_result[3]}', ФР '{actual_res["Mobile"]}'"
        assert actual_res["Date of Birth"] == expected_result[4], \
            f"Значение поля 'Date of Birth': ОР '{expected_result[4]}', ФР '{actual_res["Date of Birth"]}'"
        assert actual_res["Picture"] == expected_result[5], \
            f"Значение поля 'Picture': ОР '{expected_result[5]}', ФР '{actual_res["Picture"]}'"
        assert actual_res["Hobbies"] == expected_result[7], \
            f"Значение поля 'Hobbies': ОР '{expected_result[7]}', ФР '{actual_res["Hobbies"]}'"
        assert actual_res["Address"] == expected_result[8], \
            f"Значение поля 'Address': ОР '{expected_result[8]}', ФР '{actual_res["Address"]}'"
        assert actual_res["State and City"] == expected_result[9], \
            f"Значение поля 'State and City': ОР '{expected_result[9]}', ФР '{actual_res["State and City"]}'"

        # assert actual_res["Subjects"] == expected_result[6], \
        #     f"Значение поля 'Student Name': ОР '{expected_result[6]}', ФР '{actual_res["Subjects"]}'"

















    #
    # @allure.step("Переход на главную страницу github")
    # def open_main_page(self):
    #     self.driver.get("https://github.com")
    #     self.driver.implicitly_wait(10)
    #
    # @allure.step("Переход в раздел Issues")
    # def open_issues_page(self, repo):
    #     self.driver.find_element(By.XPATH, "//qbsearch-input").click()
    #     self.driver.find_element(By.ID, "query-builder-test").send_keys(repo)
    #     self.driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
    #     WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Issues']"))
    #         )
    #     self.driver.find_element(By.XPATH, "//span[text()='Issues']").click()
    #
    # @allure.step("Проверка отображения issue #199")
    # def is_displayed(self, number):
    #     try:
    #         element = WebDriverWait(self.driver, 5).until(
    #                 EC.visibility_of_element_located(
    #                     (By.XPATH, f"//*[text()='#' and text()='{number}']")
    #                 )
    #             )
    #         assert bool(element) is True
    #     except TimeoutException:
    #         raise AssertionError("Элемент не найден!")