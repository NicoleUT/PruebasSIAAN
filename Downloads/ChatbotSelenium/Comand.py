from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
def input (driver,path, text):
     inp = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, path))
     )
     inp.send_keys(text)
     return True

def click (driver, path):
     button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, path))
        )
     button.click() 
     return True
 
def scroll_click(driver, path):
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        driver.execute_script("arguments[0].click();", button)
        return True

def scroll(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return True

def disappear(driver, path):
    WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, path))
        )
    return True

def save(driver, path):
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    # Extrae el valor del atributo "value"
    valor = elemento.get_attribute("value")
    return valor

def extraer(driver, path):
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        # Extrae el texto del elemento
        valor = elemento.text
        return valor

def button_cerrar(driver):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//input[@id='pie_btnCerrar']"))
        )
    button.click() 
    return True

def visible(driver, path):
    iframe_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,path))
        )
    return iframe_visible

def verificar_texto_estudiantes(driver,path, texto):
    try:
        div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        texto_completo = div.text
        if texto in texto_completo:
            partes = texto_completo.split(texto) 
            if len(partes) > 1:
                texto_despues_de_colon = partes[-1].strip() 
                if texto_despues_de_colon:
                    print(f"Texto extraido: {texto_despues_de_colon}")
                    return True   
    except Exception as e:
        print(f"Error: {str(e)}")
        return False 

def visible(driver,path):
   try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        return True  
   except TimeoutException:
        return False
    
def control_de_tiempo(driver,path,timeout):
    try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, path)))
        return True
    except TimeoutException:
        return False
# Función para hacer scroll hacia arriba
def scroll_arriba(driver):
    driver.execute_script("window.scrollTo(0, 0);")

# Función para hacer click en un elemento después de hacer scroll
def click_scroll_arriba(driver, xpath_elemento):
    try:
        # Hacer scroll hacia arriba
        scroll_arriba(driver)
        # Encontrar el elemento
        elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_elemento))
        )
        # Hacer click en el elemento
        elemento.click()
    except (TimeoutException) as e:
        print(f"Error: {str(e)}")

def click_derecho(driver, xpath_elemento):
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_elemento))
        )
        # Crear una instancia de ActionChains
        action = ActionChains(driver)
        # Realizar el clic derecho en el elemento
        action.context_click(elemento).perform()