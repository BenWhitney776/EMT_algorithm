
class Scenario:
    def __init__(self, safety, noi, num_of_patients, gen_imp, oriented_to_person, oriented_to_place, oriented_to_time,
                 oriented_to_event, responds_to_pain, complaint, airway_patent, breathing_adequate, bleeding,
                 pulse_exists, lung_sounds, urticaria, blood_pressure, pulse_rate, respiratory_rate, pupils,
                 blood_glucose_level, temperature, oxygen_saturation, onset, provocation_palliation, quality,
                 radiation, severity, time, allergies, medications, pertinent_pmh, last_oral_intake, events,
                 signs_and_symptoms):
        self.safety = safety
        self.noi = noi
        self.num_of_patients = num_of_patients
        self.gen_imp = gen_imp
        self.oriented_to_person = oriented_to_person
        self.oriented_to_place = oriented_to_place
        self.oriented_to_time = oriented_to_time
        self.oriented_to_event = oriented_to_event
        self.responds_to_pain = responds_to_pain
        self.complaint = complaint
        self.airway_patent = airway_patent
        self.breathing_adequate = breathing_adequate
        self.bleeding = bleeding
        self.pulse_exists = pulse_exists
        self.lung_sounds = lung_sounds
        self.urticaria = urticaria  # this is an ams ss but there isn't a jvd sign and symptom just ss at the end
        self.blood_pressure = blood_pressure
        self.pulse_rate = pulse_rate
        self.respiratory_rate = respiratory_rate
        self.pupils = pupils
        self.blood_glucose_level = blood_glucose_level
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.onset = onset
        self.provocation_palliation = provocation_palliation
        self.quality = quality
        self.radiation = radiation
        self.severity = severity
        self.time = time
        self.allergies = allergies
        self.medications = medications
        self.pertinent_pmh = pertinent_pmh
        self.last_oral_intake = last_oral_intake
        self.events = events
        self.signs_and_symptoms = signs_and_symptoms  # should only be listed if ask in a body systems exam


myocardial_infarction = Scenario("yes", "chest pain", "one",
                                 "you see a 64yof clutching her chest sitting on the bleachers of a basketball court",
                                 "katie", "basketball court", "2024", "playing basketball when chest started to hurt",
                                 "yes", "chest pain", "yes", "yes", "no", "yes", "clear and equal bilaterally", "no",
                                 "180/120", "140", "25", "PEARL", "90mg/dl", "normal", "90%",
                                 "while playing basketball", "rest makes it better", "dull and squeezing",
                                 "to left arm and jaw", "10/10", "30 minutes ago", "NKA", "nitroglycerin", "CHF",
                                 "lunch one hour ago", "playing basketball", "fill this in later")


hypoglycemia = Scenario("no the patient is violent", "Altered Mental Status", "one",
                        "you see a patient sitting in a chair who appears to be angry", "Matt", "at home", "2024",
                        "I dont know what is going on", "yes", "family says he hasn't been acting right", "yes", "yes",
                        "no", "yes", "clear and equal bilaterally", "no", "150/110", "140", "24", "PEARL", "60mg/dl",
                        "low body temperature", "98%", "sudden", "time vs sugar?", "irrelevant", "none", "none",
                        "about ten minutes ago", "NKA", "insulin", "diabetes", "lunch", "vomited", "fill this in later")


# what if they need an emergency move like behind the wheel of a car not lying supine
opioid_overdose = Scenario("the scene is safe", "AMS", "one",
                           "you see a 24yom unconscious behind the driver's seat of a car", "none", "none", "none",
                           "none", "no response", "unconsciousness is apparent", "yes", "no", "no", "yes",
                           "clear and equal bilaterally", "no", "90/60", "59", "4", "pinpoint", "100mg/dl", "normal",
                           "50%", "sudden", "none", "none", "none", "none", "10 minutes ago", "NKA", "none", "none",
                           "none", "none", "fill this in later")


