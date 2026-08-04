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

# Жестко указываем Buildozer использовать готовый системный SDK и лицензии
android.ndk_path = 
