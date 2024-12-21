import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from json_handler import save_step

def handle_text(driver, training_id, step_id):
    try:
        save_step(training_id, step_id, "text")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "next"))
        )
        next_button.click()
        print("Clic sur le bouton 'Suivant' effectué.")
        time.sleep(2)
    except Exception as e:
        print(f"Erreur lors du traitement du texte : {e}")