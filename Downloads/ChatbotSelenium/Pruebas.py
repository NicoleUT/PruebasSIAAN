from Login import *
from Menu.Estudiantes.PlataformaDePagos import *
from Menu.Estudiantes.Mis_datos_personales.Perfil import *
from Menu.Estudiantes.FileAcademico.PagosPendientes import *
from Comand import *
from Pruebas_Pagos import pruebas_pagos
from Menu.Estudiantes.FileAcademico.Kardex import *
from Menu.Estudiantes.FileAcademico.Oferta_de_asignatura import *
from Menu.Estudiantes.FileAcademico.Horarios_de_clases import *
from Menu.Estudiantes.FileAcademico.Mi_asignatura import *
from Menu.Estudiantes.FileAcademico.Programa_de_profesionalizacion import *
from Menu.Estudiantes.FileAcademico.Inscripcion_de_asignatura import *
def ejecutar_pruebas():
    resultados = []
    driver = iniciar_navegador()
        
    if driver:
        #prueba Login
        resultados.append(("Prueba de ingreso de usuario", prueba_ingreso_usuario(driver, "nicole.uribe")))
        resultados.append(("Prueba de ingreso de contrasena", prueba_ingreso_contraseña(driver, "@AmyLili24")))
        #prueba inicio
        driver.get("https://academico.ucb.edu.bo/AcademicoNacionalTest/inicio")
        #click(driver,'//span[contains(text(),"Realizarlo más tarde")]') #Encuesta
        
        
        #PRUEBA PLATAFORMA DE PAGOS
        #resultados.append(("Prueba de menu", prueba_de_menu_estudiantes(driver)))
        #driver.switch_to.window(driver.window_handles[1])
        #resultados.append(("Prueba de plataforma de pagos",prueba_de_plataforma_pago(driver)))
        #resultados.append(("Prueba sede La Paz",pruebas_pagos(driver,"LaPaz","9908642")))
        #resultados.append(("Prueba sede Cochabamba",pruebas_pagos(driver,"Cochabamba","4919193")))
        #resultados.append(("Prueba sede Santa Cruz",pruebas_pagos(driver,"SantaCruz","8327033")))
        #resultados.append(("Prueba sede Tarija",pruebas_pagos(driver,"Tarija","7619799"))) 
        #resultados.append(("Prueba sede La Plata", pruebas_pagos(driver,"Sucre", "13220722")))
        #resultados.append((("Prueba de seleccion de sedes Oruro", prueba_de_Sedes(driver,"Oruro","")))) no existen semestre ni estudiantes
        #driver.switch_to.window(driver.window_handles[0])   
             
        #PRUEBA DE MIS DATOS PERSONALES
        #resultados.append(("Prueba de menu", prueba_de_menu_estudiantes_misdatos(driver)))
        #resultados.append(("Prueba verificacion de datos",prueba_verificar_datos_personales(driver)))
        #resultados.append(("Prueba de edicion",prueba_editar_datos(driver)))
        
        #PRUEBA DE PAGOS PENDIENTES
        #resultados.append(("Prueba de pagos pendientes", prueba_de_menu_estudiantes_pagospendientes(driver)))
        
        #PRUEBA DE KARDEX
        #resultados.append(("Prueba de kardex", prueba_de_menu_estudiantes_kardex(driver)))
        #resultados.append(("descargar kardex",descargar(driver)))
        #driver.switch_to.window(driver.window_handles[0])
        
        #PRUEBA DE OFERTA DE MATERIAS
        #resultados.append(("Prueba ingreso a oferta de materias", prueba_de_menu_estudiantes_ofertadematerias(driver)))
        #resultados.append(("Prueba de seleccion de sede La Paz", prueba_seleccion_sede(driver,"LA PAZ")))
        #resultados.append(("Prueba de busqueda de materias", prueba_de_busqueda_de_materias(driver,'[IN-2024]','[ADM]','[DER]','[A-2024]')))
        #resultados.append(("Prueba de periodo", prueba_cambio_de_periodo(driver,'POSTGRADO')))
        
        #resultados.append(("Prueba de seleccion de sede Cochabamba", prueba_seleccion_sede(driver,"COCHABAMBA")))
        #resultados.append(("Prueba de busqueda de materias", prueba_de_busqueda_de_materias(driver,'[2-2024]','[ADM]','[ING]','[A-2024]')))
        #resultados.append(("Prueba de periodo", prueba_cambio_de_periodo(driver,'POSTGRADO')))
        
        #resultados.append(("Prueba de seleccion de sede Santa Cruz", prueba_seleccion_sede(driver,"SANTA CRUZ")))
        #resultados.append(("Prueba de busqueda de materias", prueba_de_busqueda_de_materias_1_periodo (driver,'[AGN]','[CIV]')))
        
        #resultados.append(("Prueba de seleccion de sede Tarija", prueba_seleccion_sede(driver,"TARIJA")))
        #resultados.append(("Prueba de busqueda de materias", prueba_de_busqueda_de_materias(driver,'[T2-2024]','[ADM]','[ARQ]','[I-2024]')))
        
        #resultados.append(("Prueba de seleccion de sede Escuela", prueba_seleccion_sede(driver,"ESCUELA")))
        #resultados.append(("Prueba de busqueda de materias", prueba_de_busqueda_de_materias_1_periodo (driver,'[MMD]','[ISE]')))
        
        #Prueba de horarios de clases
        #resultados.append(("Prueba de menu de horarios de clases", prueba_de_menu_estudiantes_horarios_de_clases(driver)))
        #resultados.append(("Prueba de aparicion de horarios",prueba_de_horarios(driver)))
        #resultados.append(("descargar horario",descargar_horario(driver)))
        #driver.switch_to.window(driver.window_handles[0])
        
        #Prueba de mis asignaturas
        #resultados.append(("Prueba de mis asignaturas", prueba_de_menu_estudiantes_mis_asignaturas(driver)))
        #resultados.append(("Ingreso materia", prueba_de_materia(driver)))
        #resultados.append(('Prueba de horario al abrir materia', prueba_horario_en_materia_materia(driver)))
        #resultados.append(("Prueba Evaluacion docente",prueba_evaluacion_continua(driver)))
        #resultados.append(("Prueba de ingreso al LMS", prueba_LMS(driver)))
        
        #PRUEBA DE PROFESIONALIZACION
        #resultados.append(("Prueba de ingreso a programa de profesionalizacion", prueba_de_menu_estudiantes_programa_de_profesionalizacion(driver)))
        #resultados.append(("Prueba de seleccion de sede",prueba_cambio_SEDE(driver)))
        #resultados.append(("Prueba de cambio de carrera",prueba_de_cambio_de_carreras(driver)))
        
        #PRUEBA DE INSCRIPCION
        #click(driver,'//span[contains(text(),"Realizarlo más tarde")]') #Encuesta
        resultados.append(("Prueba varios usuarios a la vez",prueba_de_menu_estudiantes_inscripcion(driver)))
        resultados.append(("Prueba de toma de materia",prueba_de_toma_de_materias(driver)))
        time.sleep(15000) 
        
        driver.quit()
    return resultados

# Ejecutar pruebas
resultados = ejecutar_pruebas()

# Mostrar resultados
for prueba, resultado in resultados:
    estado = "paso" if resultado else "fallo"
    print(f"{prueba}: {estado}")
