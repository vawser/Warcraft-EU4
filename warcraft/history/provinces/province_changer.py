import os
import re

while True:
    target_id = input("Print province id to reduce dev")
    files = os.listdir(".")

    i = 0
    for f in files:
        if re.search(target_id, f):
            fh = open(f, "r")
            ft = fh.read()
            ft = ft.replace("base_tax = 2", "base_tax = 1")
            ft = ft.replace("base_tax = 3", "base_tax = 2")
            ft = ft.replace("base_tax = 4", "base_tax = 3")
            ft = ft.replace("base_tax = 5", "base_tax = 4")

            ft = ft.replace("base_production = 2", "base_production = 1")
            ft = ft.replace("base_production = 3", "base_production = 2")
            ft = ft.replace("base_production = 4", "base_production = 3")
            ft = ft.replace("base_production = 5", "base_production = 4")

            ft = ft.replace("base_manpower = 2", "base_manpower = 1")
            ft = ft.replace("base_manpower = 3", "base_manpower = 2")
            ft = ft.replace("base_manpower = 4", "base_manpower = 3")
            ft = ft.replace("base_manpower = 5", "base_manpower = 4")

            fh = open(f, "w")
            fh.write(ft)
            i += 1
            fh = None
    print("Wrote " + str(i) + " files")