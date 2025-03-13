from .import_api import *
from .utils import tr
from .config import config_loader

# This plugin's life cycle.
def on_load(server: PluginServerInterface, prev_module):
    config_loader(server)

def on_unload(server: PluginServerInterface):
    server.logger.info(tr("on_unload"))

# Server's life cycle.
def on_server_start_pre(server: PluginServerInterface):
    pass

def on_server_start(server: PluginServerInterface):
    pass

def on_server_startup(server: PluginServerInterface):
    pass

def on_server_stop(server: PluginServerInterface, server_return_code: int):
    if server_return_code == 0:
        pass
    else:
        pass

# MCDR's Info event.
def on_user_info(server: PluginServerInterface, info: Info):
    pass

def on_info(server: PluginServerInterface, info: Info):
    pass

# Player's gaming life cycle.
def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    pass

def on_player_left(server: PluginServerInterface, player: str):
    pass