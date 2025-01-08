import game_mail.config.applying as cfg

from ..import_api import *
from . import info_logger, debug_logger


class psiLogger:

    def info(self, *args):
        psi.logger.info(args[0])

    def warning(self, *args):
        psi.logger.warning(args[0])
    
    def error(self, *args):
        psi.logger.error(args[0])

    def debug(self, *args):
        psi.logger.debug(args[0])

def get_logger():
    if cfg.logger_config["mcdr"]:
        logger = psiLogger()
        return logger
    else:
        if cfg.logger_config["debug"]:
            logger = debug_logger
        else:
            logger = info_logger
        return logger


__all__ = ["get_logger"]
import sys
sys.modules[__name__] = get_logger