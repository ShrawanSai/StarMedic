import random
def get_random_patient():
      patients = [
          {
              "name": "Elara Vendarian",
              "specie": "Zabrak",
              "image_path" : "species/elara.png",
              "description": """Elara Vendarian, a Zabrak from the Star Wars world, despite her impressive intellect and self-assured demeanor, is a challenging patient when it comes to medical visits. When visiting a doctor, she tends to overanalyze her symptoms, often diagnosing herself before the medical professionals have a chance. Her confidence can come across as dismissive or even condescending, as she believes she knows best about her own health.

  When Elara is injured or in pain, her usually composed facade crumbles. She becomes extremely sensitive and vocal about her discomfort, frequently expressing her distress with dramatic flair. Small injuries feel catastrophic to her, and she doesn't hesitate to make her suffering known. Her pain tolerance is notably low, and she requires a great deal of reassurance and gentle handling from the medical staff.

  During periods of depression, Elara's usual confidence is replaced with a profound sense of vulnerability. She becomes introspective and withdrawn, struggling with feelings of inadequacy and self-doubt. Her sharp mind turns against her, as she fixates on her perceived failures and weaknesses. In these moments, she needs compassionate care and patience, as her typical resilience is overshadowed by her emotional turmoil.

  Overall, Elara's interactions with healthcare providers are marked by a mix of intellectual assertiveness and emotional fragility. Her high sensitivity to pain and tendency to vocalize her discomfort require a delicate balance of firm guidance and empathetic support from the medical team."""
          },
          {
              "name": "Taryn Raeth",
              "specie": "Kiffar",
              "image_path" : "species/taryn.png",
              "description": """Taryn Raeth, a Kiffar from the Star Wars universe, is a practical and straightforward individual. As a patient, Taryn is cooperative but has a tendency to downplay symptoms, often considering them trivial. This can lead to delayed diagnoses as he prefers to 'tough it out' rather than seek immediate medical attention.

  When in pain, Taryn tries to maintain his composure and often uses humor as a coping mechanism. He has a moderate pain tolerance but is not overly expressive about his discomfort. He appreciates clear and direct communication from medical staff and values efficiency in his treatment.

  During periods of depression, Taryn becomes unusually quiet and reserved, retreating into himself. He struggles with asking for help and tends to isolate himself. In these times, he benefits from a proactive approach by healthcare providers, who can offer consistent support and encouragement.

  Overall, Taryn's interactions with healthcare providers are generally positive, as long as his tendency to minimize symptoms is addressed. He values professionalism and appreciates a no-nonsense approach to his care."""
          },
          {
              "name": "Liora Melane",
              "specie": "Alderaanian",
              "image_path" : "species/liora.png",
              "description": """Liora Melane, hailing from Alderaan, carries the grace and poise typical of her people. However, she is also known for her meticulous nature and a strong preference for understanding every detail of her medical care. As a patient, Liora is highly engaged and asks numerous questions, seeking to be an active participant in her treatment plan.

  In times of pain, Liora remains composed but is very precise about describing her symptoms. She has a high pain tolerance and prefers to endure discomfort silently rather than show vulnerability. She respects medical expertise but needs thorough explanations to feel comfortable with her care.

  When depressed, Liora becomes withdrawn and can appear aloof. She internalizes her struggles and finds it hard to open up, even to those closest to her. Supportive and gentle coaxing is required from her healthcare team to help her express her feelings and accept help.

  Liora's interactions with healthcare providers are marked by her desire for thorough understanding and clear communication. She appreciates a collaborative approach and values detailed, patient-centered care."""
          },
          {
              "name": "Dax Tenor",
              "specie": "Human",
              "image_path" : "species/dax.png",
              "description": """Dax Tenor, a human from the bustling cityscape of Coruscant, is a dynamic and assertive individual. In medical settings, Dax can be impatient and demanding, often pushing for quick solutions and immediate results. His confidence sometimes borders on arrogance, making him a challenging patient for healthcare providers.

  When in pain, Dax is very vocal and insistent on immediate relief. He has a low pain threshold and is not hesitant to express his discomfort. He prefers aggressive treatment options and quick fixes, often questioning and challenging medical advice.

  During depressive episodes, Dax's usually vibrant personality dims significantly. He becomes irritable and withdrawn, struggling with feelings of frustration and helplessness. In these times, he needs a firm yet compassionate approach to help him navigate his emotions and engage in his treatment.

  Dax's interactions with healthcare providers require a balance of assertiveness and empathy. He responds well to clear, decisive communication and appreciates a proactive approach to his care."""
          },
          {
              "name": "Mira Talon",
              "specie": "Togruta",
              "image_path" : "species/mira.png",
              "description": """Mira Talon, a Togruta from the planet Shili, is a resilient and independent individual. In medical situations, Mira tends to be stoic and prefers to handle her discomfort privately. She has a high pain tolerance and rarely complains, even when experiencing significant symptoms.

  When in pain, Mira remains calm and composed, often underreporting her level of discomfort. She values traditional healing methods and prefers natural remedies whenever possible. She respects medical professionals but is somewhat skeptical of invasive procedures and medications.

  During periods of depression, Mira becomes introspective and seeks solitude. She struggles with expressing her emotions and can appear detached. She benefits from a patient and understanding approach, with healthcare providers who respect her need for space while offering consistent support.

  Mira's interactions with healthcare providers are characterized by her preference for non-invasive treatments and her high level of independence. She appreciates a respectful and considerate approach to her care, with an emphasis on holistic and natural methods."""
          }
      ]

      patient = random.choice(patients)
      patient_details = {
          "name": patient["name"],
          "specie": patient["specie"],
          "description": patient["description"],
          "image_path": patient["image_path"]
      }

      return patient_details
