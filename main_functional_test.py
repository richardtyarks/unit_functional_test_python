# https://stackoverflow.com/questions/56119289/element-not-interactable-selenium resolve bug submit button
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        print("setup")
        # self.driver = webdriver.Chrome(r'J:\COURS_ESIG_2\INLO\test Selenium\chromedriver.exe')
        self.driver = webdriver.Chrome(
            r'/chromedriver.exe')
        page_url = "https://esig-sandbox.ch/team20_7_v2/"
        driver = self.driver
        driver.maximize_window()
        driver.get(page_url)

        path_login_main_page = driver.find_element_by_css_selector('.nav-item:nth-child(6) > .nav-link')
        path_login_main_page.click()

        four_input_login_mail = driver.find_element_by_id("email_address")
        four_input_login_mail.clear()
        four_input_login_mail.send_keys("esigfour1@hotmail.com")

        four_input_login_mail_login_pswrd = driver.find_element_by_id("password")
        four_input_login_mail_login_pswrd.clear()
        four_input_login_mail_login_pswrd.send_keys("Super2020")

        btn_login = driver.find_element_by_name('connection')
        btn_login.click()

        btn_admin_nav = driver.find_elements_by_link_text('Administration')
        btn_admin_nav[0].click()

        btn_admin_product_crud = driver.find_element_by_css_selector('.col-sm-4:nth-child(5) .fa')
        btn_admin_product_crud.click()

        btn_admin_product_add = driver.find_element_by_css_selector('.btn-success')
        btn_admin_product_add.click()

    # Insert Data Product
    def insert_data_test(self, product_value_name, product_value_description, product_value_prize,
                         product_value_file1, product_value_file2):

        prod_input_name = self.driver.find_element_by_name("productName")
        prod_input_name.clear()
        prod_input_name.send_keys(product_value_name)

        prod_input_description = self.driver.find_element_by_name("productDescription")
        prod_input_description.clear()
        prod_input_description.send_keys(product_value_description)

        prod_input_prize = self.driver.find_element_by_name("productPrize")
        prod_input_prize.clear()
        prod_input_prize.send_keys(product_value_prize)
        if product_value_file1 != "":
            prod_input_file1 = self.driver.find_element_by_name("file1")
            prod_input_file1.send_keys(product_value_file1)
        if product_value_file2 != "":
            prod_input_file2 = self.driver.find_element_by_name("file2")
            prod_input_file2.send_keys(product_value_file2)

        btn_submit = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='submit']")))
        self.driver.execute_script("arguments[0].click();", btn_submit)

    # disable product's display from the test
    def back_to_normal(self):
        btn_admin_nav = self.driver.find_elements_by_link_text('Administration')
        btn_admin_nav[0].click()

        btn_admin_product_crud = self.driver.find_element_by_css_selector('.col-sm-4:nth-child(5) .fa')
        btn_admin_product_crud.click()

        list_product_created = self.driver.find_elements_by_css_selector('tr')
        if len(list_product_created) > 4:
            i = 0
            for row in list_product_created:
                if i > 4:
                    button_row = self.driver.find_elements_by_css_selector('tr:nth-child(' + str(i) + ') .fa')
                    if button_row[0].get_attribute('class') == 'fa fa-check':
                        button_row[0].click()
                i += 1

    # Closing the browser.
    def tearDown(self):
        print("teardown")
        self.back_to_normal()
        self.driver.close()

    def check_product_image_exist(self):
        for i in range(1, 3):
            try:
                self.driver.find_elements_by_css_selector('.col-md-3:nth-child(' + str(i) + ') .img-fluid')
            except NoSuchElementException:
                return False
        return True

    def test_succes_insertion(self):
        self.insert_data_test("Air pods", "c'est cher", "150", r'C:\Users\richa\Desktop\kirbo.jpg',
                              r'C:\Users\richa\Desktop\kirbo.jpg')
        self.assertEqual("le produit a été ajouté", self.driver.find_elements_by_css_selector('h4')[0].text)

    def test_name_blank_insertion(self):

        self.insert_data_test("", "c'est cher", "150", r'C:\Users\richa\Desktop\kirbo.jpg',
                              r'C:\Users\richa\Desktop\kirbo.jpg')
        alert = Alert(self.driver)
        self.assertEqual("Nom manquant", alert.text)
        alert.accept()

    def test_desc_blank_insertion(self):
        self.insert_data_test("Banane", "", "150", r'C:\Users\richa\Desktop\kirbo.jpg',
                              r'C:\Users\richa\Desktop\kirbo.jpg')
        alert = Alert(self.driver)
        self.assertEqual("Description manquante", alert.text)
        alert.accept()

    def test_negative_prize(self):
        self.insert_data_test("Banane", "c'est cher", "-1", r'C:\Users\richa\Desktop\kirbo.jpg',
                              r'C:\Users\richa\Desktop\kirbo.jpg')
        alert = Alert(self.driver)
        self.assertEqual("Veuillez mettre un prix entier", alert.text)
        alert.accept()

    def test_blank_image1(self):
        self.insert_data_test("Banane", "c'est cher", "1", "", r'C:\Users\richa\Desktop\kirbo.jpg')
        alert = Alert(self.driver)
        self.assertEqual("Image 1 manquante", alert.text)
        alert.accept()

    def test_blank_image2(self):
        self.insert_data_test("Banane", "c'est cher", "1", r'C:\Users\richa\Desktop\kirbo.jpg', "")
        alert = Alert(self.driver)
        self.assertEqual("Image 2 manquante", alert.text)
        alert.accept()

    def test_check_extension_image(self):
        self.insert_data_test("Banane", "c'est cher", "1", r'C:\Users\richa\Desktop\kirbo.jpg',
                              r'C:\Users\richa\Desktop\hhva_richardtrks_v3.sql')
        self.assertEqual(
            "L'extension utilisé pour l'image 2 n'est pas autorisée, les types d'extensions autorisées sont: jpg, "
            "jpeg, gif, png",
            self.driver.find_elements_by_css_selector('h4')[0].text)

    def test_number_of_images(self):
        btn_admin_nav_back = self.driver.find_elements_by_xpath('//div[3]/a')
        btn_admin_nav_back[0].click()

        list_product_created = self.driver.find_elements_by_css_selector('tr')

        button_row = self.driver.find_elements_by_css_selector(
            'tr:nth-child(' + str(len(list_product_created) - 1) + ') a > .btn')
        button_row[0].click()
        sleep(5)
        self.assertTrue(self.check_product_image_exist())


if __name__ == "__main__":
    unittest.main()
