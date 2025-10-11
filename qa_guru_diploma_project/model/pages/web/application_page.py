import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.utils import get_picture_path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
import time


class SettingsAppPage:

    def __init__(self, driver):
        self.driver = driver

    def open_settings_app(self):
        self.driver.get("https://stage.mesone.kz/settings/application")
        self.driver.implicitly_wait(15)

    @allure.step("Прямой переход на страницу настроек приложения")
    def open_settings_app_admin(self, browser, refresh_token_admin):

        self.open_settings_app()
        browser.add_cookie({"name": "refreshToken", "value": refresh_token_admin})
        self.open_settings_app()

    @allure.step("Загрузка Picture")
    def upload_picture(self, filename):
        file_path = get_picture_path(filename)
        self.driver.find_element(By.XPATH, '//input[@name="logo"]').send_keys(file_path)

    @allure.step("Удаление Picture")
    def delete_picture(self):
        icon_delete = self.driver.find_element(By.XPATH, '//*[@data-icon="delete"]')
        icon_delete.click()

    @allure.step("Клик Сохранить")
    def click_save_btn(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@aria-label="save"]')
        login_btn.click()
        time.sleep(1)

    @allure.step("Клик switch Логотип")
    def click_switch_logo(self, browser):
        switch_logo = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="ant-space-item"][1]//*[@role="switch"]')
            )
        )
        switch_logo.click()

    @allure.step("Клик switch Изображение")
    def click_switch_picture(self, browser):
        switch_picture = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[contains(@class, "ant-upload-wrapper")]/../..//button')
            )
        )
        switch_picture.click()

    @allure.step("Клик switch Текст")
    def click_switch_text(self):
        switch_text = self.driver.find_element(By.XPATH, '//*[contains(@role, "tablist")]'
                                                         '/../../..//*[@role="switch"]')
        switch_text.click()

    @allure.step("Клик switch Футер")
    def click_switch_footer(self):
        switch_footer = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-space")]'
                                                           '//*[@class="ant-space-item"][3]//*[@role="switch"]')
        switch_footer.click()

    @allure.step("Клик switch Язык")
    def click_switch_lang(self):
        switch_lang = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-flex")]'
                                                         '/div[2]//*[@role="switch"]')
        switch_lang.click()

    @allure.step("Выбор языка из списка")
    def select_lang(self, l1, l2, l3):

        select_list = self.driver.find_element(By.XPATH, '//*[@class="ant-select-selection-overflow"]')
        select_list.click()
        lang1 = self.driver.find_element(By.XPATH, f'//*[@title="{l1}"]')
        lang1.click()
        lang2 = self.driver.find_element(By.XPATH, f'//*[@title="{l2}"]')
        lang2.click()
        lang3 = self.driver.find_element(By.XPATH, f'//*[@title="{l3}"]')
        lang3.click()

    @allure.step("Выбор языка по умолчанию")
    def select_default_lang(self, lang):

        select_list = self.driver.find_element(By.XPATH, '(//div[contains(@class, "ant-select-selector")])[2]')
        select_list.click()

        lang1 = self.driver.find_element(By.XPATH, f'//div[@class="rc-virtual-list"]//*[@title="{lang}"]')
        lang1.click()

    @allure.step("Клик таб локаль")
    def click_tab_locale(self, locale):
        tab_en = self.driver.find_element(By.XPATH, f'//*[@data-node-key="{locale}"]/div')
        tab_en.click()

    @allure.step("Ввод текста в поле Основной")
    def input_text_field_main(self, locale, text):
        field_main = self.driver.find_element(By.XPATH, f'(//*[contains(@id, "panel-{locale}")]'
                                                        '//*[@class="ant-space-item"])[1]//input')
        field_main.send_keys(text)

    @allure.step("Ввод текста в поле Дополнительный")
    def input_text_field_additional(self, locale, text):
        field_additional = self.driver.find_element(By.XPATH, f'(//*[contains(@id, "panel-{locale}")]'
                                                              '//*[@class="ant-space-item"])[2]//input')
        field_additional.send_keys(text)

    @allure.step("Клик таб RU")
    def click_tab_ru(self):
        tab_en = self.driver.find_element(By.XPATH, '//*[@data-node-key="ru-RU"]/div')
        tab_en.click()

    @allure.step("Клик кнопке Темная")
    def click_btn_dark(self, browser):
        btn_dark = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[contains(@class, "ant-radio-group-outline")]'
                                   '//*[@value="dark"]/../..')
            )
        )
        btn_dark.click()

    @allure.step("Клик кнопке Тема")
    def click_btn_theme(self, theme):
        btn_theme = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-radio-group-solid")]'
                                                       f'//*[text()="{theme}"]/..')
        btn_theme.click()

    @allure.step("Получение иконки поля загрузки лого")
    def get_attribute_picture(self):
        input_picture = self.driver.find_element(By.XPATH,
                                                 '//*[@class="ant-upload ant-upload-select"]//span[@role="img"]')
        return input_picture.get_attribute("aria-label")

    @allure.step("Получение статуса switch Изображение")
    def get_status_switch_picture(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-upload-wrapper")]/../..//button')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Логотип")
    def get_status_switch_logo(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[@class="ant-space-item"][1]//*[@role="switch"]')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Логотип")
    def get_status_switch_lang(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-flex")]'
                                                            '/div[2]//*[@role="switch"]')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение текста выбранного tab")
    def get_selected_text_tab(self):
        tab = self.driver.find_element(By.XPATH, '//*[@role="tab" and @aria-selected="true"]/..')
        return tab.get_attribute("data-node-key")

    @allure.step("Получение текста поле Основной")
    def get_text_field_main(self, locale):
        field_main = self.driver.find_element(By.XPATH, f'(//*[contains(@id, "panel-{locale}")]'
                                                        '//*[@class="ant-space-item"])[1]//input')
        return field_main.get_attribute("value")

    @allure.step("Получение текста поле Дополнительный")
    def get_text_field_additional(self, locale):
        field_additional = self.driver.find_element(By.XPATH, f'(//*[contains(@id, "panel-{locale}")]'
                                                              '//*[@class="ant-space-item"])[2]//input')
        return field_additional.get_attribute("value")

    @allure.step("Получение текущего стиля приложения")
    def get_current_style_app(self):
        style_app = self.driver.find_element(By.XPATH, '//*[@id="footer"]/..')
        return style_app.get_attribute("themestyle")

    @allure.step("Получение текущей темы приложения")
    def get_current_theme_app(self):
        style_app = self.driver.find_element(By.XPATH,
                                             '//*[contains(@class, "ant-radio-group-solid")]//input[@checked]')
        return style_app.get_attribute("value")

    @allure.step("Поиск футера")
    def get_status_footer(self):
        try:
            self.driver.find_element(By.ID, "footer")
            return True
        except NoSuchElementException:
            return False

    @allure.step("Поиск лого в хэдере")
    def get_status_logo(self):
        try:
            self.driver.find_element(By.XPATH, '//header//img[@alt="MESone"]')
            return True
        except NoSuchElementException:
            return False

    @allure.step("Получение количества выбранных языков")
    def get_quantity_langs_in_lang(self):
        quantity_langs = self.driver.find_elements(By.XPATH,
                                                   '//*[@class="ant-select-selection-overflow"]'
                                                   '/div[@class="ant-select-selection-overflow-item"]')
        return len(quantity_langs)

    @allure.step("Получение количества включенных локалей")
    def get_quantity_langs_in_instance_editor(self):
        quantity_langs = self.driver.find_elements(By.XPATH, '//*[@data-node-key]')
        return len(quantity_langs)

    @allure.step("Получение выбранного языка по умолчанию")
    def get_selected_default_lang(self):
        default_lang = self.driver.find_element(By.XPATH, '//span[@class="ant-select-selection-search"]'
                                                          '/following-sibling::span')
        return default_lang.get_attribute("title")

    @allure.step("Клик collapse Функции времени")
    def uncover_time_functions_collapse(self):
        collapse_time_func = self.driver.find_element(By.XPATH,
                                                      '//div[contains(@class, "ant-collapse-icon-position-start")]'
                                                      '/div[2]')
        collapse_time_func.click()

    @allure.step("Клик switch Диапазон")
    def click_switch_range(self):
        switch_range = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                          '/div[2]//button[@role="switch"])[1]')
        switch_range.click()

    @allure.step("Клик switch Видимость(Диапазон)")
    def click_switch_range_visibility(self):
        switch_range_visibility = self.driver.find_element(By.XPATH,
                                                           '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                           '/div[2]//button[@role="switch"])[2]')
        switch_range_visibility.click()

    @allure.step("Выбор пресета")
    def select_preset(self, text):
        presets = self.driver.find_element(By.ID, 'presets')
        presets.send_keys(text)
        presets.send_keys(Keys.RETURN)

    @allure.step("Клик btn Абсолютное")
    def click_btn_absolute(self):
        btn_absolute = self.driver.find_element(By.XPATH, '//*[@id="default_mode"]/label[1]')
        btn_absolute.click()

    @allure.step("Клик btn Относительное")
    def click_btn_relative(self):
        btn_relative = self.driver.find_element(By.XPATH, '//*[@id="default_mode"]/label[2]')
        btn_relative.click()

    @allure.step("Выбор даты и времени начала")
    def select_time_function_left_date_and_time(self, **args):
        self.driver.find_element(By.XPATH, '//*[@date-range="start"]').click()
        self.driver.find_element(By.XPATH, '//button[@aria-label="month panel"]').click()
        self.driver.find_element(By.XPATH, f'//td[contains(@title, "{args['month']}")]').click()
        self.driver.find_element(By.XPATH,
                                 f'//td[contains(@title, "{args['day']}") and contains(@class, "view")]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="hour"]//*[@data-value="{args['hour']}"]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="minute"]//*[@data-value="{args["minute"]}"]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="second"]//*[@data-value="{args["second"]}"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="ant-picker-ok"]/button').click()

    @allure.step("Выбор даты и времени окончания")
    def select_time_function_right_date_and_time(self, **args):
        self.driver.find_element(By.XPATH, '//*[@date-range="end"]').click()
        self.driver.find_element(By.XPATH, '//button[@aria-label="month panel"]').click()
        self.driver.find_element(By.XPATH, f'//td[contains(@title, "{args['month']}")]').click()
        self.driver.find_element(By.XPATH,
                                 f'//td[contains(@title, "{args['day']}") and contains(@class, "view")]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="hour"]//*[@data-value="{args['hour']}"]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="minute"]//*[@data-value="{args['minute']}"]').click()
        self.driver.find_element(By.XPATH, f'//ul[@data-type="second"]//*[@data-value="{args['second']}"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="ant-picker-ok"]/button').click()

    @allure.step("Получение статуса switch Диапазон")
    def get_status_switch_range(self):
        switch_range = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                          '/div[2]//button[@role="switch"])[1]')
        return switch_range.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Видимость")
    def get_status_switch_visibility(self):
        switch_range_visibility = self.driver.find_element(By.XPATH,
                                                           '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                           '/div[2]//button[@role="switch"])[2]')
        return switch_range_visibility.get_attribute("aria-checked")

    @allure.step("Получение выбранного пресета")
    def get_selected_preset(self, text):
        selected_preset = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-item")][2]'
                                                             f'//*[@class="ant-select-selector"])[1]//*[@title="{text}"]')
        return selected_preset.get_attribute("title")

    @allure.step("Получение выбранного Значения по умолчанию")
    def get_text_selected_default_value(self):
        return self.driver.find_element(By.XPATH, '//*[@id="default_mode"]'
                                                  '/label[contains(@class, "checked")]/span[2]').text

    @allure.step("Получение значения старт диапазона")
    def get_value_range_start(self):
        value_range_start = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-item")])[2]'
                                                               '//*[@date-range="start"]')
        return value_range_start.get_attribute("value")

    @allure.step("Получение значения окончание диапазона")
    def get_value_range_end(self):
        value_range_end = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-item")])[2]'
                                                             '//*[@date-range="end"]')
        return value_range_end.get_attribute("value")

    @allure.step("Выбор пресета по умолчанию(Диапазон)")
    def select_default_preset(self, preset):
        field_default_presets = self.driver.find_element(By.ID, 'default_preset')
        field_default_presets.click()
        select_preset = self.driver.find_element(By.XPATH, f'//*[@title="{preset}"]')
        select_preset.click()

    @allure.step("Получение выбранного пресета по умолчанию")
    def get_selected_default_preset(self):
        selected_preset = self.driver.find_element(By.XPATH, '//*[@id="default_preset"]/../following-sibling::span[1]')
        return selected_preset.get_attribute("title")

    @allure.step("Клик switch Обновление")
    def click_switch_updater(self):
        switch_updater = self.driver.find_element(By.XPATH, '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                            '/div[2]//button[@role="switch"])[3]')
        switch_updater.click()

    @allure.step("Клик switch Видимость(Updater)")
    def click_switch_updater_visibility(self):
        switch_updater_visibility = self.driver.find_element(By.XPATH,
                                                             '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                             '/div[2]//button[@role="switch"])[4]')
        switch_updater_visibility.click()

    @allure.step("Выбор пресета по умолчанию(Updater)")
    def select_default_preset_updater(self, preset):
        default_preset_updater = self.driver.find_element(By.XPATH, '//*[@id="default"]/../..')
        default_preset_updater.click()
        select_preset = self.driver.find_element(By.XPATH, f'//*[@title="{preset}"]')
        select_preset.click()

    @allure.step("Получение статуса switch Обновление")
    def get_status_switch_updater(self):
        get_status_switch_updater = self.driver.find_element(By.XPATH,
                                                             '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                             '/div[2]//button[@role="switch"])[3]')
        return get_status_switch_updater.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Видимость(Updater)")
    def get_status_switch_visibility_updater(self):
        switch_visibility_updater = self.driver.find_element(By.XPATH,
                                                             '(//*[contains(@class, "ant-collapse-icon-position-start")]'
                                                             '/div[2]//button[@role="switch"])[4]')
        return switch_visibility_updater.get_attribute("aria-checked")

    @allure.step("Получение выбранного пресета Обновление")
    def get_selected_preset_updater(self):
        selected_preset = self.driver.find_element(By.XPATH, '//*[@id="default"]/../following-sibling::span[1]')
        return selected_preset.get_attribute("title")
