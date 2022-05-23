from pathlib import Path
import os
import datetime
import Config.ObsidianFilePath as ObsidianFilePath

LastRunIsToday = False

_lastRunFilePath = Path(ObsidianFilePath.lastRun)

# Last fun file exist
if (_lastRunFilePath.is_file()):
    # Get last modified date
    fileTimeStamp = os.path.getmtime(_lastRunFilePath)
    fileTime = datetime.datetime.fromtimestamp(fileTimeStamp)

    # If today
    LastRunIsToday = fileTime.date() == datetime.datetime.today().date()

    if (LastRunIsToday == False):
        # Update last run file
        with open(_lastRunFilePath, 'w') as emptyFile:
            pass
else:
    # Create last fun file
    with open(_lastRunFilePath, 'w') as emptyFile:
        pass
