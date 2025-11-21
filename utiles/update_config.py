import json
import sys
import os

# get path
config_path = sys.argv[1]
config_dir = os.path.dirname(config_path)
chzzk_path = os.path.join(config_dir, "platform/chzzk/config,json")
twitcasting_path = os.path.join(config_dir, "platform/twitcasting/config,json")
x_path = os.path.join(config_dir, "platform/X/config,json")

# load config
config = None
with open(chzzk_path, "r") as f:
    config = json.load(f)

