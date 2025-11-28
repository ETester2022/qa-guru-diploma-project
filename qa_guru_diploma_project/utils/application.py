from qa_guru_diploma_project.model.pages.web.user_login_page import UserLoginPage
from qa_guru_diploma_project.model.pages.web.application_page import SettingsAppPage
from qa_guru_diploma_project.model.pages.web.tools_editor_page import SettingsToolsPage
from qa_guru_diploma_project.model.pages.web.crud_viewer.crud_viewer_page import CrudViewerPage

class Application:
    def __init__(self, browser):
        self.browser = browser
        self.login_page = UserLoginPage(browser)
        self.application_page = SettingsAppPage(browser)
        self.tools_editor_page = SettingsToolsPage(browser)
        self.crud_viewer_page = CrudViewerPage(browser)
