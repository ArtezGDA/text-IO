Last login: Thu Dec  3 10:40:14 on ttys001
[esmeeellson@MacBook-Pro-van-Esmee-Ellson: ~]%  ps                         [422]
  PID TTY           TIME CMD
35333 ttys000    0:00.06 -bash
36231 ttys000    0:00.14 /bin/zsh
59252 ttys001    0:00.13 -zsh
37144 ttys002    0:00.78 -zsh
36646 ttys003    0:00.06 -zsh
88054 ttys000    0:00.16 -zsh
[esmeeellson@MacBook-Pro-van-Esmee-Ellson: ~]% ps-ax                      [423]
zsh: command not found: ps-ax
[esmeeellson@MacBook-Pro-van-Esmee-Ellson: ~]% ps - ax                    [424]
ps: illegal argument: -
usage: ps [-AaCcEefhjlMmrSTvwXx] [-O fmt | -o fmt] [-G gid[,gid...]]
          [-g grp[,grp...]] [-u [uid,uid...]]
          [-p pid[,pid...]] [-t tty[,tty...]] [-U user[,user...]]
       ps [-L]
[esmeeellson@MacBook-Pro-van-Esmee-Ellson: ~]% ps -ax                     [425]
  PID TTY           TIME CMD
    1 ??        14:18.23 /sbin/launchd
   43 ??         0:46.28 /usr/libexec/UserEventAgent (System)
   44 ??         0:50.37 /usr/sbin/syslogd
   46 ??         0:21.16 /usr/libexec/kextd
   47 ??         1:54.68 /System/Library/Frameworks/CoreServices.framework/Versi
   49 ??         0:00.28 /usr/libexec/thermald
   51 ??         0:03.47 /System/Library/CoreServices/appleeventsd --server
   52 ??         0:58.91 /usr/libexec/configd
   53 ??         0:25.72 /System/Library/CoreServices/powerd.bundle/powerd
   57 ??         0:58.65 /usr/libexec/airportd
   59 ??         0:02.12 /usr/libexec/warmd
   60 ??         5:56.02 /System/Library/Frameworks/CoreServices.framework/Frame
   66 ??         0:04.55 /usr/libexec/diskarbitrationd
   74 ??        21:58.42 /usr/libexec/opendirectoryd
   75 ??         0:05.17 /usr/sbin/wirelessproxd
   77 ??         0:19.03 /System/Library/PrivateFrameworks/ApplePushService.fram
   78 ??         0:00.93 /Library/Application Support/Adobe/Adobe Desktop Common
   79 ??         0:59.26 /System/Library/CoreServices/launchservicesd
   80 ??         0:25.48 /System/Library/PrivateFrameworks/MobileDevice.framewor
   81 ??         1:05.92 /usr/sbin/securityd -i
   83 ??         0:24.93 /usr/libexec/locationd
   86 ??         0:00.14 autofsd
   88 ??         0:24.94 /usr/sbin/blued
   92 ??         1:23.68 /usr/sbin/mDNSResponder
   94 ??         0:00.08 /usr/libexec/stackshot -t -O
   95 ??         0:00.81 /System/Library/PrivateFrameworks/GenerationalStorage.f
   96 ??         2:32.24 /System/Library/CoreServices/loginwindow.app/Contents/M
   97 ??         0:00.33 /System/Library/CoreServices/logind
   98 ??         0:00.05 /usr/sbin/KernelEventAgent
  100 ??        26:37.67 /usr/libexec/hidd
  101 ??         0:23.82 /usr/libexec/taskgated -s
  102 ??         0:51.30 /usr/sbin/notifyd
  104 ??         0:42.98 /System/Library/CoreServices/coreservicesd
  105 ??        10:12.33 /usr/sbin/distnoted daemon
  117 ??         0:03.92 /System/Library/Frameworks/Security.framework/Versions/
  173 ??         0:00.05 /System/Library/Frameworks/PCSC.framework/Versions/A/XP
  178 ??         0:59.87 /usr/libexec/networkd
  183 ??         0:01.65 /usr/libexec/awacsd
  199 ??         0:05.00 /usr/libexec/watchdogd
  204 ??       310:21.74 /System/Library/Frameworks/ApplicationServices.framewor
  205 ??         5:37.95 /System/Library/Frameworks/CoreServices.framework/Frame
  208 ??         0:33.83 /usr/libexec/usbd
  210 ??         0:01.63 /System/Library/Frameworks/CoreMediaIO.framework/Resour
  211 ??         0:00.79 /usr/libexec/corestoraged
  213 ??         0:10.84 /usr/sbin/ntpd -c /private/etc/ntp-restrict.conf -n -g 
  218 ??         0:04.74 /System/Library/Frameworks/OpenGL.framework/Versions/A/
  223 ??         0:05.68 /System/Library/PrivateFrameworks/AmbientDisplay.framew
  255 ??         0:01.16 /usr/libexec/securityd_service
  257 ??         0:18.91 /usr/libexec/UserEventAgent (Aqua)
  259 ??        56:36.64 /usr/sbin/distnoted agent
  262 ??         0:08.02 /usr/sbin/usernoted
  263 ??         1:09.13 /System/Library/PrivateFrameworks/CalendarAgent.framewo
  281 ??         2:57.73 /System/Library/CoreServices/Dock.app/Contents/MacOS/Do
  283 ??         1:06.69 /System/Library/CoreServices/SystemUIServer.app/Content
  286 ??        21:06.53 /usr/sbin/coreaudiod
  287 ??         0:02.91 /usr/sbin/racoon -D
  295 ??         0:22.30 /System/Library/CoreServices/backupd.bundle/Contents/Re
  297 ??         0:00.11 /usr/sbin/pboard
  300 ??         0:15.37 /usr/libexec/sharingd
  305 ??         0:09.21 /System/Library/PrivateFrameworks/IDS.framework/identit
  309 ??         2:55.70 /System/Library/Frameworks/ApplicationServices.framewor
  312 ??         0:07.43 /System/Library/PrivateFrameworks/CommerceKit.framework
  314 ??         0:14.08 /System/Library/PrivateFrameworks/CommerceKit.framework
  318 ??         0:25.19 /System/Library/CoreServices/Spotlight.app/Contents/Mac
  321 ??         0:04.03 /usr/sbin/filecoordinationd
  330 ??         0:07.49 /System/Library/PrivateFrameworks/ParsecUI.framework/Ve
  331 ??         0:04.11 /System/Library/CoreServices/Menu Extras/AirPort.menu/C
  334 ??         0:01.90 /System/Library/PrivateFrameworks/CommerceKit.framework
  347 ??         0:00.55 /System/Library/CoreServices/SocialPushAgent.app/Conten
  349 ??         0:01.49 /System/Library/CoreServices/Keychain Circle Notificati
  351 ??         0:48.20 /Users/esmeeellson/Library/Application Support/com.geni
  353 ??         0:21.09 /System/Library/CoreServices/NotificationCenter.app/Con
  355 ??         0:03.30 /Library/Application Support/Sony Application Launcher/
  360 ??         0:00.36 /System/Library/PrivateFrameworks/AskPermission.framewo
  362 ??         0:03.47 com.apple.photostream-agent
  363 ??         0:10.84 /Users/esmeeellson/Library/Application Support/Spotify/
  364 ??         0:02.51 /System/Library/PrivateFrameworks/IMCore.framework/imag
  365 ??         0:06.66 /System/Library/CoreServices/cloudpaird
  368 ??       133:56.14 /Applications/Utilities/Adobe Creative Cloud/ACC/Creati
  370 ??         0:03.75 /System/Library/CoreServices/WiFiAgent.app/Contents/Mac
  371 ??         0:05.41 /System/Library/CoreServices/diagnostics_agent
  376 ??         0:19.76 /System/Library/CoreServices/SubmitDiagInfo server-init
  377 ??         0:01.92 /System/Library/CoreServices/CrashReporterSupportHelper
  381 ??         0:01.77 /Applications/iTunes.app/Contents/MacOS/iTunesHelper.ap
  393 ??         7:44.36 /Applications/Dropbox.app/Contents/MacOS/Dropbox
  402 ??         0:04.15 /System/Library/PrivateFrameworks/CommerceKit.framework
  414 ??         0:02.32 /usr/libexec/fmfd
  428 ??         3:18.72 /Applications/Utilities/Adobe Application Manager/IPC/A
  429 ??         0:00.42 /System/Library/PrivateFrameworks/CommerceKit.framework
  434 ??         0:02.20 /System/Library/CoreServices/Dock.app/Contents/XPCServi
  436 ??         0:01.31 /Applications/Canon Utilities/IJ Network Scanner Select
  437 ??         0:01.67 /System/Library/PrivateFrameworks/CommerceKit.framework
  447 ??         4:29.94 /Applications/Utilities/Adobe Creative Cloud/ACC/Creati
  474 ??       146:51.11 /Library/Application Support/Adobe/Adobe Desktop Common
  475 ??        11:24.33 /Library/Application Support/Adobe/Adobe Desktop Common
  498 ??         4:29.17 /Library/Application Support/Adobe/Adobe Desktop Common
  520 ??         0:01.26 /System/Library/Frameworks/ApplicationServices.framewor
  521 ??         6:34.94 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
  523 ??         0:55.33 /Applications/Utilities/Adobe Creative Cloud/CCXProcess
  532 ??       146:18.94 /Library/Application Support/Adobe/Adobe Desktop Common
  534 ??         0:13.35 /Library/DropboxHelperTools/Dropbox_u501/dbfseventsd
  535 ??         0:15.04 /Library/Application Support/Adobe/Adobe Desktop Common
  537 ??         0:40.37 /Library/DropboxHelperTools/Dropbox_u501/dbfseventsd
  538 ??         0:34.98 /Library/DropboxHelperTools/Dropbox_u501/dbfseventsd
  550 ??         4:29.49 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
  563 ??         0:00.00 (ExManBridgeTalkC)
  569 ??         0:12.26 /System/Library/Image Capture/Support/Image Capture Ext
  577 ??         0:32.16 /Applications/Utilities/Adobe Creative Cloud/CCLibrary/
  579 ??         0:00.00 (ExManBridgeTalkC)
  607 ??         0:39.25 /System/Library/Frameworks/CoreServices.framework/Frame
  613 ??         0:00.73 /System/Library/Frameworks/CoreServices.framework/Frame
  614 ??         0:00.60 /System/Library/Frameworks/CoreServices.framework/Frame
  743 ??         0:00.25 /System/Library/PrivateFrameworks/KerberosHelper/Helper
  754 ??         0:00.52 /Library/PrivilegedHelperTools/com.microsoft.autoupdate
  861 ??         0:00.48 /System/Library/Frameworks/CoreServices.framework/Frame
 3753 ??         0:03.08 /System/Library/PrivateFrameworks/DiskImages.framework/
 3768 ??         0:00.12 /System/Library/PrivateFrameworks/DiskImages.framework/
 3792 ??         0:02.36 /usr/libexec/syspolicyd
 3826 ??         0:02.82 /System/Library/PrivateFrameworks/DiskImages.framework/
 3885 ??         0:15.18 /System/Library/Services/AppleSpell.service/Contents/Ma
 4461 ??         0:00.22 /usr/libexec/USBAgent
 6138 ??         0:02.11 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
 6139 ??         0:01.40 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
 8045 ??         0:05.13 /System/Library/PrivateFrameworks/Noticeboard.framework
 8062 ??         0:00.22 /System/Library/PrivateFrameworks/Noticeboard.framework
 9814 ??         2:37.39 /usr/libexec/nsurlstoraged
