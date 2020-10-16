from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(funcName)s : %(message)s",
                    datefmt= "%H:%M:%S",
                    filename="autentificare_log file.log")


class LogareCont(object):
    def __init__(self, url):
        logging.info(f"Inceperea sesiunii cu {url}...")
        self.url = url
        self.driver = webdriver.Chrome(r'D:\Python Fundamentals\selenium\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.url)

    def buton_navigare_sign_in(self):
        buton_sign_in = self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-login')]")
        buton_sign_in.click()

    def close_session(self):
        logging.info(f"Sesiunea cu {self.url} a fost incheiata")
        self.driver.close()

    def input_username_password(self, username, password):
        try:
            camp_email = self.driver.find_element(By.ID, 'login-email')
            camp_parola = self.driver.find_element(By.ID, 'login-password')
            logging.info("Identificarea elementelor de email/parola a reusit")
        except:
            logging.error("Identificarea elementelor de email/parola nu a reusit")
            return False

        camp_email.send_keys(username)
        camp_parola.send_keys(password)

        buton_autentificare = self.driver.find_element(By.XPATH, "//button[@type = 'submit']")
        buton_autentificare.click()


auth = LogareCont("https://cursuri.telacad.ro")
auth.buton_navigare_sign_in()
time.sleep(3)
auth.input_username_password('carmen.anda1505@yahoo.com', 'Chooseyourself1!')
logging.info(auth.driver.title)
time.sleep(5)
auth.close_session()

