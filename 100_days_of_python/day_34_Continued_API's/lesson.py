#declaring variable type

age: int

age = "twelve"

def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

police_check()