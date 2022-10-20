import logging
import multiprocessing
import time
from epic7_bot.core.ScreenManager import ScreenManager
from epic7_bot.templates.CommonTemplates import CommonTemplates
import psutil


class CheckConnection(multiprocessing.Process):
    def __init__(self, main_process_pid):
        multiprocessing.Process.__init__(self, daemon=True)
        self.CommonTemplates = CommonTemplates()
        self.ScreenManager = ScreenManager()
        self.main_process_pid = main_process_pid

    def run(self):
        main_process = psutil.Process(self.main_process_pid)

        def check():
            time.sleep(1)
            there_was_a_connection_error = self.ScreenManager.match_template_on_screen_area(
                x1=475, y1=372, x2=1122, y2=406, template=self.CommonTemplates.there_was_a_connection_error, percentage=0.7)
            connecting_problem = self.ScreenManager.match_template_on_screen_area(
                x1=694, x2=908, y1=421, y2=451, template=self.CommonTemplates.connecting_problem, percentage=0.7)
            if connecting_problem is not None or there_was_a_connection_error is not None:
                logging.error(f"Found Connection Problem")
                main_process.suspend()
                while True:
                    time.sleep(1)
                    if there_was_a_connection_error is not None:
                        there_was_a_connection_error = self.ScreenManager.match_template_on_screen_area(
                            x1=475, y1=372, x2=1122, y2=406, template=self.CommonTemplates.there_was_a_connection_error, percentage=0.7)
                        self.ScreenManager.click_middle_and_check_change_on_area_retry(
                            x1=475, y1=372, x2=1122, y2=406, action="Click on there_was_a_connection_error")
                        if there_was_a_connection_error is None:
                            main_process.resume()
                            break
                    if connecting_problem is not None:
                        connecting_problem = self.ScreenManager.match_template_on_screen_area(
                            x1=694, x2=908, y1=421, y2=451, template=self.CommonTemplates.connecting_problem, percentage=0.7)
                        if connecting_problem is None:
                            main_process.resume()
                            break
            else:
                check()
        check()
