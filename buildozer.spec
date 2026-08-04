[app]
title = Amira
package.name = amira
package.domain = org.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Жестко фиксируем рабочую версию Python и библиотеки pyjnius
requirements = python3==3.11.9, kivy, kivymd, plyer, pyjnius==1.6.0

orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO, INTERNET
android.accept_apk_license = True
android.skip_apk_rescale = True
android.private_storage = 1
