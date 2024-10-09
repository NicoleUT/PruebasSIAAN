from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time

def prueba_de_menu_estudiantes_mis_asignaturas(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        return  click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/div/a[5]/div/p")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False

def prueba_de_materia(driver):
    try:
        if not click(driver,'//*[@id="mat-tab-label-0-1"]'):
            return False
        return scroll_click(driver,'//span[contains(text(),"VER")]')
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False

def prueba_horario_en_materia_materia(driver):
    try:
        return visible(driver, '//mat-card-title[contains(text(),"HORARIO")]')
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False

def prueba_evaluacion_continua(driver):
    try:
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-mi-materia/div[1]/a[1]'):
            return False
        return visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-mi-materia/div[2]/ucb-evaluacion-continua/div/div[3]/mat-card[1]/div/table/tbody/tr/td[7]')
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False

def prueba_LMS(driver):
    try:
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-mi-materia/div[1]/a[2]'):
            return False
        return True
    except(TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False