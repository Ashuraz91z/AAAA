import time
from json_handler import save_step
from selenium.webdriver.common.by import By

def handle_video(driver, training_id, step_id):
    try:
        video_element = driver.find_element(By.CLASS_NAME, "html5-main-video")
        duration = video_element.get_attribute("duration")  # Durée en secondes
        time.sleep(float(duration))  # Attendre la durée de la vidéo
        save_step(training_id, step_id, "video", duration)
    except Exception as e:
        print(f"Erreur lors du traitement de la vidéo : {e}")