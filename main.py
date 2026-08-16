
# -*- coding: utf-8 -*-
import os
import json
from decimal import Decimal, InvalidOperation

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

KV = r'''
#:import dp kivy.metrics.dp

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(10)

        Label:
            text: "🧮 الحاسبة الذكية"
            font_size: "25sp"
            bold: True
            size_hint_y: None
            height: dp(50)

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)

                Label:
                    text: "العملية الأساسية"
                    font_size: "20sp"
                    bold: True
                    size_hint_y: None
                    height: dp(40)

                Label:
                    text: "الرقم الأول"
                    halign: "right"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(28)

                TextInput:
                    id: first_number
                    hint_text: "مثال: 1133.543"
                    input_filter: "float"
                    multiline: False
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(52)
                    padding: dp(12)

                Label:
                    text: "العملية"
                    halign: "right"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(28)

                Spinner:
                    id: operation
                    text: "×"
                    values: ["+", "−", "×", "÷"]
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(52)

                Label:
                    text: "الرقم الثاني"
                    halign: "right"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(28)

                TextInput:
                    id: second_number
                    hint_text: "مثال: 2"
                    input_filter: "float"
                    multiline: False
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(52)
                    padding: dp(12)

                Button:
                    text: "احسب النتيجة"
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(55)
                    on_release: root.calculate_first()

                Label:
                    text: "الناتج"
                    font_size: "18sp"
                    bold: True
                    size_hint_y: None
                    height: dp(30)

                Label:
                    text: root.result_text
                    font_size: "26sp"
                    bold: True
                    halign: "center"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(60)

                Label:
                    text: "🔄 عملية جديدة باستخدام الناتج السابق"
                    font_size: "20sp"
                    bold: True
                    size_hint_y: None
                    height: dp(45)

                Label:
                    text: "الرقم الجديد"
                    halign: "right"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(28)

                TextInput:
                    id: new_number
                    hint_text: "اكتب الرقم الجديد هنا"
                    input_filter: "float"
                    multiline: False
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(52)
                    padding: dp(12)

                Label:
                    text: "العملية مع الناتج السابق"
                    halign: "right"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(28)

                Spinner:
                    id: second_operation
                    text: "×"
                    values: ["+", "−", "×", "÷"]
                    font_size: "20sp"
                    size_hint_y: None
                    height: dp(52)

                Button:
                    text: "احسب باستخدام الناتج السابق"
                    font_size: "19sp"
                    size_hint_y: None
                    height: dp(55)
                    on_release: root.calculate_again()

                Label:
                    text: "الناتج الجديد"
                    font_size: "18sp"
                    bold: True
                    size_hint_y: None
                    height: dp(30)

                Label:
                    text: root.second_result_text
                    font_size: "26sp"
                    bold: True
                    halign: "center"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(60)

                BoxLayout:
                    size_hint_y: None
                    height: dp(55)
                    spacing: dp(8)

                    Button:
                        text: "📄 ملف نصي جديد"
                        font_size: "17sp"
                        on_release: root.new_file()

                    Button:
                        text: "💾 حفظ الحساب"
                        font_size: "17sp"
                        on_release: root.save_calculation()

                Button:
                    text: "📁 الملفات المحفوظة"
                    font_size: "18sp"
                    size_hint_y: None
                    height: dp(55)
                    on_release: root.show_files()

                Button:
                    text: "مسح الحقول"
                    font_size: "18sp"
                    size_hint_y: None
                    height: dp(50)
                    on_release: root.clear_all()


<FileScreen>:
    name: "files"
    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(10)

        Label:
            text: "📁 الملفات والنصوص"
            font_size: "24sp"
            bold: True
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: file_name
            hint_text: "اسم الملف"
            multiline: False
            font_size: "18sp"
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: file_content
            hint_text: "اكتب النص هنا..."
            font_size: "18sp"

        BoxLayout:
            size_hint_y: None
            height: dp(55)
            spacing: dp(8)

            Button:
                text: "💾 حفظ"
                font_size: "18sp"
                on_release: root.save_file()

            Button:
                text: "🗑 مسح"
                font_size: "18sp"
                on_release: root.clear_file()

        Button:
            text: "↩ العودة للحاسبة"
            font_size: "18sp"
            size_hint_y: None
            height: dp(55)
            on_release: app.root.current = "main"

        Label:
            id: files_list
            text: "لا توجد ملفات محفوظة"
            font_size: "16sp"
            halign: "right"
            valign: "top"
            text_size: self.size
'''