10845 ??         0:38.10 /usr/sbin/spindump
13172 ??         0:00.33 /System/Library/Services/AppleSpell.service/Contents/Ma
13343 ??         0:15.23 /System/Library/Frameworks/WebKit.framework/Versions/A/
14508 ??         0:03.32 /System/Library/PrivateFrameworks/TelephonyUtilities.fr
15217 ??         0:00.36 /System/Library/PrivateFrameworks/DiskImages.framework/
15257 ??         0:33.90 /System/Library/PrivateFrameworks/PackageKit.framework/
15289 ??         0:00.55 /System/Library/PrivateFrameworks/DiskImages.framework/
15509 ??         0:00.52 /System/Library/PrivateFrameworks/DiskImages.framework/
16000 ??        12:27.83 /System/Library/CoreServices/Software Update.app/Conten
16001 ??         0:00.95 /System/Library/PrivateFrameworks/SoftwareUpdate.framew
22191 ??         0:00.32 /System/Library/Services/AppleSpell.service/Contents/Ma
22214 ??         0:27.10 /System/Library/PrivateFrameworks/DiskImages.framework/
28617 ??         0:00.22 /System/Library/Services/AppleSpell.service/Contents/Ma
28691 ??         0:00.22 /System/Library/Services/AppleSpell.service/Contents/Ma
32027 ??         0:00.13 /System/Library/Frameworks/DiskArbitration.framework/Ve
40356 ??         0:28.83 /Applications/Sublime Text.app/Contents/MacOS/Sublime T
40369 ??         0:00.76 /Applications/Sublime Text.app/Contents/MacOS/plugin_ho
40414 ??         0:01.09 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
40415 ??         0:01.12 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
42711 ??        25:50.72 /Library/Application Support/Adobe/Adobe Desktop Common
43217 ??         0:00.42 /System/Library/Frameworks/InputMethodKit.framework/Res
54263 ??         0:00.20 /System/Library/Frameworks/CoreServices.framework/Frame
54310 ??         0:03.72 /usr/libexec/nsurlsessiond
60687 ??        62:29.10 /System/Library/CoreServices/Dock.app/Contents/Resource
61472 ??         0:13.88 /usr/sbin/cfprefsd agent
61473 ??         0:09.52 /usr/sbin/cfprefsd daemon
61541 ??         9:02.33 /System/Library/CoreServices/Finder.app/Contents/MacOS/
61545 ??         0:02.19 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
61546 ??         0:02.48 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
61553 ??         0:01.77 /System/Library/PrivateFrameworks/CommerceKit.framework
61557 ??        14:48.12 /Applications/Safari.app/Contents/MacOS/Safari
61563 ??        25:55.79 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61597 ??        37:04.07 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61657 ??        10:09.23 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61669 ??        17:01.63 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61680 ??        29:13.34 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61683 ??         0:00.66 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
61684 ??         0:00.55 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
61691 ??         2:02.28 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61695 ??         0:54.76 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61696 ??         5:09.59 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61700 ??        21:09.40 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61701 ??         2:08.60 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61707 ??         2:21.28 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61708 ??         2:29.39 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61709 ??        13:17.01 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61715 ??         3:20.07 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61716 ??         2:52.12 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61719 ??         1:58.44 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61720 ??         1:28.08 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61724 ??         2:25.38 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61725 ??        89:29.13 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61726 ??         1:01.30 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61749 ??         2:09.65 /System/Library/StagedFrameworks/Safari/WebKit.framewor
61756 ??        10:18.29 /Applications/GitHub Desktop.app/Contents/MacOS/GitHub 
61765 ??         0:00.86 /usr/bin/ssh-agent -l
65170 ??         4:06.64 /Applications/Adobe Photoshop CS6/Adobe Photoshop CS6.a
65178 ??         1:10.45 /Applications/Adobe Photoshop CS6/Adobe Photoshop CS6.a
65190 ??         0:00.74 /Library/Application Support/Adobe/CS6ServiceManager/CS
65192 ??         0:00.00 (adobe_licutil)
65424 ??         0:00.86 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
66082 ??        32:25.72 /Applications/Adobe InDesign CC 2015/Adobe InDesign CC 
66085 ??         0:00.47 /System/Library/PrivateFrameworks/PerformanceAnalysis.f
66090 ??         0:03.59 /usr/libexec/amfid
66091 ??         1:02.99 /Applications/Adobe InDesign CC 2015/Adobe InDesign CC 
66092 ??         0:00.41 /System/Library/Frameworks/Security.framework/Versions/
66093 ??         0:00.55 /System/Library/PrivateFrameworks/MessagesKit.framework
66094 ??         0:02.94 /System/Library/CoreServices/lsuseractivityd
66095 ??         0:04.76 /usr/libexec/secinitd
66096 ??         0:04.97 /System/Library/PrivateFrameworks/TCC.framework/Resourc
66097 ??         0:24.26 /usr/libexec/coreduetd
66098 ??         0:00.34 /usr/libexec/nsurlstoraged
66101 ??         0:16.80 /System/Library/PrivateFrameworks/CacheDelete.framework
66102 ??         0:00.12 /usr/libexec/spindump_agent
66104 ??         0:00.12 /usr/libexec/diagnosticd
66109 ??         0:00.26 /usr/libexec/networkd_privileged
66111 ??         0:01.71 /System/Library/CoreServices/iconservicesagent
66112 ??         0:00.02 /System/Library/Frameworks/ApplicationServices.framewor
66113 ??         0:00.42 /System/Library/CoreServices/iconservicesd
66118 ??         0:20.83 /usr/libexec/systemstatsd
66120 ??         0:01.78 /usr/libexec/pkd
66121 ??         0:00.28 /System/Library/CoreServices/pbs
66122 ??         1:28.34 automountd
66124 ??         0:00.00 (sh)
66127 ??         0:00.00 (sh)
66129 ??         0:25.56 /Applications/Adobe InDesign CC 2015/Adobe InDesign CC 
66134 ??         4:10.80 /Applications/Adobe InDesign CC 2015/Adobe InDesign CC 
66162 ??         0:01.06 /System/Library/Frameworks/Accounts.framework/Versions/
66163 ??         0:00.34 /System/Library/PrivateFrameworks/TCC.framework/Resourc
66166 ??         0:00.25 /usr/libexec/sandboxd -n PluginProcess -n 
66167 ??         0:00.88 /System/Library/PrivateFrameworks/CoreSymbolication.fra
66221 ??         0:04.30 sysmond
66236 ??         0:00.00 (sh)
66415 ??         0:07.06 /System/Library/PrivateFrameworks/CloudKitDaemon.framew
66431 ??         0:00.04 /System/Library/CryptoTokenKit/com.apple.ifdreader.slot
66450 ??         0:18.45 /usr/sbin/distnoted agent
66513 ??         0:00.04 /System/Library/Frameworks/GSS.framework/Helpers/com.ap
66596 ??         0:00.55 /System/Library/PrivateFrameworks/WirelessDiagnostics.f
66602 ??         0:04.07 /System/Library/PrivateFrameworks/CoreRecents.framework
66604 ??         0:00.52 /System/Library/PrivateFrameworks/CloudServices.framewo
66605 ??         0:00.21 /System/Library/PrivateFrameworks/AccountPolicy.framewo
66606 ??         0:01.37 /System/Library/CoreServices/AirPlayUIAgent.app/Content
66612 ??         0:00.10 /System/Library/PrivateFrameworks/IMFoundation.framewor
66613 ??         0:03.75 /System/Library/PrivateFrameworks/CalendarAgent.framewo
66615 ??         0:01.10 /usr/libexec/secd
66618 ??         0:01.73 /System/Library/PrivateFrameworks/InternetAccounts.fram
66622 ??         0:00.08 /System/Library/Frameworks/Security.framework/Versions/
66623 ??         0:00.20 /System/Library/PrivateFrameworks/CloudServices.framewo
66631 ??         0:00.99 /System/Library/PrivateFrameworks/CloudServices.framewo
67015 ??         0:00.29 /System/Library/Frameworks/InputMethodKit.framework/Ver
67016 ??         0:00.14 /System/Library/PrivateFrameworks/CloudDocsDaemon.frame
67507 ??         0:06.34 /System/Library/Frameworks/ApplicationServices.framewor
67565 ??         0:01.12 /System/Library/CoreServices/mapspushd
68337 ??         0:02.66 /System/Library/PrivateFrameworks/SafariShared.framewor
68971 ??         0:00.04 /System/Library/PrivateFrameworks/SystemAdministration.
69043 ??         0:00.03 /usr/libexec/smd
69191 ??        13:39.21 /Applications/P-touch Editor 5.1/P-touch Editor.app/Con
69431 ??         0:00.28 /System/Library/PrivateFrameworks/SafariShared.framewor
69894 ??         0:01.21 /System/Library/CoreServices/CoreServicesUIAgent.app/Co
70157 ??         0:00.12 /usr/libexec/nehelper
70272 ??         0:00.03 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
70273 ??         0:00.11 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
70687 ??         0:00.57 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
70688 ??         0:00.65 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
70840 ??         2:00.04 /Applications/Adobe Reader.app/Contents/MacOS/AdobeRead
71549 ??         0:00.20 /usr/libexec/SafariNotificationAgent
72003 ??         0:02.02 /System/Library/PrivateFrameworks/SpeechRecognitionCore
72226 ??         0:01.91 /Applications/Preview.app/Contents/MacOS/Preview
72231 ??         0:00.08 /System/Library/PrivateFrameworks/BookKit.framework/Ver
72234 ??         0:00.27 /System/Library/CoreServices/ScopedBookmarkAgent
72240 ??         0:00.04 /System/Library/Frameworks/ApplicationServices.framewor
72679 ??         3:11.56 /Applications/Microsoft Word.app/Contents/MacOS/Microso
72699 ??         0:00.33 /Library/Application Support/Microsoft/MAU2.0/Microsoft
72707 ??         0:00.51 /System/Library/PrivateFrameworks/RemoteViewServices.fr
73484 ??         0:48.24 /Users/esmeeellson/Downloads/Mou.app/Contents/MacOS/Mou
73883 ??         0:00.02 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
73884 ??         0:00.11 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
74383 ??         0:00.09 /System/Library/PrivateFrameworks/DataDetectorsCore.fra
75496 ??         2:44.20 /Applications/Adobe Illustrator CC 2015/Adobe Illustrat
75509 ??         0:27.03 /Applications/Adobe Illustrator CC 2015/Adobe Illustrat
75512 ??         0:00.02 /System/Library/Frameworks/ApplicationServices.framewor
75564 ??         0:00.57 /Applications/Utilities/Adobe Creative Cloud/CoreSync/C
75565 ??         0:00.38 /Applications/Dropbox.app/Contents/PlugIns/garcon.appex
76098 ??         0:01.79 /System/Library/CoreServices/AppleIDAuthAgent
77122 ??         0:00.41 /usr/sbin/diskmanagementd
77129 ??         0:00.02 /System/Library/CoreServices/iconservicesagent
77599 ??         0:00.01 /usr/libexec/periodic-wrapper daily
77871 ??         0:00.07 /System/Library/PrivateFrameworks/CommerceKit.framework
79226 ??         0:02.95 /System/Library/PrivateFrameworks/CloudDocsDaemon.frame
80086 ??         0:00.02 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
80087 ??         0:00.09 /System/Library/Frameworks/AudioToolbox.framework/XPCSe
80612 ??         0:00.02 /System/Library/Frameworks/ApplicationServices.framewor
80856 ??         0:00.18 /System/Library/PrivateFrameworks/CloudPhotoServices.fr
80857 ??         0:04.48 /System/Library/PrivateFrameworks/PhotoLibraryPrivate.f
80867 ??         0:00.56 /System/Library/PrivateFrameworks/PhotoLibraryPrivate.f
80868 ??         0:00.51 /System/Library/CoreServices/cloudphotosd.app/Contents/
80872 ??         0:00.57 /System/Library/PrivateFrameworks/GeoServices.framework
80884 ??         0:00.10 /System/Library/PrivateFrameworks/PhotoLibraryPrivate.f
81285 ??         0:00.16 /Users/esmeeellson/Library/Application Support/Spigot/A
82331 ??        10:06.55 /Applications/Utilities/Terminal.app/Contents/MacOS/Ter
83631 ??        20:12.44 /Volumes/Sublime Text/Sublime Text.app/Contents/MacOS/S
83670 ??         0:17.71 /Volumes/Sublime Text/Sublime Text.app/Contents/MacOS/p
85196 ??         0:00.05 /System/Library/Services/AppleSpell.service/Contents/Ma
85253 ??         0:00.02 /System/Library/PrivateFrameworks/HelpData.framework/Ve
86370 ??         0:00.04 /usr/sbin/netbiosd
86533 ??         0:00.03 /System/Library/Services/AppleSpell.service/Contents/Ma
86703 ??         0:00.07 /System/Library/Frameworks/CoreServices.framework/Frame
86742 ??         0:00.08 /System/Library/Frameworks/CoreServices.framework/Frame
86806 ??         0:00.09 /System/Library/Frameworks/CoreServices.framework/Frame
87549 ??         0:07.23 /System/Library/StagedFrameworks/Safari/WebKit.framewor
97321 ??         0:09.39 /System/Library/Frameworks/ApplicationServices.framewor
88051 ttys000    0:00.32 login -pf esmeeellson /bin/zsh
88054 ttys000    0:00.17 -zsh
88095 ttys000    0:00.00 ps -ax
[esmeeellson@MacBook-Pro-van-Esmee-Ellson: ~]% netstat -a | grep 'adobe'  [426]
df7558c6b02865a3 stream      0      0                0 df7558c6b0285ab3                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae22a603 stream      0      0                0 df7558c6ae22a53b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ab1a9473 stream      0      0                0 df7558c6a1bc2a53                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6b028666b stream      0      0                0 df7558c6b028779b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6b02864db stream      0      0                0 df7558c6ad30dcab                0                0 /tmp/com.adobe.csi.ctrl-CS6-esmeeellson
df7558c69c9e9543 stream      0      0                0 df7558c6ae1fbefb                0                0 /tmp/com.adobe.csi.ctrl-CS6-esmeeellson
df7558c6b1e352eb stream      0      0 df7558c6a538bc2b                0                0                0 /tmp/com.adobe.csi.ctrl-CS6-esmeeellson
df7558c6ae22bf03 stream      0      0                0 df7558c6ae22bfcb                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae22c093 stream      0      0                0 df7558c6ae1fce9b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ad30c2e3 stream      0      0                0 df7558c6ad30c603                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae1fe60b stream      0      0                0 df7558c6ae1fe223                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae1fdf03 stream      0      0                0 df7558c6ae1fd1bb                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae1fc85b stream      0      0                0 df7558c6998d8ab3                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae1fbd6b stream      0      0                0 df7558c6ae22c79b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ae22c47b stream      0      0                0 df7558c6ae1fde3b                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ad30d283 stream      0      0                0 df7558c6ad30cf63                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ad30c85b stream      0      0                0 df7558c6ad30c793                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
df7558c6ad30d34b stream      0      0 df7558c6a2797feb                0                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-esmeeellson
