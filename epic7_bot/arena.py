import time
from epic7_bot import templates
import epic7_bot.common.config as config
import epic7_bot.common.screen as screen
import logging


def battle_rotation():
    logging.debug(f"Started battle rotation")

    screen.click_middle_and_check_change_retry(
        x1=1065, x2=1216, y1=799, y2=852, action="Click on start battle")

    time.sleep(4)

    screen.click_middle_and_check_change_retry(
        x1=1476, x2=1574, y1=23, y2=76, action="Click on skip")

    screen.click_middle_and_check_change_retry(
        x1=1379, x2=1439, y1=14, y2=68, action="Click on auto battle")

    while screen.check_change_on_area(x1=1471, x2=1581, y1=19, y2=76, template=templates.skip_button, percentage=0.55) is None:
        logging.debug(f"Wait for skip button to appear")
        time.sleep(1)

    screen.click_middle_and_check_change_retry(
        x1=1476, x2=1574, y1=23, y2=76, action="Click on skip button")

    time.sleep(2)

    screen.click_middle_and_check_change_retry(
        x1=1378, x2=1546, y1=802, y2=853, action="Click on confirm")


def do_battle_rotation(x1, y1, x2, y2, action):
    clicked = screen.click_middle_and_check_change_retry(
        x1, y1, x2, y2, action)
    if clicked:
        battle_rotation()


def scroll():
    config.device.shell(
        "input touchscreen swipe 1200 700 1200 400 200")


def scroll_and_do_battle_rotation(x1, y1, x2, y2, action):
    scroll()
    do_battle_rotation(x1, y1, x2, y2, action)


def start_arena_npc_auto_battle():
    # helper.click_position(position_x=871, position_y=814, waitTime=0)
    # # click on arena icon on lobby
    # click_middle_and_check_change_retry(x1=1022, x2=1129, y1=749, y2=882)

    # # click on arena ranked
    # click_middle_and_check_change_retry(x1=246, x2=438, y1=218, y2=283)

    # # click on NPC opponents
    # click_middle_and_check_change_retry(x1=1334, x2=1551, y1=236, y2=298)

    do_battle_rotation(x1=1109, x2=1212, y1=218, y2=294,
                       action="Click on first opponent")

    do_battle_rotation(x1=1115, x2=1208, y1=354, y2=418,
                       action="Click on second opponent")

    do_battle_rotation(x1=1117, x2=1203, y1=480, y2=544,
                       action="Click on third opponent")

    do_battle_rotation(x1=1117, x2=1207, y1=615, y2=681,
                       action="Click on fouth opponent")

    do_battle_rotation(x1=1114, x2=1212, y1=740, y2=815,
                       action="Click on fifth opponent")

    scroll_and_do_battle_rotation(x1=1121, x2=1209, y1=274, y2=339,
                                  action="Click on sixty opponent")

    scroll_and_do_battle_rotation(x1=1117, x2=1208, y1=408, y2=479,
                                  action="Click on seventy opponent")

    scroll_and_do_battle_rotation(x1=1117, x2=1203, y1=546, y2=594,
                                  action="Click on eighth opponent")

    scroll_and_do_battle_rotation(x1=1117, x2=1207, y1=676, y2=735,
                                  action="Click on nineth opponent")

    scroll_and_do_battle_rotation(x1=1114, x2=1212, y1=804, y2=865,
                                  action="Click on tenth opponent")
