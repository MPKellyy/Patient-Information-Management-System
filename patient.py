import names
import random
import numpy as np
from consts import PATIENT_RACES, ADMISSION_REASONS, HUNTSVILLE_ZIP_CODES, MARITAL_STATUSES, \
    EMPLOYMENT_STATUSES, INSURANCE_PROVIDERS
import datetime
from util import calculate_current_age, literal


class Patient:
    """This class will only be interfaced with through the Database class -
    never instantiated on its own.
    Use cases:
        1. Create a patient using admin-specified data. (MOSTLY WORKING)
        2. Create a patient using partially admin-specified data, otherwise randomly-generated. (KINDA WORKING)
        3. Create a patient using completely randomly-generated data. (WORKING!)
    """

    def __init__(self, patientID=None, firstname=None, lastname=None, room_number=None, bed_number=None,
                 sex=None, age=None, height=None, weight=None, race=None, dob=None, care_provider=None,
                 current_status=None, medical_risks=None, allowed_visitors=None, restricted_visitors=None,
                 admission_date=None, admission_reason=None, discharge_date=None, emergency_contacts=None,
                 family_doctor=None, medical_history=None, photo=None, phone_number=None, ssn=None,
                 doctor_notes=None, nurse_notes=None, address=None, prescriptions=None, procedures=None,
                 building=None, marital_status=None, employment_status=None, employer=None,
                 insurance_provider=None, insurance_contact=None, invoice=None, patient_amount_paid=None,
                 insurance_amount_paid=None, pay_plan=None, pay_history=None, insurance_account_num=None,
                 charge_history=None, insurance_num=None, edited=None, data=None):

        if not data:
            data = {}
        self.data = data

        # patient_medical attributes
        self.patientID = patientID
        self.firstname = firstname
        self.lastname = lastname
        self.room_number = room_number
        self.bed_number = bed_number
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.race = race
        self.dob = dob
        self.care_provider = care_provider
        self.current_status = current_status
        self.medical_risks = medical_risks
        self.allowed_visitors = allowed_visitors
        self.restricted_visitors = restricted_visitors
        self.admission_date = admission_date
        self.admission_reason = admission_reason
        self.discharge_date = discharge_date
        self.emergency_contacts = emergency_contacts
        self.family_doctor = family_doctor
        self.medical_history = medical_history
        self.photo = photo
        self.phone_number = phone_number
        self.ssn = ssn
        self.doctor_notes = doctor_notes
        self.nurse_notes = nurse_notes
        self.address = address
        self.prescriptions = prescriptions
        self.procedures = procedures
        self.building = building

        # patient_accounting attributes
        self.marital_status = marital_status
        self.employment_status = employment_status
        self.employer = employer
        self.insurance_provider = insurance_provider
        self.insurance_contact = insurance_contact
        self.invoice = invoice
        self.patient_amount_paid = patient_amount_paid
        self.insurance_amount_paid = insurance_amount_paid
        self.pay_plan = pay_plan
        self.pay_history = pay_history
        self.insurance_account_num = insurance_account_num
        self.charge_history = charge_history
        self.insurance_num = insurance_num

        # keep track of edits
        self.changes = []

        # other attributes that are not part of general patient data
        self.height_in_inches = None
        self.admission_date_object = None
        self.discharge_date_object = None

        if self.data:
            self._parse_database_input()
            self.changes = []
            return
        else:
            self.data = {}

        empty_args = True
        for key in list(self.data.keys())[1:]:
            # if any key other than patientID return a value, do not fill with random patient data
            # else, create random data automatically
            if self.data[key]:
                empty_args = False

        if empty_args:
            # if no inputs contain data, create a random patient
            self.create_random_patient_data()

        # once patient is initialized, create a change log
        self.changes = []

    def create_random_patient_data(self):
        # initialize dictionary
        self._refresh_dict()

        # sex is used to seed name, then attributes are sequentially generated
        self.randomize_all_missing_data()

        # add all data to dict
        self._refresh_dict()

    def randomize_all_missing_data(self):
        for key in list(self.data.keys())[1:]:
            if not self.data[key] or self.data[key] == 'None' or self.data[key] == 'NULL':
                try:
                    exec("self._set_random_" + key + "()")
                except AttributeError:
                    exec("self.set_" + key + "(" + "\'NULL\'" + ")")

    def get_full_name(self):
        if self.firstname and self.lastname:
            return self.firstname + " " + self.lastname
        else:
            return 'Unknown'

    def get_attributes(self):
        return self.data.keys()

    def get_patient_data_as_dict(self):
        return self.data

    def get_patient_medical_data(self):
        return {'patientID': self.patientID,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'room_number': self.room_number,
                'bed_number': self.bed_number,
                'sex': self.sex,
                'age': self.age,
                'height': self.height,
                'weight': self.weight,
                'race': self.race,
                'dob': self.dob,
                'care_provider': self.care_provider,
                'current_status': self.current_status,
                'medical_risks': self.medical_risks,
                'allowed_visitors': self.allowed_visitors,
                'restricted_visitors': self.restricted_visitors,
                'admission_date': self.admission_date,
                'admission_reason': self.admission_reason,
                'discharge_date': self.discharge_date,
                'emergency_contacts': self.emergency_contacts,
                'family_doctor': self.family_doctor,
                'medical_history': self.medical_history,
                'photo': self.photo,
                'phone_number': self.phone_number,
                'ssn': self.ssn,
                'doctor_notes': self.doctor_notes,
                'nurse_notes': self.nurse_notes,
                'address': self.address,
                'prescriptions': self.prescriptions,
                'procedures': self.procedures,
                'building': self.building,
                }

    def get_patient_accounting_data(self):
        return {'accountingID': self.patientID,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'address': self.address,
                'marital_status': self.marital_status,
                'employment_status': self.employment_status,
                'employer': self.employer,
                'insurance_provider': self.insurance_provider,
                'insurance_contact': self.insurance_contact,
                'invoice': self.invoice,
                'patient_amount_paid': self.patient_amount_paid,
                'insurance_amount_paid': self.insurance_amount_paid,
                'pay_plan': self.pay_plan,
                'pay_history': self.pay_history,
                'phone_number': self.phone_number,
                'insurance_account_num': self.insurance_account_num,
                'charge_history': self.charge_history,
                'insurance_num': self.insurance_num,
                }

    # setters........ so many of them

    def set_firstname(self, new):
        if self.firstname is not new:
            self.firstname = new
            self.data['firstname'] = new
            self.changes.append('firstname')

    def set_lastname(self, new):
        if self.lastname is not new:
            self.lastname = new
            self.data['lastname'] = new
            self.changes.append('lastname')

    def set_room_number(self, new):
        if self.room_number is not new:
            self.room_number = new
            self.data['room_number'] = new
            self.changes.append('room_number')

    def set_bed_number(self, new):
        if self.bed_number is not new:
            self.bed_number = new
            self.data['bed_number'] = new
            self.changes.append('bed_number')

    def set_sex(self, new):
        if self.sex is not new:
            self.sex = new
            self.data['sex'] = new
            self.changes.append('sex')

    def set_age(self, new):
        if self.age is not new:
            self.age = new
            self.data['age'] = new
            self.changes.append('age')

    def set_height(self, new):
        if self.height is not new:
            self.height = new
            self.data['height'] = new
            self.changes.append('height')

    def set_weight(self, new):
        if self.weight is not new:
            self.weight = new
            self.data['weight'] = new
            self.changes.append('weight')

    def set_race(self, new):
        if self.race is not new:
            self.race = new
            self.data['race'] = new
            self.changes.append('race')

    def set_dob(self, new):
        if self.dob is not new:
            self.dob = new
            self.data['dob'] = new
            self.changes.append('dob')

    def set_care_provider(self, new):
        if self.care_provider is not new:
            self.care_provider = new
            self.data['care_provider'] = new
            self.changes.append('care_provider')

    def set_current_status(self, new):
        if self.current_status is not new:
            self.current_status = new
            self.data['current_status'] = new
            self.changes.append('current_status')

    def set_medical_risks(self, new):
        if self.medical_risks is not new:
            self.medical_risks = new
            self.data['medical_risks'] = new
            self.changes.append('medical_risks')

    def set_allowed_visitors(self, new):
        if self.allowed_visitors is not new:
            self.allowed_visitors = new
            self.data['allowed_visitors'] = new
            self.changes.append('allowed_visitors')

    def set_restricted_visitors(self, new):
        if self.restricted_visitors is not new:
            self.restricted_visitors = new
            self.data['restricted_visitors'] = new
            self.changes.append('restricted_visitors')

    def set_admission_date(self, new):
        if self.admission_date is not new:
            self.admission_date = new
            self.data['admission_date'] = new
            self.changes.append('admission_date')

    def set_admission_reason(self, new):
        if self.admission_reason is not new:
            self.admission_reason = new
            self.data['admission_reason'] = new
            self.changes.append('admission_reason')

    def set_discharge_date(self, new):
        if self.discharge_date is not new:
            self.discharge_date = new
            self.data['discharge_date'] = new
            self.changes.append('discharge_date')

    def set_emergency_contacts(self, new):
        if self.emergency_contacts is not new:
            self.emergency_contacts = new
            self.data['emergency_contacts'] = new
            self.changes.append('emergency_contacts')

    def set_family_doctor(self, new):
        if self.family_doctor is not new:
            self.family_doctor = new
            self.data['family_doctor'] = new
            self.changes.append('family_doctor')

    def set_medical_history(self, new):
        if self.medical_history is not new:
            self.medical_history = new
            self.data['medical_history'] = new
            self.changes.append('medical_history')

    def set_photo(self, new):
        if self.photo is not new:
            self.photo = new
            self.data['photo'] = new
            self.changes.append('photo')

    def set_phone_number(self, new):
        if self.phone_number is not new:
            self.phone_number = new
            self.data['phone_number'] = new
            self.changes.append('phone_number')

    def set_ssn(self, new):
        if self.ssn is not new:
            self.ssn = new
            self.data['ssn'] = new
            self.changes.append('ssn')

    def set_doctor_notes(self, new):
        if self.doctor_notes is not new:
            self.doctor_notes = new
            self.data['doctor_notes'] = new
            self.changes.append('doctor_notes')

    def set_nurse_notes(self, new):
        if self.nurse_notes is not new:
            self.nurse_notes = new
            self.data['nurse_notes'] = new
            self.changes.append('nurse_notes')

    def set_address(self, new):
        if self.address is not new:
            self.address = new
            self.data['address'] = new
            self.changes.append('address')

    def set_prescriptions(self, new):
        if self.prescriptions is not new:
            self.prescriptions = new
            self.data['prescriptions'] = new
            self.changes.append('prescriptions')

    def set_procedures(self, new):
        if self.procedures is not new:
            self.procedures = new
            self.data['procedures'] = new
            self.changes.append('procedures')

    def set_building(self, new):
        if self.building is not new:
            self.building = new
            self.data['building'] = new
            self.changes.append('building')

    def set_marital_status(self, new):
        if self.marital_status is not new:
            self.marital_status = new
            self.data['marital_status'] = new
            self.changes.append('marital_status')

    def set_employment_status(self, new):
        if self.employment_status is not new:
            self.employment_status = new
            self.data['employment_status'] = new
            self.changes.append('employment_status')

    def set_employer(self, new):
        if self.employer is not new:
            self.employer = new
            self.data['employer'] = new
            self.changes.append('employer')

    def set_insurance_provider(self, new):
        if self.insurance_provider is not new:
            self.insurance_provider = new
            self.data['insurance_provider'] = new
            self.changes.append('insurance_provider')

    def set_insurance_contact(self, new):
        if self.insurance_contact is not new:
            self.insurance_contact = new
            self.data['insurance_contact'] = new
            self.changes.append('insurance_contact')

    def set_invoice(self, new):
        if self.invoice is not new:
            self.invoice = new
            self.data['invoice'] = new
            self.changes.append('invoice')

    def set_patient_amount_paid(self, new):
        if self.patient_amount_paid is not new:
            self.patient_amount_paid = new
            self.data['patient_amount_paid'] = new
            self.changes.append('patient_amount_paid')

    def set_insurance_amount_paid(self, new):
        if self.insurance_amount_paid is not new:
            self.insurance_amount_paid = new
            self.data['insurance_amount_paid'] = new
            self.changes.append('insurance_amount_paid')

    def set_pay_plan(self, new):
        if self.pay_plan is not new:
            self.pay_plan = new
            self.data['pay_plan'] = new
            self.changes.append('pay_plan')

    def set_pay_history(self, new):
        if self.pay_history is not new:
            self.pay_history = new
            self.data['pay_history'] = new
            self.changes.append('pay_history')

    def set_insurance_account_num(self, new):
        if self.insurance_account_num is not new:
            self.insurance_account_num = new
            self.data['insurance_account_num'] = new
            self.changes.append('insurance_account_num')

    def set_charge_history(self, new):
        if self.charge_history is not new:
            self.charge_history = new
            self.data['charge_history'] = new
            self.changes.append('charge_history')

    def set_insurance_num(self, new):
        if self.insurance_num is not new:
            self.insurance_num = new
            self.data['insurance_num'] = new
            self.changes.append('insurance_num')

    # methods for adding to 'list' fields
    # def add_doctor_note(self):
    #

    # private methods

    def _parse_database_input(self):
        # TODO: complete this function
        for key in list(self.data.keys())[1:]:
            if str(self.data[key]) == 'b\'NULL\'':
                exec("self.set_" + key + "(" + str(self.data[key]) + ")")
            else:
                exec("self.set_" + key + "(" + literal(str(self.data[key])) + ")")
        pass

    def _set_random_firstname(self):
        # make sure sex has been set
        if not self.sex:
            self._set_random_sex()

        self.set_firstname(names.get_first_name(gender='male' if self.sex == 'M' else 'female'))

    def _set_random_lastname(self):
        self.set_lastname(names.get_last_name())

    def _set_random_sex(self):
        self.set_sex(random.choice(['F', 'M']))

    def _set_random_room_number(self):
        self.set_room_number(random.randint(1, 50))

    def _set_random_bed_number(self):
        self.set_bed_number(random.randint(1, 250))

    def _set_random_age(self):
        # setting a random age changes the date of birth automatically

        # generate random number of years and days old in range of ages 0 to 100
        rand_years = (random.randint(0, 99))
        rand_days = random.randint(0, 365)

        # use rand values to generate date of birth
        birthdate = datetime.datetime.now() - datetime.timedelta(days=(365 * rand_years) + rand_days)

        # calculate age based on birthdate
        self.set_age(calculate_current_age(birthdate))
        self.set_dob(birthdate.strftime("%Y-%m-%d"))

    def _set_random_dob(self):
        # setting a random date of birth will choose one within the age of the patient
        # if age has been set, otherwise will generate random age as well.

        if not self.age:
            self._set_random_age()
            return

        # generate random birthday within a year of their age
        rand_days = random.randint(0, 364)

        # use rand values to generate date of birth
        birthdate = datetime.datetime.now() - datetime.timedelta(days=(365 * self.age) + rand_days)

        # calculate age based on birthdate
        self.set_dob(birthdate.strftime("%Y-%m-%d"))

    def _set_random_height(self):
        # make sure age and sex has been set:
        if not self.age:
            self._set_random_age()
        if not self.sex:
            self._set_random_sex()

        if self.age <= 14:
            # formula to calculate average height of minor based on their sex
            average_height = round(28 + (self.age * (1.95 if self.sex == 'F' else 2.2)))
        else:
            # average height of adult based on their sex
            average_height = 64 if self.sex == 'F' else 69

        # generate random height using age/sex mean and normal distribution
        self.height_in_inches = round(np.random.normal(loc=average_height, scale=2, size=1)[0])
        self.set_height(str(self.height_in_inches // 12) + "-" + str(self.height_in_inches % 12))

    def _set_random_weight(self):
        # make sure height has been set:
        if not self.height:
            self._set_random_height()

        # mean BMI = 26.55
        avg_bmi = 26.55

        # take random value from normal distribution of BMIs to pick random weight
        # that makes sense given height
        random_bmi = round(np.random.normal(loc=avg_bmi, scale=5, size=1)[0])

        # bmi = (weight (lbs) / height (in) ^ 2) * 703, therefore =>
        # weight = (bmi * height (in) ^ 2) / 703
        self.set_weight(str(round(random_bmi * (self.height_in_inches ** 2) / 703)) + ' lbs')

    def _set_random_race(self):
        self.set_race(random.choice(PATIENT_RACES))

    def _set_random_care_provider(self):
        # TODO: set this to a nurse/doctor in the system instead of just a random name
        self.set_care_provider(names.get_full_name())

    def _set_random_admission_date(self):
        # note: also impacts 'current status' as of now

        # if no discharge date has been set, generate a random admission date
        if not self.discharge_date_object:
            # pick random date in the last 5 years for admission
            rand_years = random.randint(0, 4)
            rand_days = random.randint(0, 365)
            admission_date = datetime.datetime.now() - datetime.timedelta(days=(365 * rand_years) + rand_days)

        # if discharge date has been set, pick one that makes sense (around 0 to 9 days before)
        else:
            admission_date = self.discharge_date - datetime.timedelta(days=random.randint(0, 9))

        self.set_admission_date(admission_date.strftime("%Y-%m-%d"))
        self.admission_date_object = admission_date

    def _set_random_discharge_date(self):
        # note: also impacts 'current status' as of now

        # if no admission date set, set admission date
        if not self.admission_date_object:
            self._set_random_admission_date()

        # pick random date after admission date (around 0 to 9 days after)
        discharge_date = self.admission_date_object + datetime.timedelta(days=random.randint(0, 9))

        # set status based on discharge date
        if discharge_date < datetime.datetime.today():
            self.set_discharge_date(discharge_date.strftime("%Y-%m-%d"))
            self.discharge_date_object = discharge_date
            self.set_current_status('Discharged')
        else:
            self.set_discharge_date(None)
            self.set_current_status('Admitted')

    def _set_random_admission_reason(self):
        self.set_admission_reason(random.choice(ADMISSION_REASONS))

    def _set_random_emergency_contacts(self):
        self.set_emergency_contacts(names.get_first_name() + ' ' + self.lastname)

    def _set_random_family_doctor(self):
        self.set_family_doctor(names.get_full_name())

    def _set_random_phone_number(self):
        phone_number = ''
        for i in range(0, 10):
            phone_number += str(random.randint(0, 9))

        self.set_phone_number(phone_number)

    def _set_random_ssn(self):
        ssn = ''
        for i in range(0, 11):
            if i == 3 or i == 6:
                ssn += '-'
            else:
                ssn += str(random.randint(0, 9))

        self.set_ssn(ssn)

    def _set_random_address(self):
        # random 5 numbers + random last name + 'st' or 'dr'
        # huntsville, al + 35###
        address = ''

        # generate 5 random numbers
        for i in range(0, 5):
            address += str(random.randint(0, 9))

        # some random last name (hopefully street name sounding)
        address += ' ' + names.get_last_name()

        # choose 'st' or 'dr'
        address += random.choice([' St ', ' Dr '])

        # huntsville al
        address += 'Huntsville, AL '

        # zipcode
        address += random.choice(HUNTSVILLE_ZIP_CODES)

        self.set_address(address)

    def _set_random_building(self):
        building = random.randint(1, 10)
        self.building = building

    def _set_random_marital_status(self):
        # we'll assume minors are not married
        if int(self.age) < 18:
            marital_status = 'Unmarried'
        else:
            marital_status = random.choice(MARITAL_STATUSES)
        self.set_marital_status(marital_status)

    def _set_random_employment_status(self):
        if int(self.age) < 16:
            employment_status = 'Unemployed'
        else:
            employment_status = random.choice(EMPLOYMENT_STATUSES)
        self.set_employment_status(employment_status)

    def _set_random_employer(self):
        if self.employment_status == 'Employed':
            # we're going to set a random name here because I cannot find
            # a company names dataset
            employer = names.get_full_name()
        else:
            employer = 'N/A'
        self.set_employer(employer)

    def _set_random_insurance_provider(self):
        insurance_provider = random.choice(INSURANCE_PROVIDERS)
        self.set_insurance_provider(insurance_provider)

    def _set_random_insurance_contact(self):
        insurance_contact = names.get_full_name()
        self.set_insurance_contact(insurance_contact)

    def _set_random_invoice(self):
        invoice = random.randint(1500, 7000)
        self.set_invoice(invoice)

    def _set_random_patient_amount_paid(self):
        patient_amount_paid = random.randint(0, self.invoice // 3)
        self.set_patient_amount_paid(patient_amount_paid)

    def _set_random_insurance_amount_paid(self):
        insurance_amount_paid = random.randint(0, (self.invoice - self.patient_amount_paid))
        self.set_insurance_amount_paid(insurance_amount_paid)

    def _set_random_pay_plan(self):
        pay_plan = random.choice(['Annual', 'Monthly', 'N/A'])
        self.set_pay_plan(pay_plan)

    def _set_random_insurance_account_num(self):
        # typically between 9 and 13 digits
        insurance_account_num = ''
        digits = random.randint(9, 13)
        for i in range(0, digits):
            insurance_account_num += str(random.randint(0, 9))
        self.set_insurance_account_num(insurance_account_num)

    def _set_random_insurance_num(self):
        # sample: 2424-78787-WXZ
        insurance_num = ''

        # four random digits
        for i in range(0, 4):
            insurance_num += str(random.randint(0, 9))

        insurance_num += '-'

        # 5 random digits
        for i in range(0, 5):
            insurance_num += str(random.randint(0, 9))

        insurance_num += '-'

        # three random letters
        for i in range(0, 3):
            insurance_num += chr(random.randint(65, 90))

        self.set_insurance_num(insurance_num)

    def _refresh_dict(self):
        # dictionary implementation is used here for ease of parsing
        # since naming conventions will be consistent regardless
        self.data = {'patientID': self.patientID,
                     'firstname': self.firstname,
                     'lastname': self.lastname,
                     'room_number': self.room_number,
                     'bed_number': self.bed_number,
                     'sex': self.sex,
                     'age': self.age,
                     'height': self.height,
                     'weight': self.weight,
                     'race': self.race,
                     'dob': self.dob,
                     'care_provider': self.care_provider,
                     'current_status': self.current_status,
                     'medical_risks': self.medical_risks,
                     'allowed_visitors': self.allowed_visitors,
                     'restricted_visitors': self.restricted_visitors,
                     'admission_date': self.admission_date,
                     'admission_reason': self.admission_reason,
                     'discharge_date': self.discharge_date,
                     'emergency_contacts': self.emergency_contacts,
                     'family_doctor': self.family_doctor,
                     'medical_history': self.medical_history,
                     'photo': self.photo,
                     'phone_number': self.phone_number,
                     'ssn': self.ssn,
                     'doctor_notes': self.doctor_notes,
                     'nurse_notes': self.nurse_notes,
                     'address': self.address,
                     'prescriptions': self.prescriptions,
                     'procedures': self.procedures,
                     'building': self.building,
                     'marital_status': self.marital_status,
                     'employment_status': self.employment_status,
                     'employer': self.employer,
                     'insurance_provider': self.insurance_provider,
                     'insurance_contact': self.insurance_contact,
                     'invoice': self.invoice,
                     'patient_amount_paid': self.patient_amount_paid,
                     'insurance_amount_paid': self.insurance_amount_paid,
                     'pay_plan': self.pay_plan,
                     'pay_history': self.pay_history,
                     'insurance_account_num': self.insurance_account_num,
                     'charge_history': self.charge_history,
                     'insurance_num': self.insurance_num
                     }

    # print() overloading
    def __str__(self):
        output = ''
        for key in self.data.keys():
            output += key + ': ' + str(self.data[key]) + '\n'
        return output
