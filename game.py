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
    ans = input(" >>>> ").lower()
    return ans


def sleep():
    clear()
    print("\n\n\tJourney's End\n")


def status():
    return


def inventory():
    return


def market():
    return


def travel():
    return


def main():
    while True:
        ans = mainmenu()
        if ans in ["x", "sleep"]:
            return sleep()
        elif ans in ["s", "status"]:
            status()
        elif ans in ["i", "inventory"]:
            inventory()
        elif ans in ["m", "market"]:
            market()
        else:
            travel()


# https://github.com/kyaruwo
if __name__ == "__main__":
    main()
