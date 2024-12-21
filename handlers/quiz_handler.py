import random
import time
from selenium.webdriver.common.by import By

def handle_quiz(driver, training_id, step_id):
    """
    Gère l'ensemble du quiz, y compris la validation des réponses.
    """
    print(f"Gestion du quiz pour la formation {training_id}, étape {step_id}")
    handle_quiz_questions(driver)

def handle_quiz_questions(driver):
    try:
        # Localiser toutes les questions dans le quiz
        questions = driver.find_elements(By.CSS_SELECTOR, "li.js-quiz")

        for question in questions:
            question_type = question.find_element(By.CLASS_NAME, "js-questionType").get_attribute("value")
            print(f"Traitement de la question avec le type : {question_type}")

            if question_type == "multiplechoice":
                # Gérer les réponses multiples
                handle_multiple_choice(question)

            elif question_type == "yesno":
                # Gérer les réponses oui/non (vrai/faux)
                handle_yes_no(question)

            else:
                print(f"Type de question non pris en charge : {question_type}")
            
            # Pause aléatoire pour simuler un comportement humain
            time.sleep(random.uniform(1, 3))

        # Localiser et cliquer sur le bouton "Valider"
        
        validate_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-md.mr-0.nav-bottom-next.js-btn-validate-questions")
        if validate_button:
            validate_button.click()
            print("Réponses validées.")
            time.sleep(2)  # Attendre le chargement du résultat après validation

    except Exception as e:
        print(f"Erreur lors de la gestion des questions : {e}")


def handle_multiple_choice(question):
    """
    Gérer les questions à choix multiples.
    """
    try:
        options = question.find_elements(By.CLASS_NAME, "js-multiple-choice-option")
        selected_options = random.sample(options, random.randint(1, len(options)))

        for option in selected_options:
            option.click()  # Sélectionner les options aléatoirement
        print(f"Options sélectionnées aléatoirement : {len(selected_options)}")

    except Exception as e:
        print(f"Erreur lors de la gestion des réponses multiples : {e}")


def handle_yes_no(question):
    """
    Gérer les questions de type vrai/faux.
    """
    try:
        options = question.find_elements(By.CLASS_NAME, "btn-rup-outline-dark")
        selected_option = random.choice(options)
        selected_option.click()  # Sélectionner aléatoirement vrai ou faux
        print("Réponse sélectionnée : Vrai/Faux")

    except Exception as e:
        print(f"Erreur lors de la gestion des réponses Vrai/Faux : {e}")