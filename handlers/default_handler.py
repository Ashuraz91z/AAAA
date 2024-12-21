import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_existing_step(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "next"))
        )
        next_button.click()
        print("Clic sur le bouton 'Suivant' effectué pour une étape existante.")
        time.sleep(2)
    except Exception as e:
        print(f"Erreur lors du clic sur le bouton 'Suivant' : {e}")