"""Test file that contains test functions for all of my functions in ratebot_functions
"""


from my_module.ratebot_functions import *

test_string1 = "Hello WORLD!"
test_string2 = "shoes"
test_list1 = ["a", "b", "c", "d"]
test_list2 = ["i", "am", "hungry"]
test_list3 = ["yes", "no"]


def test_prepare_text():
    assert isinstance(prepare_text(test_string1), list)
    assert prepare_text(test_string1) == ["hello", "world!"]
    assert callable(prepare_text)
    
def test_end_chat():
    assert isinstance(end_chat(test_string1), bool)
    assert end_chat(test_string1) == False
    assert callable(end_chat)
    
def test_list_to_string():
    assert isinstance(list_to_string(test_list1), str)
    assert list_to_string(test_list1) == "a b c d"
    assert callable(list_to_string)
    
def test_list_concatenator():
    assert isinstance(list_concatenator(test_list1, test_list2, test_list3), str)
    assert list_concatenator(test_list1, test_list2, test_list3) == "a b c d i am hungry yes no"
    assert callable(list_concatenator)
    
def test_error_message():
    assert isinstance(error_message(), str)
    assert error_message() == "This movie does not exists in my database. Please try the another one."
    assert callable(error_message)