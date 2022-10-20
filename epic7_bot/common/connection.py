import logging
import multiprocessing
import time
from epic7_bot.common.devices import setup_device
import epic7_bot.templates.common as common_templates
import epic7_bot.common.screen as screen
import epic7_bot.common.config as config
import psutil


def start_checking_connection_problem(main_process_pid):
    # problem with multiprocess
    setup_device()
    main_process = psutil.Process(main_process_pid)

    def check():
        time.sleep(1)
        there_was_a_connection_error = screen.check_change_on_area(
            x1=475, y1=372, x2=1122, y2=406, template=common_templates.there_was_a_connection_error, percentage=0.7)
        connecting_problem = screen.check_change_on_area(
            x1=694, x2=908, y1=421, y2=451, template=common_templates.connecting_problem, percentage=0.7)
        if connecting_problem is not None or there_was_a_connection_error is not None:
            logging.error(f"Found Connection Problem")
            main_process.suspend()
            while True:
                time.sleep(1)
                if there_was_a_connection_error is not None:
                    there_was_a_connection_error = screen.check_change_on_area(
                        x1=475, y1=372, x2=1122, y2=406, template=common_templates.there_was_a_connection_error, percentage=0.7)
                    screen.click_middle_and_check_change_retry(
                        x1=475, y1=372, x2=1122, y2=406, action="Click on there_was_a_connection_error")
                    if there_was_a_connection_error is None:
                        main_process.resume()
                        break
                if connecting_problem is not None:
                    connecting_problem = screen.check_change_on_area(
                        x1=694, x2=908, y1=421, y2=451, template=common_templates.connecting_problem, percentage=0.7)
                    if connecting_problem is None:
                        main_process.resume()
                        break
            # config.is_checking_connection_problem = False

        if config.is_checking_connection_problem is False:
            return
        else:
            check()
    check()
