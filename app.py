import sys
import time
import datetime
from decouple import config
from selenium import webdriver


# Get credentials variables
EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

# Location of webdriver
PATH = '/usr/local/bin/chromedriver'


class PontoMais:
  # change for your work hours points
  hours_points = ["08:00", "12:00", "13:30", "17:30"]

  def start(self):
    if self.check_hour():
      self.driver = webdriver.Chrome(PATH)
      self.driver.get('https://app.pontomaisweb.com.br/#/meu_ponto/registro_de_ponto')

      self.login()
      time.sleep(15) # time to get location
      self.register_point()
      time.sleep(3)
      self.quit()
    return

  def check_hour(self):
    now = datetime.datetime.now()

    current_hour = '{:02d}'.format(now.hour)
    current_minute = '{:02d}'.format(now.minute)
  
    current_time = '{}:{}'.format(current_hour, current_minute)

    if current_time in self.hours_points:
      print("Hora de registrar o ponto!")
      return True

    return False

  def login(self):
    email_input = '/html/body/ng-view/div/div/form/div/div[1]/div/div/div/div/input'
    password_input = '/html/body/ng-view/div/div/form/div/div[2]/div/div/div/div/input'
    login_submit = '/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button'

    self.driver.find_element_by_xpath(email_input).send_keys(EMAIL)
    self.driver.find_element_by_xpath(password_input).send_keys(PASSWORD)
    self.driver.find_element_by_xpath(login_submit).click()

  def register_point(self):
    register_point_btn = '//*[@id="content-wrapper"]/div[2]/div/ng-view/div[2]/button'
    self.driver.find_element_by_xpath(register_point_btn).click()

  def quit(self):
    self.driver.close()
    self.driver.quit()
    sys.exit()


try:
  ponto_mais = PontoMais()
  while True:
    ponto_mais.start()
    time.sleep(60) # check every one minute
except KeyboardInterrupt:
  print("\nTchau!")
