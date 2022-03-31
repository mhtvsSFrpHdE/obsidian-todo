import shutil

import Config.ObsidianFilePath as ObsidianFilePath


def ResetEverydayDocument(lastRunIsToday):
    if (lastRunIsToday):
        return

    shutil.copyfile(ObsidianFilePath.everydayTemplate, ObsidianFilePath.everyday)
