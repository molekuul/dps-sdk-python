import logging
import io
import os
import sys
from logging import handlers

class DvlsLogger(object):

    def __init__(self, options):
        logging.Logger.findCaller = self.findCaller
        logging._frame_delta = 1
        self.version = options.get('version')
        self.verbose=True
        self.console_logger = logging.getLogger('dvlssdk.console')
        self.file_logger = logging.getLogger('dvlssdk.fulllog')
        self._set_logger(options.get('errorLevelLog'))

    def set_verbose(self, verbose):
        self.verbose = verbose

    def _should_log(self, verbose_override):
        if verbose_override is not None:
            return verbose_override
        return self.verbose

    def debug(self, msg, verbose_override=None, function_depth=1):
        logging._frame_delta = function_depth
        if self._should_log(verbose_override):
            self.file_logger.debug(msg)
            return self.console_logger.debug(msg)


    def info(self, msg, verbose_override=None, function_depth=1):
        logging._frame_delta = function_depth
        if self._should_log(verbose_override):
            self.file_logger.info(msg)
            return self.console_logger.info(msg)

    def warning(self, msg, verbose_override=None, function_depth=1):
        logging._frame_delta = function_depth
        self.file_logger.warning(msg)
        if self._should_log(verbose_override):
            return self.console_logger.warning(msg)

    def error(self, msg, verbose_override=None, function_depth=1):
        logging._frame_delta = function_depth
        self.file_logger.error(msg)
        if self._should_log(verbose_override):
            return self.console_logger.error(msg)

    def critical(self, msg, verbose_override=None, function_depth=1):
        logging._frame_delta = function_depth
        self.file_logger.critical(msg)
        if self._should_log(verbose_override):
            return self.console_logger.critical(msg)

    def _set_logger(self, log_level):
        try:
            log_level = getattr(logging, log_level.upper())
        except AttributeError:
            log_level = getattr(logging, 'INFO')
        self.console_logger.setLevel(log_level)
        self.file_logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(log_level)
        console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
        ch.setFormatter(console_formatter)

        file_handler = logging.handlers.RotatingFileHandler('dvls_sdk.log', mode='a', maxBytes=2000024, backupCount=5)
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter("%(asctime)s [version: " + self.version + "] [%(filename)-20s:%(lineno)-4s] [%(levelname)8s] --- %(message)s")
        file_handler.setFormatter(file_formatter)

        self.console_logger.addHandler(ch)
        self.file_logger.addHandler(file_handler)

    def findCaller(self, stack_info=False):
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """
        f = logging.currentframe()
        # On some versions of IronPython, currentframe() returns None if
        # IronPython isn't run with -X:Frames.
        for _ in range(1 + logging._frame_delta):
            if f is not None:
                f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)", None
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == logging._srcfile:
                f = f.f_back
                continue
            sinfo = None
            if stack_info:
                sio = io.StringIO()
                sio.write('Stack (most recent call last):\n')
                logging.traceback.print_stack(f, file=sio)
                sinfo = sio.getvalue()
                if sinfo[-1] == '\n':
                    sinfo = sinfo[:-1]
                sio.close()
            rv = (co.co_filename, f.f_lineno, co.co_name, sinfo)
            break
        return rv