# what if they need to be restrained
toxin_overdose = Scenario("the scene is not safe", "AMS", "one", "you see a 16yof crying with her parents there",
                          "Rachel", "at home", "2024", "attempted suicide", "yes", "overdose on depression medication",
                          "yes", "yes", "no", "yes", "clear and equal bilaterally", "no", "normal", "tachycardia",
                          "20", "PEARL", "120mg/dl", "normal", "99%", "sudden", "none", "none", "none", "10/10",
                          "30 min ago", "NKA", "depression medication: zoloft", "depression",
                          "the depression medication", "the overdose", "signs_and_symptoms fill this in later")


# what if they're only using one to two word sentences
congestive_heart_failure = Scenario("yes", "SOB", "one", "a 60yom sitting bolt upright on a chair in the living room",
                                    "Thomas", "in my house", "2024", "I can't breath", "yes", "Short of Breath", "yes",
                                    "no", "no", "yes", "crackles and rhonchi bilaterally in lung bases", "no",
                                    "170/130", "120", "26", "PEARL", "110mg/dl", "normal", "79%", "sudden",
                                    "sitting up helps it and lying down makes it worse", "none", "none", "9/10",
                                    "30 min", "NKA", "a beta blocker, propranolol", "CHF and an MI one year ago",
                                    "lunch", "going up the steps didn't make it",
                                    "signs_and_symptoms fill this in later")


# what if they cant speak but are oriented
choking = Scenario("yes", "respiratory arrest", "one", "a child clutching their throat standing up panicking",
                   "can't speak", "can't speak", "can't speak", "can't speak", "yes", "choking", "no", "no", "no",
                   "yes", "absent", "no", "normal", "130bpm", "zero", "PEARL", "90mg/dl", "normal", "860%", "sudden",
                   "none", "none", "none", "none", "5 minutes ago", "NKA", "none", "none", "lunch", "eating lunch",
                   "signs_and_symptoms fill this in later")


asthma = Scenario("yes", "SOB", "one", "a 15yom sitting on the sidelines at a football game", "Jake",
                  "high school football field", "2024", "SOB", "yes", "SOB", "yes", "no", "no", "yes", "wheezing",
                  "no", "120/80mmhg", "125", "26", "PEARL", "92mg/dl", "normal", "87%", "sudden",
                  "exertion makes it worse and tripodding makes it better", "none", "none", "4/10 chest tightness",
                  "30 minutes ago", "pollen", "albuterol", "asthma", "lunch", "physical exertion during the game",
                  "signs and symptoms fill in later")


anaphylaxis = Scenario("yes", "SOB", "one", "42yof wheezing with angio-edema", "Kelly", "in front yard", "2024",
                       "stung by a bee", "yes", "stung by a bee", "yes", "no", "no", "yes", "wheezing bilaterally",
                       "yes", "88/60mmhg", "120", "33", "PEARL", "92mg/dl", "normal", "80%", "sudden", "none", "none",
                       "none", "none", "10 minutes ago", "bees", "epinephrine", "none", "lunch", "stung by a bee",
                       "signs_and_symptoms fill this in later")


# would they be coughing
chronic_obstructive_pulmonary_disease = Scenario("yes", "wheezing", "one", "you see a 54yom wheezing and coughing",
                                                 "Mike", "at the park", "2024",
                                                 "became short of breath while smoking a cigarette", "yes", "SOB",
                                                 "yes", "no", "no", "yes", "wheezing bilaterally", "no", "110/70",
                                                 "pulse_rate", "24", "PEARL", "86mg/dl", "normal", "76%", "sudden",
                                                 "none", "none", "none", "none", "20 minutes ago", "NKA", "albuterol",
                                                 "COPD", "dinner", "smoking a cigarette",
                                                 "signs_and_symptoms fill this in later")


# because I can do something about the above emergencies


class Medications:
    def __init__(self, indications, contraindications, route, amount, medication_name, prescribed, expiration,
                 documentation):
        self.indications = indications
        self.contraindications = contraindications
        self.route = route
        self.amount = amount
        self.medication_name = medication_name
        self.prescribed = prescribed
        self.expiration = expiration
        self.documentation = documentation
        # what will I put that is different for documentation should a method return a string
        # with the documentation using the other information

    def medication_delivery(self):
        print(f"{self.medication_name} is indicated because of it's indications which are...{self.indications}.")
        print(f"{self.medication_name} is not contraindicated, it's contraindications are...{self.contraindications}.")
        print(f"I will deliver this medication {self.route}.")
        print(f"I will deliver {self.amount} of this medication.")
        print(f"The medication name is {self.medication_name}")
        if self.prescribed == "yes":
            print("This medication belongs to my patient.")
        else:
            print("This medication does not belong to my patient.")  # this only matters for epi and inhalers fix this
            print("I will not give this medication.")
            return
        if self.expiration == "not expired":
            print("This medication is not expired.")
        else:
            print("This medication is expired.")
            print("I will not give this medication.")
            return
        print(f"I am now going to administer {self.medication_name}.")
        print(self.documentation)


