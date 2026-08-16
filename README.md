# الحاسبة الذكية

مشروع Kivy عربي يحتوي على:
- حاسبة جمع/طرح/ضرب/قسمة.
- رقم جديد مستقل يستخدم الناتج السابق.
- حفظ الحسابات.
- إنشاء وحفظ ملفات نصية.
- ملف buildozer.spec جاهز للبناء.

تشغيل الكمبيوتر:
```bash
pip install kivy
python main.py
```

بناء APK:
```bash
pip install buildozer
buildozer android debug
```

بعد نجاح البناء ستجد APK داخل مجلد `bin`.
يفضل بناء APK عبر Linux أو WSL أو GitHub Actions.
