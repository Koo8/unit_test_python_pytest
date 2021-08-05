from math_func import StudentDB
import pytest

# there are two methods to simplify the program, use setup and teardown methods from classic xunit
# db = None # create a global db variable
# def setup_module(module): # auto called by pytest
#     global db
#     db = StudentDB()
#     db.connect('data.json')
#     print("********** Set Up  ************")
#
# def teardown_module(module): #auto called by pytest
#     print("********** Tear Down  ************")

# 2nd method is to use pytest fixtures
@pytest.fixture(scope='module') # use scope module so that it is called only once throughout the module
def db():
    print("********SET UP******")
    db = StudentDB()
    db.connect('data.json')
    yield db
    db.close()
    print('*********** TEAR DOWN **********')


def test_scott_data(db):
    scott_data = db.get_student_data_from_name('Scott')
    assert scott_data['id'] ==1
    assert scott_data['name'] == "Scott"
    assert scott_data['result'] == "pass"

def test_mark_data(db):
    mark_data = db.get_student_data_from_name('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'