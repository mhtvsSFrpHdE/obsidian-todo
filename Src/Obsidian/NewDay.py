import shutil
from pathlib import Path

import Config.ObsidianFilePath as ObsidianFilePath


def ResetEverydayDocument(lastRunIsToday):
    if (lastRunIsToday):
        return

    everydayTemplatePath = Path(ObsidianFilePath.everydayTemplate)
    everydayPath = Path(ObsidianFilePath.everyday)
    shutil.copyfile(everydayTemplatePath, everydayPath)
