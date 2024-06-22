from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

opciones_chrome = webdriver.ChromeOptions()
opciones_chrome.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opciones_chrome)
navegador.get("https://orteil.dashnet.org/experiments/cookie/")
galleta = navegador.find_element(By.ID, value='cookie')
def comprar_elemento():
    productos_disponibles = ['Time machine', 'Portal', 'Alchemy lab', 'Shipment', 'Mine', 'Factory', 'Grandma', 'Cursor']
    for producto in productos_disponibles:
        try:
            articulo_tienda = navegador.find_element(By.XPATH, value =f'//*[@id="buy{producto}"]/b')
            precio = articulo_tienda.text.split('-')[1].strip().replace(',', '')
            galletas = navegador.find_element(By.ID, value='money').text.replace(',', '')
            if int(galletas) > int(precio):
                cantidad_a_comprar = int(int(galletas) / int(precio))
                for intento in range(cantidad_a_comprar):
                    try:
                        articulo_tienda.click()
                    except StaleElementReferenceException:
                        pass
                    except NoSuchElementException:
                        pass
        except StaleElementReferenceException:
            pass

horneando = True
cinco_min = time.time() + 60 * 5
tres_min = time.time() + 60 * 3
intervalo_retraso = 5
retraso_compra = time.time() + intervalo_retraso
proximo_hito = tres_min

while horneando:
    if time.time() > cinco_min:
        galletas_por_segundo = navegador.find_element(By.ID, value='cps').text
        print(f"Puntaje final: {galletas_por_segundo}")
        break
    if time.time() >= retraso_compra:
        retraso_compra = time.time() + intervalo_retraso
        comprar_elemento()
    if time.time() >= proximo_hito:
        intervalo_retraso += 5
        proximo_hito += 60
    galleta.click()
