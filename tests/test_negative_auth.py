import pytest
from utils.vars import invalid_emails
from utils.logger import Logger
from pages.login_page import AuthorizationPage

logger = Logger()

@pytest.mark.negative
@pytest.mark.run(order=100)
def test_06_negative_auth(browser_1):
    auth_page = AuthorizationPage(browser_1)
    auth_page.test_invalid_emails(invalid_emails)