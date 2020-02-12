# You have to be MIN_DRIVE or more to drive. Let's print with f-strings
# to test it.

MIN_DRIVE = 18


def can_you_drive(name, age):
    string = ""
    if age >= MIN_DRIVE:
        string = f"{name} is old enough to drive"
    else:
        string = f"{name} is not old enough to drive"
    return string


print(can_you_drive("Quique", 20))