# doses change based on age and expiration and prescribed differ patient to patient so that needs fixed
epinephrine = Medications("anaphylaxis", "not anaphylaxis", "Intra Muscular", ".3mg", "epinephrine", "yes",
                          "not expired", "documentation")
cpap = Medications("fluid in the lungs causing crackles from CHF or COPD wheezing maybe?",
                   "hypotension, pneumothorax, respiratory failure, nausea / vomiting, claustrophobia, poor mask seal",
                   "inhaled?", "5-10 cm of h20?", "CPAP", "irrelevant", "not expired", "documentation")
albuterol = Medications("wheezing from asthma or bronchitis?", "no need, allergy", "inhaled", "2.5mg", "albuterol",
                        "yes", "not expired", "documentation")
aspirin = Medications("cardiac chest pain", "NSAID allergy", "chew it", "324mg that is four baby aspirin each 81mg",
                      "aspirin", "yes", "not expired", "documentation")
nitroglycerin = Medications("cardiac chest pain", "systolic BP under 100mmhg, ED meds", "sublingual", "0.4mg",
                            "nitroglycerin", "yes", "not expired", "documentation")
oral_glucose = Medications("low blood sugar/ hypoglycemia under 70bgl",
                           "the patient can't protect the airway or follow basic commands", "buccal", "15 grams",
                           "oral glucose", "yes", "not expired", "documentation")
activated_charcoal = Medications("numerous medication overdoses", "corrosives and caustics", "oral", "25-50 grams",
                                 "activated charcoal", "yes", "not expired", "documentation")
naloxone = Medications("opioid overdose as defined by respiratory depression", "none?", "intra-nasally",
                       "2mg (one up each nostril)", "naloxone/ narcan", "yes", "not expired", "documentation")
# oxygen = Medications(), has different flow rates and delivery devices


def scene_safety(scenario):
    print("Is the scene safe?")
    safe = scenario.safety
    print(safe)
    if safe == "yes":
        print("I'm entering the scene.")
    else:
        print("I will call additional resources to make the scene safe then I will enter the scene.")


def scene_size_up(scenario):
    print("My BSI is on.")
    scene_safety(scenario)
    print("What is the MOI or NOI?")  # here is when I could choose the trauma or medical assessment
    print(scenario.noi)
    print("How many patients do I have?")
    print(scenario.num_of_patients)
    print("I'm calling for additional resources at this time.")  # In real life I wouldn't always call for ALS
    print("Now I'm considering stabilization of the C-spine.")  # do this based on MOI


def orientation_questions(scenario):
    oriented = 1

    print("Where are you?")
    print(scenario.oriented_to_place)
    location = input("Makes Sense? YES or NO?: ")
    if location.lower() == "yes":
        oriented += 1

    print("What year is it?")
    print(scenario.oriented_to_time)
    year = input("Makes Sense? YES or NO?: ")
    if year.lower() == "yes":
        oriented += 1

    print("Why did you call 911?")
    print(scenario.oriented_to_event)
    event = input("Makes Sense? YES or NO?: ")
    if event.lower() == "yes":
        oriented += 1

    return oriented


def level_of_consciousness(scenario):
    print("Hey! What is your name?")
    print(scenario.oriented_to_person)
    name = input("ALERT, VERBAL, or NO RESPONSE?: ")
    if name.lower() == "alert":
        orientation = orientation_questions(scenario)
        return f"My patient is A&Ox{orientation} and their airway is patent because they are speaking to me."
    if name.lower() == "verbal":
        return "My patient is verbal."
    print("Because my patient is not alert or verbal I will do a sternal rub or trap pinch.")
    # painful stimulus location depends on where there is injury
    print(scenario.responds_to_pain)
    if scenario.responds_to_pain == "yes":
        return "My patient is responsive to painful stimulus."
    return "My patient is unresponsive."


