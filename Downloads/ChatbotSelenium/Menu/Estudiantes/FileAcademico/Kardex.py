from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *

def prueba_de_menu_estudiantes_kardex(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/div/a[2]/div/mat-icon"):
            return False
        if not visible(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-kardex-estudiante/div/div[3]/ucb-tabla-kardex/mat-card/div/table[1]/thead/tr[1]/th/div"): 
            return False
        scroll(driver)
        if not visible(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-kardex-estudiante/div/div[4]/div[2]/mat-card/mat-card-header/div[2]/mat-card-title"):
            return False
        return visible(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-kardex-estudiante/div/div[4]/div[1]/mat-card/mat-card-header/div[2]/mat-card-title")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False
def descargar(driver):
    try:
      if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-kardex-estudiante/div/div[3]/ucb-tabla-kardex/mat-card/button/span[1]/mat-icon'):
          return False 
      return True
    except(TimeoutError,TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False