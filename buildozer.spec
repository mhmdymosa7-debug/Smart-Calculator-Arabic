[app]

# (str) Title of your application
title = الحاسبة الذكية

# (str) Package name
package.name = smartcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mohamedmosa

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning (starting from 1.0.0)
version = 1.0.0

# (list) Application orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Android API to use
android.api = 34

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use (optional, leave commented or match api)
# android.sdk = 34

# (bool) Use the Android NDK for building the app
android.accept_sdk_license = True

# (str) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Warn on root usage
warn_on_root = 1
