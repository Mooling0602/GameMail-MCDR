# Import built-in or pypi modules.
import datetime
import re

from typing import Optional

# Import all MCDR interfaces and features.
from mcdreforged.api.all import *
from mcdreforged.minecraft.rtext.style import *

# Import interfaces and variables from plugins of MCDR.


# Init useful interfaces or variables.
psi = ServerInterface.psi() # MCDR plugin server interface.
MCDRConfig = psi.get_mcdr_config() # MCDR config data, a dict.
MCDRLocale = psi.get_mcdr_language() # Language MCDR defaults.
plgSelf = psi.get_self_metadata() # Metadata of this plugin.
plugin_id = plgSelf.id # Plugin ID of this plugin, loaded from metadata.
configDir = psi.get_data_folder() # Config and data path this plugin defaults.
serverDir = MCDRConfig["working_directory"] # Server's root path.