from pathlib import Path
import os
import datetime
import Config.ObsidianFilePath as ObsidianFilePath
import Config.Setting as Setting

LastRunIsToday = False

_lastRunFilePath = Path(ObsidianFilePath.lastRun)

# When read only
# skip update last run file and assume it has already updated by server
if Setting.readOnly:
    LastRunIsToday = True

else:
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
