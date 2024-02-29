from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Crear una clase AutomatizadorWeb


class AutomatizadorWeb:
    def __init__(self, url_login, usuario, contrasena, ruta_descargas):
        self.url_login = url_login
        self.usuario = usuario
        self.contrasena = contrasena
        self.ruta_descargas = ruta_descargas

    def configurar_descargas(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.ruta_descargas
        })
        self.driver = webdriver.Chrome(options=chrome_options)

    def iniciar_sesion(self):
        self.driver.get(self.url_login)
        username = self.driver.find_element(By.NAME, 'login')
        password = self.driver.find_element(By.NAME, 'password')
        username.send_keys(self.usuario)
        password.send_keys(self.contrasena)
        password.submit()

    def procesar_pagina(self):
        sleep(2)

        for i in range(1, 5):
            utilidades = self.driver.find_element(By.ID, 'item_78')

            actions = ActionChains(self.driver)
            actions.move_to_element(utilidades).perform()

            utilidades2 = self.driver.find_element(By.ID, 'item_137')
            actions.move_to_element(utilidades2).perform()

            utilidades3 = self.driver.find_element(By.ID, 'item_129')
            actions.move_to_element(utilidades3).perform()
            actions.click(utilidades3).perform()
            actions.move_to_element_with_offset(utilidades3, 0, -100).perform()

            sleep(2)
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'aba_td_txt_item_129'))
            )

            iframe = self.driver.find_element(By.ID, "iframe_item_129")
            self.driver.switch_to.frame(iframe)

            elemento = WebDriverWait(self.driver, 10000).until(
                EC.presence_of_element_located((By.ID, f'id-opt-opcion-{i}'))
            )
            elemento.click()

            enviar = self.driver.find_element(By.ID, 'sub_form_b').click()
            sleep(5)
            archivos = self.driver.find_elements(
                By.CLASS_NAME, 'css_archivo_grid_line')
            for archivo in archivos:
                sleep(3)

                archivo.click()
            self.driver.switch_to.default_content()
            sleep(2)

    def cerrar_navegador(self):
        self.driver.quit()