def chief_complaint(scenario):
    print("What is the patient's chief complaint?")
    return scenario.complaint


def cpr():
    print("I tell my partner to get the AED.")
    print("I'm starting chest compressions at a rate of 100-120 per minute and "
          "a depth of 2 inches allowing the chest to recoil fully.")
    print("Now that the AED arrived I am attaching the pads turning it on and plugging it in.")
    print("I am now ordering everyone to clear the patient as the AED decides weather or not the rhythm is shock-able")
    print("I will now resume CPR for five cycles of 30:2 for two minutes")
    print("repeat until there is a pulse or ACLS arrives and declares death")
    # check in mouth for foreign body airway obstructions during compressions


def airway(loc, scenario):
    if "patent" in loc:
        return
    print("I'm going to open the airway with a head-tilt-chin-lift or jaw-thrust "
          "depending on if I found them unresponsive or they sustained trauma")
    print("I am now checking the airway for secretions.")
    if scenario.airway_patent == "yes":
        print("There are no secretions in the airway.")
    else:
        print("The airway is full of secretions.")
        print("I am now suctioning the airway only on the way out, visualizing the distal end, side to side, and for "
              "no longer than ten seconds.")
    if "unresponsive" in loc:
        print("Because my patient is unresponsive and without a gag reflex "
              "or any other contraindications to the use of an OPA "
              "I'm going to insert an OPA at this time measuring it from the corner of the mouth to the ear lobe")
    else:  # patient is responsive to verbal or painful stimulus
        print("Because my patient has a gag reflex but needs airway management if it isn't contraindicated "
              "for another reason I will insert an NPA at this time.")


def breathing(scenario):
    print("I'm assessing the adequacy of breathing by seeing chest rise and fall, and if breathing is labored as "
          "seen by nasal flaring, wheezing, stridor, retractions, pursed lip breathing, and tripod positioning.")
    if scenario.breathing_adequate == "yes" and 8 < int(scenario.respiratory_rate) < 30:
        print("Breathing is adequate")
        print("Because breathing is adequate I will oxygenate my patient via a non-rebreather mask at 15 lpm.")
    else:
        print("Breathing is inadequate.")
        print("Because breathing is inadequate I will use a BVM to ventilate my patient at a rate of 10-12 bpm.")


def circulation(scenario, loc):
    print("Do I see any major bleeding when I do a blood sweep?")
    if scenario.bleeding == "yes":
        print("There is major bleeding.")
        print("I'm stopping the bleeding with direct pressure.")
        print("If the bleeding doesn't stop I will escalate to a tourniquet.")
    else:
        print("No major bleeding is present.")
    if "unresponsive" in loc:
        print("I'm checking a carotid pulse for if it exists?")
        if scenario.pulse_exists == "yes":
            print("There is a pulse.")
        else:
            print("No pulse exists.")
            cpr()
    else:
        print("I'm checking a radial pulse for "
              "rate (fast or slow), "
              # "rhythm (regular or irregular), and "  # not assessed in the primary assessment
              "quality (strong or weak).")
        print("I'm assessing skin Color, Temperature, and Condition")
        print("I'm laying my patient supine to help manage shock if it doesn't cause greater respiratory distress.")
        # put them in a supine position


def manage_life_threats(loc, scenario):
    if "unresponsive" in loc:
        circulation(scenario, loc)
        airway(loc, scenario)
        breathing(scenario)
    else:  # shouldn't I be doing circulation first if there is a major bleed and they are conscious
        airway(loc, scenario)
        breathing(scenario)
        circulation(scenario, loc)


