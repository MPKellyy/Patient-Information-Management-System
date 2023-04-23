import datetime


# utilities


# create patient ids from integer
def create_patient_id(i):
    i = str(i)
    return '0' * (8 - len(i)) + i


def literal(s):
    if s:
        s = s.replace('\'', '\'\'').replace('\n', ' ')
        return "\'" + str(s) + "\'"
    else:
        return "\'\'"


def automate_class_input(l):
    s = ''
    for item in l:
        s += item + '=None, '
    return s


def automate_attribute_list(s):
    """ input a string containing the input arguments and output the attribute definitions.
    example: for a function defined as: def __init__(foo, bar=0): pass
             input: "foo, bar=0"
             output: self.foo = foo
                     self.bar = bar

    """
    s = s.replace(' ', '')
    att = s.split(',')

    for a in att:
        att_name = a.split('=')[0]
        print('self.' + att_name + ' = ' + att_name)


def automate_setters(s):
    """ input a string containing the input arguments and output the setter code
    """
    s = s.replace(' ', '')
    att = s.split(',')

    for a in att:
        att_name = a.split('=')[0]
        print("def set_" + att_name + "(self, new): \n\t"
                                      "if self." + att_name + " is not new:\n\t\t"
                                                              "self." + att_name + " = new \n\t\tself.data[\'" +
              att_name + "\'] = new \n\t\tself.changes.append(" +
              literal(att_name) + ") \n\n")


def automate_list(s):
    s = s.replace(' ', '')
    att = s.split(',')

    output = ''
    for a in att:
        att_name = a.split('=')[0]
        output += att_name + ', '
    print(output)


def automate_dict(s):
    s = s.replace(' ', '')
    att = s.split(',')

    output = ''
    for a in att:
        att_name = a.split('=')[0]
        output += '\'' + att_name + '\'' + ': ' + 'self.' + att_name + ',\n'
    print(output)


def calculate_current_age(dob):
    # return current age given Datetime date of birth
    today = datetime.date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def get_list_from_sql_output(s1, s2):
    s = s1.replace('(', '').replace(')', '').replace('\'', '').replace(',,', ',').replace(' ', '') + s2.replace('(',
                                                                                                                '').replace(
        ')', '').replace('\'', '').replace(',,', ',').replace(' ', '')
    return s.split(',')[:-1]


# s = "firstname=None, lastname=None, room_number=None, bed_number=None,\
#                  sex=None, age=None, height=None, weight=None, race=None, dob=None, care_provider=None,\
#                  current_status=None, medical_risks=None, allowed_visitors=None, restricted_visitors=None,\
#                  admission_date=None, admission_reason=None, discharge_date=None, emergency_contacts=None,\
#                  family_doctor=None, medical_history=None, photo=None, phone_number=None, ssn=None,\
#                  doctor_notes=None, nurse_notes=None, address=None, prescriptions=None, procedures=None,\
#                  building=None, marital_status=None, employment_status=None, employer=None,\
#                  insurance_provider=None, insurance_contact=None, invoice=None, patient_amount_paid=None,\
#                  insurance_amount_paid=None, pay_plan=None, pay_history=None, insurance_account_num=None,\
#                  charge_history=None, insurance_num=None"
#
# automate_setters(s)
