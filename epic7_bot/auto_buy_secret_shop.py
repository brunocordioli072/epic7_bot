import time
import epic7_bot.templates.shop as shop_templates
from sys import exit
import epic7_bot.common.screen as screen
import epic7_bot.common.config as config


def check_bookmarks():
    global bought
    global covenant
    global mystic

    mystic_pos = screen.check_image(shop_templates.mystic)
    coven_pos = screen.check_image(shop_templates.covenant)

    if mystic_pos is not None:
        x, y = screen.get_position_of_image(mystic_pos)

        screen.click_position(x + 650, y + 50, 1)

        screen.click_image(shop_templates.buy_button_mystic, 1)

        bought = True
        mystic += 1

    if coven_pos is not None:
        x, y = screen.get_position_of_image(coven_pos)

        screen.click_position(x + 650, y + 50, 1)

        screen.click_image(shop_templates.buy_button_covenant, 1)

        bought = True
        covenant += 1


def scroll():
    config.device.shell(
        "input touchscreen swipe 1200 700 1200 300 300")


def check_store():
    check_bookmarks()

    global bought
    if bought is False:
        scroll()
        check_bookmarks()
    bought = False


def refresh():
    screen.click_middle_check_change_on_screen_retry(
        x1=287, y1=808, x2=387, y2=838, action="Click on Refresh Button")
    screen.click_middle_check_change_on_screen_retry(
        x1=878, y1=537, x2=986, y2=568, action="Click on Confirm Button")

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
