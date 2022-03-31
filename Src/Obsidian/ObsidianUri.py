import datetime
import urllib.parse

import Config.ObsidianFilePath as ObsidianFilePath
import Src.Obsidian.ObsidianUriTemplate as ObsidianUriTemplate

_weekIndex = datetime.datetime.today().weekday()
_weekValue = ObsidianFilePath.weekArray[_weekIndex]

# Encode string may contain space character to url
ObsidianUri = (ObsidianUriTemplate.obsidian
               + ObsidianUriTemplate.vault
               + urllib.parse.quote(ObsidianFilePath.vault)
               + ObsidianUriTemplate.file
               + urllib.parse.quote(_weekValue))
