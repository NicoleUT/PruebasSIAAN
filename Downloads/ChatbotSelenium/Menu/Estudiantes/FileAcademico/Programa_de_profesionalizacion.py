from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time

def prueba_de_menu_estudiantes_programa_de_profesionalizacion(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/div/a[6]/div/p"):
            return False
        return visible(driver,'//mat-card-title[contains(text(),"MALLA DE ASIGNATURAS")]')
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False

def prueba_cambio_SEDE(driver):
    try:
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"LA PAZ")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"TARIJA")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"COCHABAMBA")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        return True
    except(TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        return False
    
def prueba_de_cambio_de_carreras(driver):
    try:
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ANT]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ARQ]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[COM]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[CPU]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[DER]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[DDM]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ENF]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[FYL]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[IMA]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[INC]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ICO]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ING]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[ITL]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[INE]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[IFI]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[IND]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[IME]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[INQ]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[MED]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[EPS]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[PSI]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        if not click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/mat-card/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]'):
            return False
        if not click(driver,'//span[contains(text(),"[TEO]")]'):
            return False
        if not visible(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-programa-profesionalizacion/ucb-gestion-mallas/div/div/mat-card[1]/ucb-tabla-maestra/div/table/tbody/tr[1]/td[1]/p'):
            return False
        return True
    except(TimeoutException,NoSuchElementException, ElementNotInteractableException) as e:
        return False