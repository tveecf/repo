import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR cyan][B]Bit[/B][/COLOR][COLOR azure]Matrix[/COLOR]'
BUILDERNAME = 'BitMatrix'
EXCLUDES = [ADDON_ID, 'repository.bitorbit']
# Text File with build info in it. Please read https://github.com/a4k-openproject/plugin.program.openwizard/wiki/Installing-Builds
BUILDFILE = 'https://raw.githubusercontent.com/tveecf/tveecf.github.io/main/setup/txt/builds.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'https://raw.githubusercontent.com/tveecf/tveecf.github.io/main/setup/txt/apks.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = 'Video Anleitungen'
YOUTUBEFILE = 'https://raw.githubusercontent.com/tveecf/tveecf.github.io/main/setup/txt/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'https://raw.githubusercontent.com/tveecf/tveecf.github.io/main/setup/data/addons.json'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'https://raw.githubusercontent.com/tveecf/tveecf.github.io/main/setup/txt/advanced.txt'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '___'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'cyan'
COLOR2 = 'azure'
# Primary menu items   / {0} is the menu item and is required
THEME1 = u'[COLOR {color1}][I][COLOR {color1}][B][/B][/COLOR][COLOR {color2}][COLOR {color1}][/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Aktuelles Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Aktuelles Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'No'
# You can add \n to do line breaks
CONTACT = 'Wir weisen ausdrücklich darauf hin, dass wir lediglich für das Design und die Entwicklung einzelner Plugins zuständig sind und keinerlei Haftung auf den Inhalt von Drittanbietern übernehmen können. Wir sind stets bemüht Fehler & Bugs zu entfernen.\n\nSollten Sie auf Fehler stoßen, so bitten wir Sie uns dies in kurzer Form mitzuteilen. Wir danken euch!\n\nGitHub: http://www.github.com/tveecf/plugin.program.bitmatrix/\n\nGitHub: http://www.github.com/tveecf/plugin.program.bitmatrix\n\nTelegram: https://t.me/bitorbitcf\n\nWebsite: https://bittv.ga'
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = os.path.join(ART, 'qricon.png')
CONTACTFANART = os.path.join(ART, 'ContentPanel.png')
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = 'repository.bitorbit'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'https://raw.githubusercontent.com/tveecf/repo/master/addons.xml'
# Url to folder zip is located in
REPOZIPURL = 'https://github.com/tveecf/repo/blob/master/repository.bitorbit/'
#########################################################

#########################################################
#        Notification Window                            #
#######################################0##################
# Enable Notification screen Yes or No
ENABLE = 'No'
# Url to notification file
NOTIFICATION = 'http://'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Image'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR cyan][B]Bit[/B][/COLOR][COLOR azure]Matrix[/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE = 'https://tveecf.github.io/img/kovibanner.png'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = os.path.join(ART, 'ContentPanel.png')
#########################################################
