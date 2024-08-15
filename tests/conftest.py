import pytest
from appium import webdriver
from selene import browser
import os
from dotenv import load_dotenv
from hw_20.utils import attach, path

import config


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = path.abs_path_from_project(f".env.{context}")

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):

    options = config.driver_options(context=context)
    remote_url = options.get_capability('remote_url')
    browser.config.driver = webdriver.Remote(remote_url, options=options)

    browser.config.timeout = float(os.getenv("TIMEOUT"))

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    browser.quit()

    if context == 'bstack':
        attach.add_video(browser)
