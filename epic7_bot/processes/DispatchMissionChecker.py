import logging
import multiprocessing
import sys
import time
from epic7_bot.core.Logger import get_log_level
from epic7_bot.core.ScreenManager import ScreenManager
from epic7_bot.templates.CommonTemplates import CommonTemplates
import psutil


class DispatchMissionChecker(multiprocessing.Process):
    def __init__(self, main_process_pid):
        multiprocessing.Process.__init__(self, daemon=True)
        self.CommonTemplates = CommonTemplates()
        self.ScreenManager = ScreenManager()
        self.main_process_pid = main_process_pid

    def match_dispatch_mission_completed_template(self):
        return self.ScreenManager.match_template_on_screen(template=self.CommonTemplates.dispatch_mission_completed, percentage=0.9)

    def match_dispatch_mission_template(self):
        return self.ScreenManager.match_template_on_screen(template=self.CommonTemplates.dispatch_mission, percentage=0.7)

    def run(self):
        try:
            main_process = psutil.Process(self.main_process_pid)
            seconds = 21600  # 6 hours

            # problems with - RecursionError: maximum recursion depth exceeded in comparison
            while seconds != 0:
                seconds -= 1
                time.sleep(1)
                dispatch_mission_completed = self.match_dispatch_mission_completed_template()
                dispatch_mission = self.match_dispatch_mission_template()

                if dispatch_mission is not None or dispatch_mission_completed is not None:
                    main_process.suspend()
                    logging.error(f"Dispatch Mission appeared")
                    time.sleep(5)
                    self.ScreenManager.click_middle_and_check_change_on_screen_retry(
                        x1=1099, y1=703, x2=1228, y2=745, action="Click on Try Again")
                    time.sleep(2)
                    main_process.resume()
                    break
        except BaseException as e:
            if get_log_level() == "DEBUG":
                raise e
            else:
                pass
