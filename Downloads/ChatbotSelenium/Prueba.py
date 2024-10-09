from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://academico.ucb.edu.bo/AcademicoNacionalTest/login")
    driver.maximize_window()
    
    acceder_con_google = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[text()="Acceder con Google"]'))
    )
    acceder_con_google.click()
   
    driver.switch_to.window(driver.window_handles[1])

    correo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    correo.click()
    correo.send_keys("nicole.uribe@ucb.edu.bo")
    siguiente=driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
    siguiente.click()
    
    contraseña = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
    )
    contraseña.click()
    contraseña.send_keys("nautt15a")
    contraseña.send_keys(Keys.ENTER)
finally:
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
