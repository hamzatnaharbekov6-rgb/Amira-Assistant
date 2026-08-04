# __version__ = "1.0"
# buildozer: requirements = python3==3.10.14,kivy,kivymd,plyer,pyjnius==1.5.0
import os
from kivy.app import App
from kivymd.app import MDApp
from kivymd.ui.screen import MDScreen
from kivymd.ui.button import MDFloatingActionButton
from kivymd.ui.label import MDLabel
from kivymd.ui.boxlayout import MDBoxLayout
import datetime

# Подключаем Android-компоненты для работы с микрофоном
try:
    from jnius import autoclass
    Intent = autoclass('android.content.Intent')
    RecognizerIntent = autoclass('android.speech.RecognizerIntent')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
except:
    pass

class AmiraAssistant(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.title_label = MDLabel(
            text="Ассистент Амира",
            halign="center",
            theme_text_color="Primary",
            font_style="H4",
            size_hint_y=0.1
        )
        self.add_widget(self.title_label)

        self.label = MDLabel(
            text="Амира: Привет! Нажми на микрофон, скажи моё имя и свой запрос.",
            halign="center",
            theme_text_color="Secondary",
            font_style="H6"
        )
        self.add_widget(self.label)

        btn_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=0.2,
            adaptive_height=True
        )

        self.mic_button = MDFloatingActionButton(
            icon="microphone",
            md_bg_color=MDApp.get_running_app().theme_cls.primary_color,
            pos_hint={"center_x": .5}
        )
        self.mic_button.bind(on_press=self.start_voice_input)
        btn_layout.add_widget(self.mic_button)
        self.add_widget(btn_layout)

    def start_voice_input(self, instance):
        try:
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "ru-RU")
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Скажите что-нибудь (например: Амира, привет!)")
            
            current_activity = PythonActivity.mActivity
            # ИСПРАВЛЕНО: Маленькая буква "s" в названии метода Android
            current_activity.startActivityForResult(intent, 1)
            self.label.text = "Амира: Слушаю вас..."
        except Exception as e:
            self.label.text = "Амира: Микрофон доступен только внутри установленного APK!"

class AssistantApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        screen = MDScreen()
        self.layout = AmiraAssistant()
        screen.add_widget(self.layout)
        return screen

if __name__ == '__main__':
    AssistantApp().run()
