[app]
# اسم التطبيق الذي سيظهر على الهاتف
title = X7 Security
# اسم الحزمة (يجب أن يكون فريداً)
package.name = x7security
package.domain = org.x7

# مكان الكود (النقطة تعني المجلد الحالي)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# إصدار التطبيق
version = 0.1

# المكتبات المطلوبة (ركزت لك على مكتبات التلجرام الأساسية)
requirements = python3==3.11.5, hostpython3==3.11.5, kivy, python-telegram-bot, httpx, anyio, httpcore, h11

# إعدادات الشاشة
orientation = portrait
fullscreen = 0

# الأذونات (ضرورية جداً لعمل البوت)
android.permissions = INTERNET

# إصدارات أندرويد المستقرة للبناء السحابي
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a

# إعدادات إضافية لضمان النجاح
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
