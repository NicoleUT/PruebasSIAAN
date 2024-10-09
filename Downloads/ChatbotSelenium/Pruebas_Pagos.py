from selenium.webdriver.support import expected_conditions as EC
from Login import *
from Menu.Estudiantes.PlataformaDePagos import *
from Comand import *

def pruebas_pagos(driver,sede,nroid):
    resultados = []
    prueba_de_Sedes(driver, sede, nroid)
    resultados.append(("Prueba de deuda", prueba_deuda(driver)))
    resultados.append(("Prueba de llenado de datos", prueba_datos_deuda(driver)))
    resultados.append(("Prueba pago por tarjeta", prueba_pago_por_tarjeta(driver)))
    resultados.append(("Prueba de pago por Qr",prueba_pago_por_QR(driver)))
    resultados.append(('Prueba cerrar',prueba_cerrar(driver)))
    return resultados
    