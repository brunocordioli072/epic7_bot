import logging
import os
import io
import logging
import sys
import threading
import datetime

from epic7_bot.utils.Spinner import Spinner


def get_log_level():
    LOG_LEVEL = os.getenv("LOG_LEVEL") if os.getenv(
        "LOG_LEVEL") is not None else "INFO"
    return LOG_LEVEL


def init_logger():
    level = logging.getLevelName(get_log_level())
    logging.basicConfig(level=level, handlers=[LoggerHandler(level=level)])


class LoggerHandler(logging.Handler):

    def __init__(self,
                 stream=None,
                 spin_interval=0.1,
                 format=u'{message} {spinner}',
                 level=logging.NOTSET):
        super(LoggerHandler, self).__init__(level)
        self._stream = stream
        self._message_format = format
        self._spinner = Spinner()
        self._spin_interval = spin_interval
        self._current_record_changed = threading.Condition()
        self._thread = threading.Thread(target=self._display, daemon=True)
        self._current_record = None
        sys.stdout.write('\n')
        sys.stdout.flush()

    def get_stream(self):
        stream = sys.stdout if self._stream is None else self._stream
        if callable(getattr(stream, 'isatty')):
            atty = stream.isatty()
        else:
            atty = False
        try:
            stream.write('')
        except TypeError:
            stream = io.TextIOWrapper(stream)
        return stream, atty

    def emit(self, record):
        if not self.filter(record):
            return
        stream, atty = self.get_stream()
        if not atty:
            stream.write(record.getMessage())
            return
        with self._current_record_changed:
            self._current_record = record
            self._current_record_changed.notify()
        if not self._thread.is_alive():
            self._thread.start()

    def _display(self):
        stream, _ = self.get_stream()
        format_message = self._message_format.format
        if self.level == 10:  # debug level
            stream.write(
                f"{datetime.datetime.now()} :: {self._current_record.getMessage()} \n")
            stream.flush()
        else:
            format_line = u'\r\033[F{0:{1}}\n\x1B[3mUse Ctrol-C to stop program.\x1B[0m'.format
            previous_line_length = 0
            while True:
                record = self._current_record

                if record is None:
                    break
                s = format_message(spinner=self._spinner.next(),
                                   record=record,
                                   message=record.getMessage())
                stream.write(format_line(s, previous_line_length or 1))
                previous_line_length = len(s)
                stream.flush()
                with self._current_record_changed:
                    self._current_record_changed.wait(self._spin_interval)
            s = self._current_record.getMessage()
            stream.write(u'\r{0:{1}}\n'.format(s, previous_line_length or 1))
            stream.flush()
        self._thread = threading.Thread(target=self._display, daemon=True)
