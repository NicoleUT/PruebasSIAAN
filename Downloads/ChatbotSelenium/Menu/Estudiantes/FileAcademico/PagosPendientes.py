from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *

def prueba_de_menu_estudiantes_pagospendientes(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "//mat-icon[contains(text(), 'attach_money ')]"):
            return False
        return visible(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/mat-card-header/div[2]/mat-card-title")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False