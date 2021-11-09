from appium import webdriver
desired_cap={
        "platformName": "Android",
        "deviceName": "device",
        "appPackage": "com.capitalx.blissfully",
        "appActivity": "ly.blissful.bliss.ui.ControllerActivity",
        "noReset": "true"

}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[1]').click()
driver.find_element_by_xpath('//android.view.View[@content-desc="Go Next"]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.EditText[1]').send_keys('Priyanka')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.EditText[2]').send_keys('priyankapukale259@gmail.com')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.EditText[3]').send_keys('Poo@1234')
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View[2]').click()