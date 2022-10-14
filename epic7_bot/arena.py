import time

from epic7_bot import templates
from epic7_bot.utils.devices import get_device
import epic7_bot.utils.helper as helper


def battle_rotation():
    # click on start battle
    helper.click_middle_and_check_change_retry(
        x1=1065, x2=1216, y1=799, y2=852)

    time.sleep(4)

    # click on skip
    helper.click_middle_and_check_change_retry(x1=1476, x2=1574, y1=23, y2=76)

    # click on auto battle
    helper.click_middle_and_check_change_retry(x1=1379, x2=1439, y1=14, y2=68)

    while helper.check_change_on_area(x1=1471, x2=1581, y1=19, y2=76, template=templates.skip_button, percentage=0.55) is None:
        time.sleep(1)

    # click on skip
    helper.click_middle_and_check_change_retry(x1=1476, x2=1574, y1=23, y2=76)

    time.sleep(2)

    # click on confirm
    helper.click_middle_and_check_change_retry(
        x1=1378, x2=1546, y1=802, y2=853)


def do_battle_rotation(x1, y1, x2, y2):
    clicked = helper.click_middle_and_check_change_retry(
        x1, y1, x2, y2)
    if clicked:
        battle_rotation()


def scroll():
    device = get_device()
    device.shell(
        "input touchscreen swipe 1200 700 1200 400 200")


def scroll_and_do_battle_rotation(x1, y1, x2, y2):
    scroll()
    do_battle_rotation(x1, y1, x2, y2)


def start_arena_npc_auto_battle():
    # helper.click_position(position_x=871, position_y=814, waitTime=0)
    # # click on arena icon on lobby
    # click_middle_and_check_change_retry(x1=1022, x2=1129, y1=749, y2=882)

    # # click on arena ranked
    # click_middle_and_check_change_retry(x1=246, x2=438, y1=218, y2=283)

    # # click on NPC opponents
    # click_middle_and_check_change_retry(x1=1334, x2=1551, y1=236, y2=298)

    # click on first opponent
    do_battle_rotation(x1=1109, x2=1212, y1=218, y2=294)

    # click on second opponent
    do_battle_rotation(x1=1115, x2=1208, y1=354, y2=418)

    # click on third opponent
    do_battle_rotation(x1=1117, x2=1203, y1=480, y2=544)

    # click on fouth opponent
    do_battle_rotation(x1=1117, x2=1207, y1=615, y2=681)

    # click on fifth opponent
    do_battle_rotation(x1=1114, x2=1212, y1=740, y2=815)

    # click on sixty opponent
    scroll_and_do_battle_rotation(x1=1121, x2=1209, y1=274, y2=339)

    # click on seventy opponent
    scroll_and_do_battle_rotation(x1=1117, x2=1208, y1=408, y2=479)

    # click on eighth opponent
    scroll_and_do_battle_rotation(x1=1117, x2=1203, y1=546, y2=594)

    # click on nineth opponent
    scroll_and_do_battle_rotation(x1=1117, x2=1207, y1=676, y2=735)

    # click on tenth opponent
    scroll_and_do_battle_rotation(x1=1114, x2=1212, y1=804, y2=865)
