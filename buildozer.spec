[app]

# (str) Title of your application
title = الحاسبة الذكية

# (str) Package name
package.name = 2

# (str) Package domain (needed for android/ios packaging)
package.domain = 2

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json

# (list) Application requirements
# إضافة 'openssl' و 'requests' مفيدة إذا كنت تتعامل مع إنترنت
requirements = python3,kivy

# (str) Application versioning (starting from 1.0.0)
version = 1.0.0

# (list) Application orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Android API to use. 33 هو الأكثر استقراراً حالياً
android.api = 33

# (int) Minimum API required
android.minapi = 23

# (str) Android NDK version to use. 25b هو الإصدار الأكثر توافقاً
android.ndk = 25b

# (bool) Use the Android NDK for building the app
android.accept_sdk_license = True

# (str) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Warn on root usage
warn_on_root = 1
