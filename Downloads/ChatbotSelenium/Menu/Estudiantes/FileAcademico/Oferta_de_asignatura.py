from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time

def prueba_de_menu_estudiantes_ofertadematerias(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/div/a[3]/div/p"):
            return False
        return visible(driver,'//mat-card-title[contains(text(),"OFERTA DE ASIGNATURAS")]')
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False


def prueba_seleccion_sede(driver, sede):
    try:
        if not click(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[1]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,f'//span[contains(text(),"{sede}")]'):
            return False
        return True
    except (TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False

def prueba_de_busqueda_de_materias(driver,periodo1,carrera1,carrera2,periodo2):
    try:
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'//span[contains(text(),"{periodo2}")]'):
            return False
        if not  visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p'):
            return False
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'(//span[contains(text(),"{periodo1}")])'):
            return False
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[5]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'//span[contains(text(),"{carrera1}")]'):
            return False
        time.sleep(2)
        if not visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p'):
            return False
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[5]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'//span[contains(text(),"{carrera2}")]'):
            return False
        time.sleep(2)
        if not visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p'):
            return False
        return True
    except(TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False
    
def prueba_cambio_de_periodo(driver,periodo):
    try:
        if not click(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[2]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,f'//span[contains(text(),"{periodo}")]'):
            return False
        return visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p')
    except(TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False  
    
def prueba_de_busqueda_de_materias_1_periodo(driver,carrera1,carrera2):
    try:
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[5]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'//span[contains(text(),"{carrera1}")]'):
            return False
        time.sleep(2)
        if not visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p'):
            return False
        time.sleep(2)
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-oferta-asignaturas/div/mat-tab-group/div/mat-tab-body[1]/div/mat-card[1]/ucb-filtro-obtener-carrera/form/div/div[5]/mat-form-field/div/div[1]/div[3]'):
            return False
        time.sleep(2)
        if not click(driver,f'//span[contains(text(),"{carrera2}")]'):
            return False
        time.sleep(2)
        if not visible(driver,'//*[@id="mat-tab-content-0-0"]/div/mat-card[2]/div/div/ucb-tabla-maestra/div/table/tbody/tr[1]/td[4]/p'):
            return False
        return True
    except(TimeoutException,NoSuchElementException,ElementNotInteractableException) as e:
        return False