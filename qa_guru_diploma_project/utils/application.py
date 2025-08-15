from qa_guru_diploma_project.model.pages.web.user_login_page import UserLoginPage
from qa_guru_diploma_project.model.pages.web.application_page import SettingsAppPage


class Application:
    def __init__(self, browser):
        self.browser = browser
        self.login_page = UserLoginPage(browser)
        self.application_page = SettingsAppPage(browser)
