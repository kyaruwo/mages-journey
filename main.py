from lib.clear import clear


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


def main():
    from init import init
    from game.sleep import sleep
    from game.status import status
    from game.inventory import inventory
    from game.market import market
    from game.travel import travel

    init.initialize()
    while True:
        ans = mainmenu()
        clear()
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
