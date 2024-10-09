from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Comand import input, click
def iniciar_navegador():
    try:
        driver = webdriver.Chrome()
        driver.get("https://academico.ucb.edu.bo/AcademicoNacionalTest/")
        driver.maximize_window()
        return driver
    except Exception as e:
        print(f"Error al iniciar el navegador: {str(e)}")
        return None

def prueba_ingreso_usuario(driver, usuario):
    try:
        return input(driver,"//input[@id='mat-input-0']", usuario)
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Fallo en prueba_ingreso_usuario: {str(e)}")
        return False

def prueba_ingreso_contraseña(driver, contraseña):
    try:
        input(driver, "//input[@id='mat-input-1']", contraseña)
        return click(driver,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Fallo en prueba_ingreso_contraseña: {str(e)}")
        return False

