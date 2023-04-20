# DO NOT COMMIT THIS LINK TO THE REPO OR ANYONE WHO GRABS IT
# CAN MESS WITH DATA IN THE DB
# will look into a more permanent solution.
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


# all huntsville zip codes
# https://www.city-data.com/zipmaps/Huntsville-Alabama.html
HUNTSVILLE_ZIP_CODES = ['35613', '35649', '35671', '35741', '35748', '35749', '35756', '35757', '35758',
                        '35759', '35763', '35773', '35801', '35802', '35803', '35805', '35806', '35808',
                        '35810', '35811', '35816', '35824', '35896']

# marital statuses
# https://www.cdc.gov/nchs/hus/sources-definitions/marital-status.htm
MARITAL_STATUSES = ['Married', 'Unmarried']


# employment statuses
EMPLOYMENT_STATUSES = ['Employed', 'Unemployed and actively seeking work', 'Student',
                       'Long-term sick or disabled', 'Homemaker', 'Not seeking work',
                       'Unpaid voluntary work', 'Retired', 'Not stated']

# insurance providers
# https://www.insurancebusinessmag.com/us/news/life-insurance/top-10-health-insurance-companies-in-the-us-212292.aspx
INSURANCE_PROVIDERS = ['UnitedHealth', 'Anthem, Inc.', 'Centene Corp', 'Humana', 'CVS', 'HCSC', 'Cigna Health',
                       'Molina Healthcare, Inc.', 'Independence Health Group', 'None']
