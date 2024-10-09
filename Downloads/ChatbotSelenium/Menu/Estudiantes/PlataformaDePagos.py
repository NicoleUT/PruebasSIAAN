from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotInteractableException
from Comand import *
import time
def prueba_de_menu_estudiantes(driver):
    try:
        if not click(driver, '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'):
            return False
        if not click(driver, "//mat-icon[contains(text(), 'local_library')]"):
             return False
        res=click(driver, "//mat-icon[contains(text(), 'monetization_on')]")
        time.sleep(2)
        return res
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba_de_menu: {str(e)}")
        return False

def prueba_de_plataforma_pago(driver):
    try:
       res=scroll_click(driver, "//input[@name='btnIngresar']")
       return res
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en plataforma de pagos: {str(e)}")
        return False
    
def prueba_de_Sedes(driver, text, carnet):
    try:
        xpath=f'//img[@id="ContentPlaceHolder2_img{text}"]'
        if not click(driver, xpath):
            return False
        return prueba_de_Sistema_de_Pagos(driver, carnet)
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba de sedes: {str(e)}")
        return False

def prueba_de_Sistema_de_Pagos(driver,text):
    try:
        if not input(driver,'//input[@id="ContentPlaceHolder2_tbDocIdentidad"]',text):
            return False
        print("ingresa el numero que vez en pantalla")
        time.sleep(15)
        res= scroll_click(driver,"//input[@id='ContentPlaceHolder2_btnIngresar']")
        return res 
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba de sistema de pagos: {str(e)}")
        return False

def  prueba_deuda(driver):
    try:
        if not click(driver, '//*[@id="ContentPlaceHolder2_gvDerAcad_chkElegido_0"]'):
            return False
        return scroll_click(driver,'//*[@id="pie_btnGuardar"]')
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba de sistemas de pagos: {str(e)}")
        return False

def prueba_datos_deuda(driver):
    try:
        scroll(driver)
        if not input(driver,'//input[@id="ContentPlaceHolder2_tbNIT"]', "12345678"):
            return False
        if not input(driver,'//input[@id="ContentPlaceHolder2_tbRazonSocial"]', "Prueba"):
            return False
        scroll(driver)
        if not input(driver,"//input[@id='ContentPlaceHolder2_tbCelular']", "0000000"):
            return False
        if not input(driver,'//input[@id="ContentPlaceHolder2_tbEmail"]', "name@ucb.edu.bo"):
            return False
        if not scroll_click(driver, '//*[@id="form1"]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/label'):
            return False
        return disappear(driver,"//input[@id='ContentPlaceHolder2_tbCelular']")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba datos deuda: {str(e)}")
        return False

def prueba_pago_por_tarjeta(driver):
    try:
        valor=extraer(driver,"//*[@id='ContentPlaceHolder2_gvServicios']/tbody/tr[3]/td[4]")
        if not scroll_click(driver,'//input[@value="Pagar con tarjeta"]'):
            return False
        texto=save(driver,'//input[@id="pie_btnPagar"]')
        if str(valor) in texto:
            button_cerrar(driver)
            return True
        else:
            raise ValueError("El monto no es correcto")
    except (ValueError,TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        button_cerrar(driver)
        return False

def prueba_pago_por_QR(driver):
    try:
        scroll_click(driver,'//input[@id="pie_btnPagarQr"]')
        scroll(driver)
        imagen=visible(driver,'//iframe[@id="imgQr"]')
        if imagen:
           driver.back()
           driver.refresh()
           return True
        else:
            driver.back()
            return False
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba de pago por qr: {str(e)}")
        return False
    
def prueba_cerrar(driver):
    try:
        scroll_click(driver,"//input[@id='pie_btnVolver']")
        scroll_click(driver,"//input[@id='pie_btnVolver']")
        scroll_click(driver,"//input[@id='pie_btnSalir']")
    except (TimeoutException, NoSuchElementException,ElementNotInteractableException ) as e:
        print(f"Fallo en prueba de pago por qr: {str(e)}")
        return False
