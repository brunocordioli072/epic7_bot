import logging
import epic7_bot.templates as templates
import epic7_bot.common.screen as screen
import epic7_bot.common.config as config


def start_checking_connection_problem():
    result = screen.check_change_on_area(
        x1=694, x2=908, y1=421, y2=451, template=templates.connecting_problem, percentage=0.7)
    if result is not None:
        logging.error(f"Found Connection Problem")
        config.is_checking_connection_problem = False

    if config.is_checking_connection_problem is False:
        return
    else:
        start_checking_connection_problem()