def primary_assessment(scenario):
    print("I'm forming my general impression, what do I see?")
    print(scenario.gen_imp)
    print("I'm taking note of if they are "
          # position
          "tripoding because that could indicate respiratory distress, "
          "any guarding that could show pain, "
          # behavior
          "if they are combative which could jepordize scene safety or indicate agitated delirium or hypoglycemia, "
          "tracking me with their eyes which would show they have a pulse and are alert, "
          "if they are crying as an infant, "
          "if they are actively seizing, "
          # breathing
          "if they are Short Of Breath, "
          # skin
          "skin color and condition like diaphoresis or pallor, "
          # demographic risk factors
          "their age, sex, and BMI which can be risk factors for certain conditions or presentations of conditions, "
          # environmental risk factors
          "if the environment is hot or cold or very high altitude")
    conscious = level_of_consciousness(scenario)
    print(conscious)
    cc = chief_complaint(scenario)
    print(cc)
    manage_life_threats(conscious, scenario)
    print("This is a high priority patient and I am going to transport them ASAP")
    # Do I transport now? No it is at the end of the secondary assessment
    return cc


# vital signs below

def vital_signs(scenario):
    # baseline vitals
    print("I'm now getting a blood pressure, what is it?")
    print(scenario.blood_pressure)
    print("I'm now getting a respiratory rate by seeing chest rise and fall, what is it?")
    print(scenario.respiratory_rate)
    print("I'm now getting a pulse rate, what is it?")
    print(scenario.pulse_rate)
    # I could say 0 and derive pulse_exists from pulse rate and
    # also have pulse for carotid but not radial

    # more vitals
    print("I'm now assessing if the pupils are PEARL or pinpoint, what do I see?")
    print(scenario.pupils)
    print("I'm now getting a BGL, what is the BGL?")
    print(scenario.blood_glucose_level)
    print("I'm now taking a temperature, what is it?")
    print(scenario.temperature)
    print("I'm now getting an O2 sat, what is it?")
    print(scenario.oxygen_saturation)
    # if from the general impression I see the patient is a kid and not cold or wearing nail polish
    # I can also check capillary refill at this time to make sure it is under 2 seconds


# history taking below

def opqrst_sample_history(scenario):  # separate these so I can only obtain a SAMPLE history for trauma assessments
    # OPQRST HPI
    print("Did the pain start suddenly or gradually?")  # onset
    print(scenario.onset)
    print("Does anything make the pain better or worse")  # provocation/ palliation
    print(scenario.provocation_palliation)
    print("Can you describe the quality of the pain?")  # quality
    print(scenario.quality)
    print("Does the pain go anywhere?")  # radiation
    print(scenario.radiation)
    print("on a scale of 1-10 with ten being the most painful, how bad is the pain?")
    print(scenario.severity)
    print("how long have you been experiencing this pain?")
    print(scenario.time)
    # SAMPLE medical history
    # signs and symptoms will go here or in the secondary assessment
    print("Do you have any allergies?")  # allergies
    print(scenario.allergies)
    print("Do you currently take any medications")  # medications
    print(scenario.medications)
    print("Do you have any relevant medical history?")  # pertinent PMH
    print(scenario.pertinent_pmh)
    print("What did you eat last, and when did you last eat?")  # last oral intake
    print(scenario.last_oral_intake)
    print("What were you doing when the pain started?")  # events
    print(scenario.events)


# secondary assessment below

def chest_pain_differential():  # examination of body systems with these questions
    # these questions are derived from the union of all hallmark categories in the signs and symptoms section
    # these questions examine the cardiopulmonary system (cardiovascular and respiratory systems)
    # cardiac tamponade has beck's triad which is hypotension, JVD, and muffled heart sounds
    print("Are the heart sounds muffled? This could indicate cardiac tamponade.")
    print("Is the pulse pressure narrow? This could indicate cardiac tamponade.")
    print("Is there JVD? This could indicate cardiac tamponade or pneumothorax.")
    print("Is the blood pressure different in both arms by 15mmHg or higher? This could indicate aortic dissection.")
    print("Is there a cough of blood or frothy pink sputum? This could indicate pulmonary embolism.")
    print("Is there nausea or vomiting? Hematemesis could indicate esophageal rupture.")
    print("S/S of hypovolemic shock? That could indicate esophageal rupture or AAA")  # this isn't broken down enough
    print("Is chest rise and fall unequal? That could indicate pneumothorax?")
    print("Are breaths sounds diminished on one side? Which could indicate pneumothorax.")
    print("Is the trachea deviated? Which could indicate pneumothorax.")
    print("Is there abdominal pain? Which could indicate AAA.")
    print("Is there a pulsating abdominal mass? Which could indicate AAA.")


