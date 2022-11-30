import os


def clear():
    os.system("cls")


def reset():
    from dbuild.mage import mage
    from dbuild.item import item
    from dbuild.enemy import enemy

    try:
        os.remove("db.sqlite")
    except:
        pass

    os.chdir("dbuild")

    mage()
    item()
    enemy()

    os.chdir("..")

    os.rename("dbuild/db.sqlite", "db.sqlite")


def resetgame():
    clear()
    op = input("Enter \"resetgame\" : ")
    clear()

    if op == "resetgame":
        reset()
        print("\nGame Reset\n")

    else:
        print("\nInvalid Input\n")

    os.system("pause")
    os.system("python main.py")

# https://github.com/kyaruwo
