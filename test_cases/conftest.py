import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Open source project, Orange HRM'
    config.stash[metadata_key] ['Module Name'] = 'Login'
    config.stash[metadata_key] ['Tester'] = 'Durgesh'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)