[app]

# (str) Title of your application
title = Monitor Patio

# (str) Package name
package.name = monitorpatio

# (str) Package domain (needed for android packaging)
package.domain = org.monitor

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android NDK version to use
android.ndk_version = 28c

# (bool) Enable/Disable pip/buildozer acceptance of android licenses
android.accept_sdk_license = True
