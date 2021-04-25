import os
import re

def reduce_dev():
    target_id = input("Print province id to reduce dev:\n")
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

def find_provinces():
    target= input("\nPrint regexp to find:\n")
    files = os.listdir(".")

    for f in files:
        fh = open(f, "r")
        ft = fh.read()

        provid = re.search("[0-9]+", f)

        if re.search(target, ft):
            print(provid.group(), end = " ")

        fh = None

def remove_from_string():
    replace_from = input("Replace from:\n")
    replace_what = input("Replace what:\n").split(" ")

    for f in replace_what:
        replace_from = replace_from.replace(f, "")

    replace_from = replace_from.replace("  ", " ")
    print()
    print()
    print(replace_from)

def append_to_provinces():
    target= input("\nPrint regexp to find:\n")
    files = os.listdir(".")

    i = 0
    for f in files:
        fh = open(f, "r")
        ft = fh.read()

        # provid = re.search("[0-9]+", f)

        if re.search(target, ft) or re.search(target, f):
            fh = open(f, "w")

            ft += """\n# Syndicate append
595.1.1 = {
owner = SYD
controller = SYD
add_core = SYD
}"""
            fh.write(ft)
            i += 1
        fh = None
    print("Wrote " + str(i) + " files")

while True:
    mode = input("Select desired mode:\n")
    if mode == "1":
        reduce_dev()
    elif mode == "2":
        find_provinces()
    elif mode == "3":
        remove_from_string()
    elif mode == "4":
        append_to_provinces()