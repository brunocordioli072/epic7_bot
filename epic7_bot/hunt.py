import multiprocessing
import epic7_bot.common.screen as screen
import epic7_bot.templates as templates
import time
import logging


def do_rotation():
    try_again_button, confirm_button = None, None

    def check_buttons():
        try_again_button = screen.check_change_on_area(
            x1=1416, x2=1533, y1=810, y2=841, template=templates.hunt_try_again, percentage=0.6)
        confirm_button = screen.check_change_on_area(
            x1=1395, y1=808, x2=1492, y2=839, template=templates.hunt_confirm, percentage=0.6)
        return try_again_button, confirm_button

    while try_again_button is None and confirm_button is None:
        try_again_button, confirm_button = check_buttons()
        logging.debug(f"Wait for try again button or confirm button to appear")
        time.sleep(1)

    if confirm_button is not None:
        screen.click_middle_and_check_change_retry(
            x1=1395, y1=808, x2=1492, y2=839, action="Click on confirm button")

    screen.click_middle_and_check_change_retry(
        x1=1416, x2=1533, y1=810, y2=841, action="Click on try again button")

    screen.click_middle_and_check_change_retry(
        x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

    if screen.check_change_on_area(
            x1=629, y1=175, x2=960, y2=224, template=templates.hunt_insufficient_energy, percentage=0.6) is not None:
        logging.debug(f"Insufficient Energy, finishing hunting")
        return

    do_rotation()


def start_hunt():
    screen.click_middle_and_check_change_retry(
        x1=1404, y1=811, x2=1469, y2=842, action="Click on start button")

    do_rotation()
