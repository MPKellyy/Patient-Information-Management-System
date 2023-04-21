from patient import Patient

'''
HEADER:
This file is a test case document for patient. Whenever a test case is added to this document, you MUST provide
 a sufficient description of the case you are trying to assess.

USEFUL INFO:
For Pycharm to recognize your function as a test case, it MUST start with the prefix "test_", as shown below.
Simply run the file and let Pycharm handle the rest! Make sure to check the console once testing is complete!

PROPER TESTING FORMAT:

    def function():
        preamble:
        here you will define what the test function is supposed to be testing, and what it's expected output is, as well
        as any other useful information regarding the function

        post:
        here you will define a list of testing history and results. nothing super detailed needs to be here, if output is
        wrong or an error, describe the issue briefly. if the expected output is achieved, note it.
        do not include unexpected output or errors not directly tied to the tested functions.
'''


def test_create_random_patient_data():
    """
    Autofills patient data to create test Patient objects.

    Inputs: none
    Output: Patient object where no fields are left blank.

    """
    # create random patient
    patient = Patient(0)

    # assert that there are 42 attributes total
    patient_attributes = patient.get_attributes()
    assert(len(patient_attributes) == 42)

    # assert that all fields have a value
    for a in patient_attributes:
        assert(patient.data[a] is not None)


def test_randomize_all_missing_data():
    """
    Autofills patient data to create test Patient objects within context
    of existing/filled data.

    Inputs: varied
    Output: Patient object where no fields are left blank.

    """
    patient = Patient(0, age=25)
    patient_attributes = patient.get_attributes()

    # randomize missing data
    patient.randomize_all_missing_data()

    # assert that all fields have a value
    for a in patient_attributes:
        assert (patient.data[a] is not None)

    # assert that age has not changed
    assert(patient.age == 25)


def test_all_patient_setters():
    """
    Various setters for patient attributes.

    Inputs: new value of attribute
    Output: None

    """

    # create random patient
    patient = Patient(0)
    patient_attributes = patient.get_attributes()

    # assert that each setter actually sets attribute and changelog records change
    for (a, i) in zip(patient_attributes, range(0, len(patient_attributes))):
        # set attribute to 'test' + str(i) ('test1', 'test2', etc.)
        test_val = 'test' + str(i)
        exec('patient.set_' + a + '(\'' + test_val + '\')')

        # check that the value is equal to  test_val
        assert(patient.data[a] == test_val)

        # check that patient.changes has recorded the patient edit
        assert(test_val in patient.changes)




test_randomize_all_missing_data()