class MainScreen(Screen):
    result_text = StringProperty("—")
    second_result_text = StringProperty("—")
    previous_result = None

    def _number(self, value):
        value = value.strip()
        if not value:
            raise ValueError("أدخل رقمًا أولًا.")
        try:
            return Decimal(value)
        except InvalidOperation:
            raise ValueError("الرقم غير صحيح.")

    def _calculate(self, a, b, op):
        if op == "+": return a + b
        if op == "−": return a - b
        if op == "×": return a * b
        if op == "÷":
            if b == 0:
                raise ValueError("لا يمكن القسمة على صفر.")
            return a / b

    def _format(self, value):
        text = format(value, "f")
        return text.rstrip("0").rstrip(".") if "." in text else text

    def _popup(self, message, title="تنبيه"):
        Popup(title=title, content=Label(text=message, font_size="18sp"),
              size_hint=(0.86, 0.30)).open()

    def calculate_first(self):
        try:
            a = self._number(self.ids.first_number.text)
            b = self._number(self.ids.second_number.text)
            result = self._calculate(a, b, self.ids.operation.text)
            self.previous_result = result
            self.result_text = self._format(result)
            self.second_result_text = "—"
        except ValueError as e:
            self._popup(str(e))

    def calculate_again(self):
        if self.previous_result is None:
            self._popup("احسب العملية الأولى أولًا.")
            return
        try:
            new_number = self._number(self.ids.new_number.text)
            result = self._calculate(self.previous_result, new_number,
                                     self.ids.second_operation.text)
            self.second_result_text = self._format(result)
            self.previous_result = result
        except ValueError as e:
            self._popup(str(e))

    def clear_all(self):
        for key in ("first_number", "second_number", "new_number"):
            self.ids[key].text = ""
        self.ids.operation.text = "×"
        self.ids.second_operation.text = "×"
        self.result_text = "—"
        self.second_result_text = "—"
        self.previous_result = None

    def new_file(self):
        self.manager.current = "files"
        screen = self.manager.get_screen("files")
        screen.ids.file_name.text = ""
        screen.ids.file_content.text = ""

    def save_calculation(self):
        if self.result_text == "—":
            self._popup("احسب نتيجة أولًا ثم اضغط حفظ الحساب.")
            return
        data = {
            "الرقم الأول": self.ids.first_number.text,
            "العملية": self.ids.operation.text,
            "الرقم الثاني": self.ids.second_number.text,
            "الناتج": self.result_text,
            "الرقم الجديد": self.ids.new_number.text,
            "العملية الثانية": self.ids.second_operation.text,
            "الناتج الجديد": self.second_result_text,
        }
        folder = App.get_running_app().files_dir
        path = os.path.join(folder, "الحسابات.json")
        try:
            old = []
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    old = json.load(f)
            old.append(data)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(old, f, ensure_ascii=False, indent=2)
            self._popup("تم حفظ الحساب بنجاح.", "تم الحفظ")
        except Exception as e:
            self._popup(f"حدث خطأ أثناء الحفظ:\n{e}")

    def show_files(self):
        screen = self.manager.get_screen("files")
        screen.load_files()
        self.manager.current = "files"


class FileScreen(Screen):
    def _popup(self, message, title="تنبيه"):
        Popup(title=title, content=Label(text=message, font_size="18sp"),
              size_hint=(0.86, 0.30)).open()

    def save_file(self):
        name = self.ids.file_name.text.strip()
        content = self.ids.file_content.text
        if not name:
            self._popup("اكتب اسمًا للملف.")
            return
        safe_name = "".join(c for c in name if c not in '/\\:*?"<>|')
        if not safe_name:
            self._popup("اسم الملف غير صالح.")
            return
        folder = os.path.join(App.get_running_app().files_dir, "text_files")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, safe_name + ".txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            self._popup("تم حفظ الملف.", "تم الحفظ")
            self.load_files()
        except Exception as e:
            self._popup(f"تعذر الحفظ:\n{e}")

    def clear_file(self):
        self.ids.file_name.text = ""
        self.ids.file_content.text = ""

    def load_files(self):
        folder = os.path.join(App.get_running_app().files_dir, "text_files")
        os.makedirs(folder, exist_ok=True)
        files = sorted(f for f in os.listdir(folder) if f.endswith(".txt"))
        self.ids.files_list.text = (
            "لا توجد ملفات محفوظة." if not files else
            "الملفات المحفوظة:\n\n" + "\n".join(f"• {f[:-4]}" for f in files)
        )


class SmartCalculatorApp(App):
    title = "الحاسبة الذكية"

    def build(self):
        Window.clearcolor = (0.94, 0.95, 0.97, 1)
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(FileScreen())
        return sm

if __name__ == "__main__":
    SmartCalculatorApp().run()
