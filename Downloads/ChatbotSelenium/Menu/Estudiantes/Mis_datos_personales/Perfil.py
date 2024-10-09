
from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *

def prueba_de_menu_estudiantes_misdatos(driver):
    try:
        if not click(driver, '/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-toolbar/button[1]/span[1]/mat-icon'):
            print("1")
            return False
        if not click(driver, "//mat-icon[contains(text(), 'local_library')]"):
            print("2")
            return False
        if not click(driver, "//mat-icon[contains(text(), 'people')]"):
            print("3")
            return False
        if not click(driver,"(//mat-icon[contains(text(), 'people')])[2]"):
            print("4")
            return False
        return visible(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/mat-card-header/div[2]/mat-card-title")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False

def prueba_verificar_datos_personales(driver):
    try:
        if not verificar_texto_estudiantes(driver,"/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/div/div[2]/div[1]/div[1]/div",'Nombre Completo:'):
            raise ValueError("No hay dato nombre")
        if not verificar_texto_estudiantes(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/div/div[2]/div[2]/div[1]/div','cedula de identidad:'):
            raise ValueError("No hay dato CI")
        if not verificar_texto_estudiantes(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/div/div[2]/div[3]/div[1]/div','Nacionalidad:'):
            raise ValueError("No hay dato Nacionalidad")
        if not verificar_texto_estudiantes(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[1]/mat-card/div/div[2]/div[5]/div[1]/div','Extranjero:'):
            raise ValueError("No hay datos extranjero")
        if not verificar_texto_estudiantes(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[2]/mat-card/div[2]/div[2]/div','Teléfono móvil:'):
            raise ValueError("No hay celular del estudiante")
        if not verificar_texto_estudiantes(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[4]/mat-card/div/div[1]/div','Colegio de egreso:'):
            raise ValueError("No hay datos de colegio")
        return True
    except (ValueError,TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en datos personales: {str(e)}")
        return False

def prueba_editar_datos(driver):
    try:
        if not scroll_click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[3]/div/button'): 
            return False
        if not input(driver,'//input[@id="mat-input-0"]','Centro'):
            return False
        if not input(driver,'//input[@id="mat-input-1"]','4123456'):
            return False
        if not input(driver,'//input[@id="mat-input-4"]','Avenida1 y Avenida2 Nro 098'):
            return False
        click(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[3]/mat-card/mat-card-content/div/button[2]')
        return disappear(driver,'/html/body/ucb-root/ucb-navegacion/ucb-navegacion-lateral/mat-sidenav-container/mat-sidenav-content/div/ucb-perfil-estudiante/div/div[3]/mat-card/mat-card-content/div/button[1]')
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        return False
