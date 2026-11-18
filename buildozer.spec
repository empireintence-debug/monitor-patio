[app]

# (str) Title of your application
title = Monitor Patio

# (str) Package name
package.name = monitorpatio

# (str) Package domain (needed for android packaging)
package.domain = org.empireintence

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android X
android.androidx = True
