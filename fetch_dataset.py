import random

def get_random_disease():
    diseases = [
        {
            "disease_name": "Strep Throat",
            "symptoms": [
                "Sore throat",
                "Painful swallowing",
                "Red and swollen tonsils",
                "White patches or streaks of pus on the tonsils",
                "Tiny red spots on the area at the back of the roof of the mouth (soft or hard palate)",
                "Swollen, tender lymph nodes in your neck",
                "Fever",
                "Headache",
                "Rash",
                "Nausea or vomiting, especially in younger children",
                "Body aches"
            ],
            "major_tests_scan_results": [
                "Rapid Antigen Test: Positive for Group A Streptococcus bacteria",
                "Throat Culture: Presence of Group A Streptococcus bacteria",
                "Complete Blood Count (CBC): Elevated white blood cell count (suggestive of infection)",
                "Chest X-Ray: Normal findings (irrelevant)",
                "Urine Test: Normal findings (irrelevant)",
                "Electrocardiogram (ECG): Normal findings (irrelevant)"
            ],
            "treatments": [
                "Antibiotics (e.g., penicillin or amoxicillin) (Correct, for the disease)",
                "Over-the-counter pain relievers (acetaminophen or ibuprofen) (Correct, for symptoms of pain and fever)",
                "Rest and hydration (Correct, for the disease)",
                "Gargling with warm salt water (Correct, for the symptom of sore throat)",
                "Using throat lozenges (Correct, for the symptom of sore throat)",
                "Using a humidifier (Correct, for the symptom of sore throat)",
                "Steroids: Unnecessary and can suppress the immune system (Incorrect)",
                "Combination inhalers: No effect on strep throat, unnecessary treatment (Incorrect)",
                "Antivirals: Ineffective as strep throat is bacterial (Incorrect)",
                "Incorrect use of antibiotics: Can lead to antibiotic resistance and not treating the infection effectively (Incorrect)",
                "Warm compresses (Correct, for the symptom of swollen lymph nodes)"
            ],
            "other_information": [
                "Effects of smoking: Can irritate the throat and worsen symptoms",
                "Effects of sexual activity: No direct impact on strep throat",
                "Effects of family history: Slightly higher risk if there is a family history of frequent infections",
                "Effects of obesity: No direct impact on strep throat",
                "Effects of stress: Can weaken the immune system and prolong recovery"
            ]
        },
        {
            "disease_name": "Gastroenteritis",
            "symptoms": [
                "Watery diarrhea",
                "Abdominal cramps and pain",
                "Nausea and vomiting",
                "Fever",
                "Muscle aches or joint stiffness",
                "Headache",
                "Dehydration",
                "Loss of appetite",
                "Weight loss",
                "Chills",
                "Sweating"
            ],
            "major_tests_scan_results": [
                "Stool Test: Presence of bacteria, viruses, or parasites causing the infection",
                "Blood Test: Elevated white blood cell count (suggestive of infection), electrolyte imbalances",
                "Urine Test: Signs of dehydration, elevated specific gravity",
                "Abdominal Ultrasound: Normal findings (irrelevant)",
                "Chest X-Ray: Normal findings (irrelevant)",
                "Electrocardiogram (ECG): Normal findings (irrelevant)"
            ],
            "treatments": [
                "Oral Rehydration Solutions (ORS) (Correct, for the symptom of dehydration)",
                "IV fluids (in severe cases) (Correct, for the symptom of severe dehydration)",
                "Over-the-counter anti-diarrheal medications (e.g., loperamide) (Correct, for the symptom of diarrhea)",
                "Antibiotics (if bacterial infection is confirmed) (Correct, for the disease)",
                "Rest and hydration (Correct, for the disease)",
                "Eating a bland diet (e.g., bananas, rice, applesauce, toast) (Correct, for the disease)",
                "Antiemetic medications (e.g., ondansetron) (Correct, for the symptom of nausea and vomiting)",
                "Steroids: Unnecessary and can suppress the immune system (Incorrect)",
                "Antivirals: Ineffective unless the cause is a viral infection and specified (Incorrect)",
                "Painkillers like aspirin: Can irritate the stomach lining and worsen symptoms (Incorrect)",
                "Probiotics: Helpful in recovery but not a primary treatment (Incorrect)",
                "Avoiding dairy products temporarily (Correct, for the symptom of diarrhea)"
            ],
            "other_information": [
                "Effects of smoking: Can irritate the stomach lining and worsen symptoms",
                "Effects of sexual activity: No direct impact on gastroenteritis",
                "Effects of family history: No direct impact, but hygiene practices can play a role in prevention",
                "Effects of obesity: No direct impact on gastroenteritis",
                "Effects of stress: Can weaken the immune system and prolong recovery"
            ]
        },
        {
            "disease_name": "Influenza",
            "symptoms": [
                "Fever or feeling feverish/chills",
                "Cough",
                "Sore throat",
                "Runny or stuffy nose",
                "Muscle or body aches",
                "Headaches",
                "Fatigue (tiredness)",
                "Vomiting and diarrhea (more common in children)"
            ],
            "major_tests_scan_results": [
                "Rapid Influenza Diagnostic Tests (RIDTs): Positive for influenza virus",
                "Viral Culture: Isolation of influenza virus",
                "Reverse Transcription Polymerase Chain Reaction (RT-PCR): Detection of influenza viral RNA",
                "Chest X-Ray: Normal findings or may show pneumonia in complicated cases",
                "Complete Blood Count (CBC): Variable findings, may show elevated white blood cells",
                "Urine Test: Normal findings (irrelevant)"
            ],
            "treatments": [
                "Antiviral drugs (e.g., oseltamivir, zanamivir) (Correct, for the disease)",
                "Rest and hydration (Correct, for the disease)",
                "Over-the-counter pain relievers (acetaminophen or ibuprofen) (Correct, for symptoms of pain and fever)",
                "Cough suppressants and decongestants (Correct, for symptoms)",
                "Using a humidifier (Correct, for the symptom of sore throat)",
                "Steroids: Unnecessary and can suppress the immune system (Incorrect)",
                "Antibiotics: Ineffective as influenza is viral (Incorrect)",
                "Vitamin C: Popular but not proven to be effective (Incorrect)",
                "Herbal supplements: Unproven efficacy (Incorrect)",
                "Homeopathic remedies: Lack scientific evidence (Incorrect)"
            ],
            "other_information": [
                "Effects of smoking: Can worsen respiratory symptoms",
                "Effects of sexual activity: No direct impact on influenza",
                "Effects of family history: No direct impact, but vaccination history can play a role",
                "Effects of obesity: Increased risk of complications",
                "Effects of stress: Can weaken the immune system and prolong recovery"
            ]
        },
        {
            "disease_name": "Diabetes Mellitus",
            "symptoms": [
                "Increased thirst",
                "Frequent urination",
                "Extreme hunger",
                "Unexplained weight loss",
                "Presence of ketones in the urine",
                "Fatigue",
                "Irritability",
                "Blurred vision",
                "Slow-healing sores",
                "Frequent infections"
            ],
            "major_tests_scan_results": [
                "Fasting Blood Sugar Test: Elevated blood sugar levels",
                "HbA1c Test: Elevated levels indicating poor blood sugar control",
                "Oral Glucose Tolerance Test: Abnormal glucose levels",
                "Urine Test: Presence of glucose and ketones",
                "Lipid Profile: Abnormal cholesterol and triglyceride levels",
                "Kidney Function Test: Abnormal findings if complications present"
            ],
            "treatments": [
                "Insulin therapy (Correct, for type 1 diabetes and sometimes type 2)",
                "Oral diabetes medications (e.g., metformin) (Correct, for type 2 diabetes)",
                "Healthy eating (Correct, for managing blood sugar levels)",
                "Regular physical activity (Correct, for managing blood sugar levels)",
                "Blood sugar monitoring (Correct, for managing the disease)",
                "Weight loss (Correct, for type 2 diabetes management)",
                "Steroids: Can increase blood sugar levels (Incorrect)",
                "Antivirals: No effect on diabetes (Incorrect)",
                "Painkillers like aspirin: No direct effect on diabetes (Incorrect)",
                "Antibiotics: No effect unless treating an infection (Incorrect)",
                "Over-the-counter supplements: Variable efficacy and safety (Incorrect)"
            ],
            "other_information": [
                "Effects of smoking: Increases risk of diabetes complications",
                "Effects of sexual activity: Erectile dysfunction in men and reduced libido in women",
                "Effects of family history: Increased risk if there is a family history",
                "Effects of obesity: Major risk factor for type 2 diabetes",
                "Effects of stress: Can increase blood sugar levels"
            ]
        },
        {
            "disease_name": "Hypertension",
            "symptoms": [
                "Often none (silent condition)",
                "Headaches",
                "Shortness of breath",
                "Nosebleeds",
                "Flushing",
                "Dizziness",
                "Chest pain",
                "Blood in the urine",
                "Visual changes"
            ],
            "major_tests_scan_results": [
                "Blood Pressure Measurement: Elevated readings",
                "Electrocardiogram (ECG): Signs of heart strain or damage",
                "Echocardiogram: Enlarged heart or other abnormalities",
                "Blood Test: Kidney function, cholesterol levels",
                "Urine Test: Protein or blood in urine",
                "Eye Exam: Blood vessel damage in the retina"
            ],
            "treatments": [
                "Lifestyle changes (diet, exercise, weight loss) (Correct, for managing the condition)",
                "Antihypertensive medications (e.g., ACE inhibitors, beta-blockers) (Correct, for the disease)",
                "Reducing salt intake (Correct, for managing blood pressure)",
                "Limiting alcohol (Correct, for managing blood pressure)",
                "Managing stress (Correct, for managing blood pressure)",
                "Steroids: Can increase blood pressure (Incorrect)",
                "Antibiotics: No effect on hypertension (Incorrect)",
                "Antivirals: No effect on hypertension (Incorrect)",
                "Painkillers like NSAIDs: Can increase blood pressure (Incorrect)",
                "Herbal supplements: Unproven efficacy and safety (Incorrect)"
            ],
            "other_information": [
                "Effects of smoking: Increases risk of hypertension complications",
                "Effects of sexual activity: No direct impact but erectile dysfunction can occur with some medications",
                "Effects of family history: Increased risk if there is a family history",
                "Effects of obesity: Major risk factor for hypertension",
                "Effects of stress: Can increase blood pressure"
            ]
        },
        {
            "disease_name": "Migraine",
            "symptoms": [
                "Severe, throbbing headache",
                "Nausea",
                "Vomiting",
                "Sensitivity to light",
                "Sensitivity to sound",
                "Aura (visual disturbances)",
                "Dizziness",
                "Fatigue",
                "Neck stiffness"
            ],
            "major_tests_scan_results": [
                "MRI: Rule out other conditions",
                "CT Scan: Rule out other conditions",
                "Blood Test: Normal findings (irrelevant)",
                "Electroencephalogram (EEG): Normal findings (irrelevant)",
                "Eye Exam: Normal findings (irrelevant)"
            ],
            "treatments": [
                "Triptans (e.g., sumatriptan) (Correct, for aborting migraine attacks)",
                "Pain relievers (e.g., ibuprofen, aspirin) (Correct, for pain relief)",
                "Anti-nausea medications (e.g., metoclopramide) (Correct, for nausea and vomiting)",
                "Rest in a dark, quiet room (Correct, for symptom relief)",
                "Preventive medications (e.g., beta-blockers, anticonvulsants) (Correct, for reducing frequency and severity)",
                "Caffeine: Can help or worsen symptoms (variable effect)",
                "Steroids: Unnecessary and can suppress the immune system (Incorrect)",
                "Antibiotics: No effect on migraines (Incorrect)",
                "Antivirals: No effect on migraines (Incorrect)",
                "Over-the-counter supplements: Variable efficacy and safety (Incorrect)"
            ],
            "other_information": [
                "Effects of smoking: Can trigger or worsen migraines",
                "Effects of sexual activity: No direct impact on migraines",
                "Effects of family history: Increased risk if there is a family history",
                "Effects of obesity: May increase frequency of migraines",
                "Effects of stress: Can trigger or worsen migraines"
            ]
        }
    ]

    disease = random.choice(list(diseases))
    disease_name = disease['disease_name']

    symptoms = disease["symptoms"]
    treatment_plan = disease["treatments"]
    major_tests_scan_results = disease["major_tests_scan_results"]
    other_information = disease["other_information"]

    return disease_name, symptoms, treatment_plan, major_tests_scan_results, other_information
