import urllib.parse
import datetime
import webbrowser
from pathlib import Path
import os

import ObsidianFilePath
import ObsidianUriTemplate

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
