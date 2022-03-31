from pathlib import Path  # nopep8
import os  # nopep8
import sys  # nopep8

# Append source code folder
srcPath = Path(os.path.dirname(__file__)).joinpath("src")  # nopep8
sys.path.append(srcPath.joinpath("Config"))  # nopep8
sys.path.append(srcPath.joinpath("Obsidian"))  # nopep8
sys.path.append(srcPath.joinpath("Debug"))  # nopep8

del srcPath  # nopep8

import time
import webbrowser

import Src.Debug.DebugFlag as DebugFlag
import Src.LastRun.LastRun as LastRun
import Src.Obsidian.NewDay as NewDay
import Src.Obsidian.ObsidianUri as ObsidianUri

NewDay.ResetEverydayDocument(LastRun.LastRunIsToday)

if (DebugFlag.SkipOpenObsidian == False):
    webbrowser.open(ObsidianUri.ObsidianUri)

# Why sleep
# https://forum.obsidian.md/t/obisidian-uri-will-not-open-obsidian-if-parent-process-exit-too-fast/34978
time.sleep(60)
