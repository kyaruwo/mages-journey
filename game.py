import os


def clear():
    os.system("cls")


def line():
    print(22 * "-")


def title():
    clear()
    line()
    print((4 * " ") + "Mage's Journey")
    line()


def mainmenu():
    title()
    print("     (?) travel")
    print("     (M) market")
    print("     (I) inventory")
    print("     (S) status")
    print("     (X) sleep")
    line()
    res = input(" >>>> ").lower()
    return res


def main():
    while True:
        res = mainmenu()
        if res in ["x", "sleep"]:
            return
        if res in ["s", "status"]:
            continue
        if res in ["i", "inventory"]:
            continue
        if res in ["m", "market"]:
            continue


# https://github.com/kyaruwo
if __name__ == "__main__":
    main()
