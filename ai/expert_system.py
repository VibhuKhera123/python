class Symptom:
    def __init__(self, name, question):
        self.name = name
        self.question = question

class Disease:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

def get_input(symptoms):
    answers = {}
    for symptom in symptoms:
        while True:
            answer = input(symptom.question + " (yes/no): ")
            if answer.lower() in ['yes', 'no']:
                answers[symptom.name] = answer.lower() == 'yes'
                break
            else:
                print("Please answer with 'yes' or 'no'.")
    return answers

def diagnose(answers, diseases):
    for disease in diseases:
        if all(answers[symptom] for symptom in disease.symptoms):
            return disease.name
    return "No diagnosis found."

def main():
    symptoms = [
        Symptom("fever", "Do you have a fever?"),
        Symptom("cough", "Do you have a cough?"),
        Symptom("headache", "Do you have a headache?")
    ]

    diseases = [
        Disease("cold", ["fever", "cough"]),
        Disease("flu", ["fever", "cough", "headache"]),
        Disease("allergy", ["cough"])
    ]

    answers = get_input(symptoms)
    diagnosis = diagnose(answers, diseases)
    print("Diagnosis:", diagnosis)

if __name__ == "__main__":
    main()