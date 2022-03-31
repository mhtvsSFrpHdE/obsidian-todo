from pathlib import Path  # nopep8
import os  # nopep8
import sys  # nopep8

# Append source code folder
srcPath = Path(os.path.dirname(__file__)).joinpath("src")  # nopep8
sys.path.append(srcPath.joinpath("config"))  # nopep8
sys.path.append(srcPath.joinpath("obsidian"))  # nopep8

del srcPath  # nopep8

import datetime
import time
import urllib.parse
import webbrowser

import Config.ObsidianFilePath as ObsidianFilePath
import Src.Obsidian.ObsidianUriTemplate as ObsidianUriTemplate

lastRunFilePath = Path(ObsidianFilePath.lastRun)
lastRunIsToday = False
# Last fun file exist
if (lastRunFilePath.is_file()):
    # Get last modified date
    fileTimeStamp = os.path.getmtime(lastRunFilePath)
    fileTime = datetime.datetime.fromtimestamp(fileTimeStamp)

    # If today
    lastRunIsToday = fileTime.date() == datetime.datetime.today().date()

    if (lastRunIsToday == False):
        # Update last run file
        with open(lastRunFilePath, 'w') as emptyFile:
            pass
else:
    # Create last fun file
    with open(lastRunFilePath, 'w') as emptyFile:
        pass


weekIndex = datetime.datetime.today().weekday()
weekValue = ObsidianFilePath.weekArray[weekIndex]

# Encode string may contain space character to url
obsidian_uri = (ObsidianUriTemplate.obsidian
                + ObsidianUriTemplate.vault
                + urllib.parse.quote(ObsidianFilePath.vault)
                + ObsidianUriTemplate.file
                + urllib.parse.quote(weekValue))

webbrowser.open(obsidian_uri)
