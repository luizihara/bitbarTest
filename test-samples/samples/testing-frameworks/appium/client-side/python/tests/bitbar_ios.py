import os
import unittest
from time import sleep
from base_test import BaseTest
from selenium.webdriver.common.by import By


class BitbarIOS(BaseTest):
    def setUp(self):
        super().setUp()
        bitbar_project_name = os.environ.get("BITBAR_PROJECT") or "iOS sample project"
        bitbar_bundle_id = (
            os.environ.get("BITBAR_BUNDLE_ID") or "com.bitbar.testdroid.BitbarIOSSample"
        )
        automation_name = os.environ.get("BITBAR_AUTOMATION_NAME") or "XCUITest"
        if self.bitbar_device == "":
            self._find_device("iOS")

        self.capabilities["platformName"] = "iOS"
        self.capabilities["bitbar:options"]["project"] = bitbar_project_name
        self.capabilities["bitbar:options"]["device"] = self.bitbar_device
        self.capabilities["appium:bundleId"] = bitbar_bundle_id
        self.capabilities["appium:automationName"] = automation_name
        self.capabilities["appium:deviceName"] = "iPhone device"

    def test_sample(self):
        super()._start_webdriver()
        sleep(20)
        # view1
        self.utils.log("view1: Finding buttons")
        #buttons = self.driver.find_elements(By.ID, "button_access_account")
        #self.driver.find_element(By.ID, "button_access_account").click() # Falhou
        self.driver.find_element(By.XPATH, "//*[contains(@name, 'Acesse')]").click() # Funcionou
        #buttons = self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]")
        self.utils.log("view1: Clicking button [0] - RadioButton 1")

        #button = self.driver.find_element(By.XPATH, '//*[@text="Acesse"]')
        #button.click()

        
        sleep(10)
        #buttons.click()
        #button.click()



def initialize():
    return BitbarIOS


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BitbarIOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
