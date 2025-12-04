[app]
title = BOMAconfiguration
package.name = BOMAconf
package.domain = optimal-system.com
source.dir = .
source.include_exts = py,png,jpg,kv
source.exclude_exts = spec,pyc,pyo,bin
source.exclude_dirs = tests, bin, venv, .git
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[android]
arch = armeabi-v7a
permissions = INTERNET
private_storage = True
accept_sdk_license = True
