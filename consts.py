import json

# TODO: PUT YOUR OWN PATH HERE; FILE IN DISCORD UNDER RESOURCES
JSON_PATH = '/Users/wasp/patient_information.json'
data = json.load(open(JSON_PATH))
HOST = data['HOST']
PORT = int(data['PORT'])
DATABASE = data['DATABASE']
ADMINUSER = data['ADMINUSER']
ADMINPASS = data['ADMINPASS']

# options obtained from Mount Sinai Patient Race and Ethnicity Data Form
# https://www.mountsinai.org/files/MSHealth/Assets/HS/Locations/Patient%20Race%20and%20Ethnicity.pdf
PATIENT_RACES = ['White', 'Black or African American', 'American Indian or Alaska Native',
                 'Asian', 'Native Hawaiian or Pacific Islander']

# most common reasons for admission
# https://healthnewshub.org/the-top-10-reasons-people-visit-their-primary-care-physician/
ADMISSION_REASONS = ['Upper respiratory tract infection', 'Hypertension', 'Routine health maintenance',
                     'Arthritis', 'Diabetes', 'Depression or anxiety', 'Pneumonia',
                     'Middle ear infection', 'Back pain', 'Dermatitis', 'Cough']
