import game_mail.config.applying as cfg

from ..import_api import *
from .defaults import *
from ..lang.api import *
from ..utils import tr

def config_loader(server: PluginServerInterface):
    cfg.plugin_config = server.load_config_simple('config.json', default_config) # Load basic config of this plugin, default tip enabled.
    cfg.logger_config = server.load_config_simple(file_name='logger.json', default_config=default_log_style, echo_in_console=False)
    locales.locale_zh_cn = server.load_config_simple(file_name=f'{configDir}/lang/zh_cn.json', default_config=locale_zh_cn, in_data_folder=False, echo_in_console=False)
    locales.locale_en_us = server.load_config_simple(file_name=f'{configDir}/lang/en_us.json', default_config=locale_en_us, in_data_folder=False, echo_in_console=False)
    server.register_translation("zh_cn", locales.locale_zh_cn)
    server.register_translation("en_us", locales.locale_en_us)
    server.logger.info(tr("on_load"))
    server.logger.info("Finished GameMail config loading!")
    test_logger()

def check_config(server: PluginServerInterface):
    config_list = [cfg.plugin_config, cfg.logger_config, locales.locale_zh_cn, locales.locale_en_us]
    for i in config_list:
        if i is None:
            server.logger.critical("Load config error, plugin can't continue work!")
            server.unload_plugin(plugin_id)
            break

def test_logger():
    if not cfg.logger_config["mcdr"]:
        from ..logger import get_logger
        logger = get_logger()
        logger.info(tr("on_inited_logger"))