[app]
title = Amira
package.name = amira
package.domain = org.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy, kivymd, plyer
orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO, INTERNET
android.accept_apk_license = True
android.skip_apk_rescale = True
android.private_storage = 1

# Указываем использовать стабильные, проверенные версии инструментов
android.api = 33
android.ndk = 25b
android.build_tools_version = 33.0.0
