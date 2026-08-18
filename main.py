from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        lbl = Label(text='مرحباً بك في تطبيقي الأول!')
        btn = Button(text='اضغط هنا', size_hint=(1, 0.3))
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(lbl)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        print("تم الضغط على الزر!")

if __name__ == '__main__':
    MyApp().run()
