# ========================================================
#               Author Brad Heffernan
# ========================================================
import os
from pathlib import Path

base_dir = os.path.dirname(os.path.realpath(__file__))
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/arcolinux-news/"])


def fetch_notice():
    try:
        items = [x for x in os.listdir(working_dir) if ".news" in x and not x.startswith("2020")]
        return items
    except:  # noqa
        return []

def fetch_news():
    try:
        items = [x for x in os.listdir(working_dir) if ".news" in x and x.startswith("2020")]
        return items
    except:  # noqa
        return []
