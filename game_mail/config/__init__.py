import game_mail.config.applying as cfg

from ..import_api import *
from .defaults import *

def config_loader(server: PluginServerInterface):
    cfg.config = server.load_config_simple('config.json', default_config)