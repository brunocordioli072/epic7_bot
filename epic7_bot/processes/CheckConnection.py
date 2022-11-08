import logging
import multiprocessing
import sys
import time
from epic7_bot.core.Logger import get_log_level
from epic7_bot.core.ScreenManager import ScreenManager
from epic7_bot.templates.CommonTemplates import CommonTemplates
import psutil


class CheckConnection(multiprocessing.Process):
    def __init__(self, main_process_pid):
        multiprocessing.Process.__init__(self, daemon=True)
        self.CommonTemplates = CommonTemplates()
        self.ScreenManager = ScreenManager()
        self.main_process_pid = main_process_pid

    def match_there_was_a_connection_error_template(self):
        return self.ScreenManager.match_template_on_screen_area(
            x1=475, y1=372, x2=1122, y2=406, template=self.CommonTemplates.there_was_a_connection_error, percentage=0.7)

    def match_connecting_problem_template(self):
        return self.ScreenManager.match_template_on_screen_area(
            x1=694, x2=908, y1=421, y2=451, template=self.CommonTemplates.connecting_problem, percentage=0.7)

    def run(self):
        try:
            main_process = psutil.Process(self.main_process_pid)
            seconds = 21600  # 6 hours

            # problems with - RecursionError: maximum recursion depth exceeded in comparison
            while seconds != 0:
                seconds -= 1
                time.sleep(1)
                there_was_a_connection_error = self.match_there_was_a_connection_error_template()
                connecting_problem = self.match_connecting_problem_template()
                if connecting_problem is not None or there_was_a_connection_error is not None:
                    logging.error(f"Found Connection Problem")
                    main_process.suspend()
                    while True:
                        time.sleep(1)
                        if there_was_a_connection_error is not None:
                            there_was_a_connection_error = self.match_there_was_a_connection_error_template()
                            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                                x1=475, y1=372, x2=1122, y2=406, action="Click on there_was_a_connection_error")
                            if there_was_a_connection_error is None:
                                main_process.resume()
                                break
                        if connecting_problem is not None:
                            connecting_problem = self.match_connecting_problem_template()
                            if connecting_problem is None:
                                main_process.resume()
                                break
        except BaseException as e:
            if get_log_level() == "DEBUG":
                raise e
            else:
                pass
