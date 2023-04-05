import datetime

# utilities


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
        print("def set_" + att_name + "(self, new): \n\tself." + att_name +
              " = new \n\tself.data[\'" + att_name + "\'] = new \n\n")


def automate_list(s):
    s = s.replace(' ', '')
    att = s.split(',')

    output = ''
    for a in att:
        att_name = a.split('=')[0]
        output += att_name + ', '
    print(output)


def calculate_current_age(dob):
    # return current age given Datetime date of birth
    today = datetime.date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))



s = "patientID, firstname=None, lastname=None, room_number=None, sex=None, age=None,\
             height=None, weight=None, race=None, dob=None, care_provider=None, current_status=None,\
             medical_risks=None, allowed_visitors=None, restricted_visitors=None, admission_date=None,\
             admission_reason=None, discharge_date=None, emergency_contacts=None, family_doctor=None,\
             medical_history=None, photo=None, phone_number=None, ssn=None"

# automate_attribute_list(s)
# automate_setters(s)
