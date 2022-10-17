import time
import epic7_bot.templates as templates
from sys import exit
import epic7_bot.common.screen as screen
import epic7_bot.common.config as config


def check_bookmarks():
    global bought
    global covenant
    global mystic

    mystic_pos = screen.check_image(templates.mystic)
    coven_pos = screen.check_image(templates.covenant)

    if mystic_pos is not None:
        x, y = screen.get_position_of_image(mystic_pos)

        screen.click_position(x + 650, y + 50, 1)

        screen.click_image(templates.buy_button_mystic, 1)

        bought = True
        mystic += 1

    if coven_pos is not None:
        x, y = screen.get_position_of_image(coven_pos)

        screen.click_position(x + 650, y + 50, 1)

        screen.click_image(templates.buy_button_covenant, 1)

        bought = True
        covenant += 1


def scroll():
    config.device.shell(
        "input touchscreen swipe 1200 700 1200 300 200")


def check_store():
    check_bookmarks()

    global bought
    if bought is False:
        scroll()
        check_bookmarks()
    bought = False


def refresh(error_counter=0):
    screen.click_image(templates.refresh_button)
    screen.click_image(templates.confirm_button, 1)
    time.sleep(0.5)
    confirm_button = screen.check_image(templates.confirm_button)
    if confirm_button is not None:
        if error_counter < 5:
            refresh(error_counter + 1)
        else:
            print("Error: Could not refresh")
            exit(1)
    else:
        global refreshes
        refreshes += 1


mystic = 0
refreshes = 0
covenant = 0
bought = False


def show_stats():
    print("="*20)
    print("Total Covenant: " + str(covenant))
    print("Total Mystic: " + str(mystic))
    print("Total Refreshes: " + str(refreshes))
    print("="*20)


def start_auto_buy_secret_shop():
    try:
        while True:
            check_store()
            refresh()
            show_stats()
    except KeyboardInterrupt:
        print("ctrol-c pressed")
        exit(1)
