[app]
title = Amira
package.name = amira
package.domain = org.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Чистый список без знаков "==", чтобы Buildozer не сходил с ума
requirements = python3, kivy, kivymd, plyer, pyjnius

orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO, INTERNET
android.accept_apk_license = True
android.skip_apk_rescale = True
android.private_storage = 1

# Фиксируем стабильные инструменты сборки Google Android
android.api = 33
android.ndk = 25b
android.build_tools_version = 33.0.0

[buildozer]
log_level = 2
warn_on_root = 1