def shortness_of_breath_differential():
    # these questions examine the respiratory/pulmonary system
    print("Are crackles or rhonchi heard bilaterally in the lung bases? This could indicate CHF.")
    print("Is wheezing heard? That could indicate asthma, anaphylaxis, or COPD.")
    print("Does the chest feel tight? That could indicate asthma.")
    print("Are there hives? That could indicate anaphylaxis.")
    print("Is the voice hoarse or can I hear Stridor? That can indicate anaphylaxis.")
    print("Is there pursed lip breathing? That could indicate COPD (emphysema).")
    print("sharp pain that increases as breath? pleuritic pain can indicate pneumonia.")
    print("Is there a productive cough? This could indicate pneumonia.")
    print("Is there any JVD? That could indicate pneumothorax.")
    print("Is there any diminished or absent lung sounds on one side? That could indicate pneumothorax.")
    print("Is there any unequal chest rise and fall? That could indicate pneumothorax.")
    print("Is there any tracheal deviation? That could indicate pneumothorax.")
    print("Is there a seal bark cough? That could indicate croup.")
    print("Is there any drooling? That could indicate epiglottitis.")


def altered_mental_status_differential():
    # these questions examine the neurological system
    print("Do a BE FAST exam, for a stroke.")
    print("Was there a seizure? This could show epilepsy or other things in the SNOT differential.")
    print("Is there shaking/ tremors? This could indicate the DTs")
    print("Are there crackles or Rhonchi? That could indicate pneumonia.")
    print("Is there a headache? That could indicate HACE.")
    print("Is there a combination of irregular RR, bradycardia, and hypertension? "
          "Cushing's triad could indicate head trauma")


def secondary_assessment(complaint):
    if complaint == "chest pain":
        chest_pain_differential()
    elif complaint == "shortness of breath":
        shortness_of_breath_differential()
    else:  # AMS differential
        altered_mental_status_differential()
    # depending on chief complaint use different differentials and perform different exams of different body systems
    field_impression = input("My field impression is... ").lower()
    if field_impression in ["mi", "myocardial infarction", "heart attack", "angina", "acs"]:
        aspirin.medication_delivery()
        nitroglycerin.medication_delivery()
    elif field_impression == "hypoglycemia":
        oral_glucose.medication_delivery()
    elif field_impression == "opioid overdose":
        naloxone.medication_delivery()
    elif field_impression == "toxin overdose":
        activated_charcoal.medication_delivery()
    elif field_impression == "CHF":
        cpap.medication_delivery()
    elif field_impression == "anaphylaxis":
        epinephrine.medication_delivery()
    elif field_impression in ["asthma", "copd"]:
        albuterol.medication_delivery()
    else:
        print("My patient is on oxygen and I called ALS and am transporting my patient.")
        print("But other than that there is no more specific treatment I can do for this patient.")
    # get a field impression in here and based on that treat with medications


# reassessment below

def reassessment():
    print("I will reassess my patient every 5 minutes because they are a high priority patient.")
    print("I will begin the reassessment by repeating the primary assessment.")  # should ABC problems randomly pop up
    print("Then I will trend vitals.")  # should I include repeat sets of vitals in the scenario
    print("Then I will check my interventions all the way to the hospital")
    # should the focussed assessment be in here


def medical_assessment(scenario):  # should vital signs be after the secondary assessment
    scene_size_up(scenario)
    cc = primary_assessment(scenario)
    vital_signs(scenario)
    opqrst_sample_history(scenario)
    secondary_assessment(cc)  # treatment with medications can go here and contacting medical command to give meds
    reassessment()
    # radio report can go here or transfer of care?


scenarios_list = [myocardial_infarction,
                  opioid_overdose,
                  hypoglycemia,
                  toxin_overdose,
                  congestive_heart_failure,
                  asthma,
                  anaphylaxis,
                  choking,
                  chronic_obstructive_pulmonary_disease]


for each_scenario in scenarios_list:
    input()
    print("START")
    medical_assessment(each_scenario)
    print("END")
    print("")
    print("")


# is the bgl normal and what are the hallmark vitals then should I use booleans for yes and no questions
# left lateral recumbent position if pregnant over 28 weeks
# exams for each body system
