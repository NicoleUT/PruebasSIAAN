from Login import *
import threading
from selenium import webdriver
from Menu.Estudiantes.FileAcademico.Inscripcion_de_asignatura import *

def realizar_varios_ingresos_a_inscripciones_a_la_vez():
    driver = webdriver.Chrome() 
    driver.get("https://academico.ucb.edu.bo/AcademicoNacionalTest/inicio")
    try:
        prueba_ingreso_usuario(driver,"nicole.uribe")
        #PRODUCCION
        #prueba_ingreso_contraseña(driver,'Ucb.8738200')
        #TEST
        prueba_ingreso_contraseña(driver, "@AmyLili24")
        #click(driver,'//span[contains(text(),"Realizarlo más tarde")]') #Encuesta
        prueba_de_menu_estudiantes_inscripcion(driver)
        prueba_de_toma_de_materias(driver)
        return True
    except Exception as e:
        return False
def prueba_concurrencia(numero_usuarios):
    threads = []

    for i in range(numero_usuarios):
        t = threading.Thread(target=realizar_varios_ingresos_a_inscripciones_a_la_vez)
        threads.append(t)
        t.start()

    
    for t in threads:
        t.join()


prueba_concurrencia(50)
 