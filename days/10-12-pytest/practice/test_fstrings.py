from practice_fstrings import can_you_drive


def test_driving():
    name = "_"
    age = 18
    age2 = 13
    assert can_you_drive(name, age) == "_ is old enough to drive"
    assert can_you_drive(name, age2) == "_ is not old enough to drive"
