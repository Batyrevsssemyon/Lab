from Jojo import *

stand_masters = []

stand_masters.append(Jojo("Jotaro", "190", "110", date(1970, 3, 5), "Star Platinum", "OraOra"))

while True:
    command = input("Write command \r\n")

    if command == "add":
        new_stand_master = Jojo()
        new_stand_master.add()
        stand_masters.append(new_stand_master)

    if command == "show":
        for stand_master in stand_masters:
            print(stand_master.show())

    if command == "show_stand":
        for stand in stand_masters:
            print(stand.show_stand())
