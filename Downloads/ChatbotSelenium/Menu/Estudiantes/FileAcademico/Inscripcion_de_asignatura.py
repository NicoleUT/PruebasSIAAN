from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time

def prueba_de_menu_estudiantes_inscripcion(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver,'//mat-icon[contains(text(), "local_library")]'):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[3]/div/mat-icon[1]"):
            return False
        if not click(driver, "/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav/div/mat-nav-list/ucb-elementos-menu/div/a[4]/div/p"):
            return False
        start_time = time.time()
        if not control_de_tiempo(driver,'//mat-card-title[contains(text(),"MALLA")]',50):
            end_time = time.time()  # Fin del cronómetro
            return False 
        end_time = time.time()  # Fin del cronómetro
        elapsed_time = end_time - start_time
        print(f"La malla tardo en aparecer {elapsed_time:.2f} segundos.")
        
        return True
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False
    
def prueba_de_toma_de_materias(driver):
    try:
        start_time = time.time()
        scroll_click(driver,'//*[@id="mallaSeleccionada"]/ucb-toma-malla/div/div/mat-card/ucb-tabla-maestra/div/table/tbody/tr[3]/td[3]/p[1]')
        scroll_click(driver,'//*[@id="tomaParalelo"]/div/div[2]/mat-selection-list/mat-list-option[2]/div/div[2]')
        scroll_click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-toma-materias/div/div[2]/mat-card/button/span[1]')
        control_de_tiempo(driver,'//*[@id="mallaSeleccionada"]/ucb-toma-malla/div/mat-card[1]/div/ucb-tabla-maestra/div/table/tbody/tr[4]/td[4]/p',50)
        end_time = time.time()  # Fin del cronómetro
        elapsed_time2 = end_time - start_time
        print(f"La toma de materia tardo {elapsed_time2:.2f} segundos.")
        scroll_arriba(driver)
        scroll_click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-toma-materias/div/mat-tab-group/div/mat-tab-body[1]/div/div/ucb-toma-malla/div/mat-card[1]/div/ucb-tabla-maestra/div/table/tbody/tr[4]/td[7]/p')
        click(driver,'//*[@id="mat-dialog-1"]/ucb-dialogo-de-confirmacion/div/div/button[2]')
        return True
    except(TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        
        return False
