from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time

def prueba_de_menu_estudiantes_horarios_de_clases(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/div/a[4]/div/p"):
            return False
        return visible(driver,'//mat-card-title[contains(text(),"PERIODO ACADÉMICO")]')
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False

def prueba_de_horarios(driver):
    try:
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-horario-estudiante/div[3]/div[3]/mat-card/mat-card-header/div[2]/mat-card-title'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-horario-estudiante/div[3]/div[4]/mat-card/mat-card-header/div[2]/mat-card-title'):
            return False
        return True
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False

def descargar_horario(driver):
    try:
      if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-horario-estudiante/div[3]/div[3]/mat-card/ucb-tabla-maestra/button/span[1]/mat-icon'):
          return False 
      return True
    except(TimeoutError,TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False