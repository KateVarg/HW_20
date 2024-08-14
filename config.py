import os
from appium.options.android import UiAutomator2Options
from hw_20.utils import path
from dotenv import load_dotenv


load_dotenv()


def driver_options(context):
    options = UiAutomator2Options()
    dotenv_path = path.abs_path_from_project(f'.env.{context}')
    load_dotenv(dotenv_path)

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv("REMOTE_URL_BSTACK"))
        options.set_capability('deviceName', os.getenv("DEVICE_NAME"))
        options.set_capability('platformName', os.getenv("PLATFORM_NAME"))
        options.set_capability('platformVersion', os.getenv("PLATFORM_VERSION"))
        options.set_capability('app', os.getenv("APP"))
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': os.getenv("USERNAME"),
                'accessKey': os.getenv("ACCESS-KEY")
            })

    if context == 'emulator' or context == 'local_device':
        options.set_capability('remote_url', os.getenv("REMOTE_URL"))
        options.set_capability('deviceName', os.getenv("DEVICE_NAME"))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', path.abs_path_from_project(os.getenv("APP")))

        print(f"REMOTE_URL: {os.getenv('REMOTE_URL')}")
        print(f"DEVICE_NAME: {os.getenv('DEVICE_NAME')}")
        print(f"APP: {path.abs_path_from_project(os.getenv('APP'))}")

    return options
