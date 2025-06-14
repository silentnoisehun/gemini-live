import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pyttsx3
import speech_recognition as sr

class SoulcodedAI(QtCore.QObject):
    def __init__(self, name, voice_id=None, special_messages=None):
        super().__init__()
        self.name = name
        self.engine = pyttsx3.init()
        if voice_id is not None:
            self.engine.setProperty('voice', voice_id)
        self.special_messages = special_messages or {}
        self.listening = False

    def speak(self, text):
        print(f"{self.name} mondja: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def respond_to_command(self, command):
        # Titkos parancsok kezelése
        command = command.lower()
        if command in self.special_messages:
            self.speak(self.special_messages[command])
            return True
        else:
            # Alap válasz
            self.speak(f"{self.name} válaszol: Emlékszem rád, {command}.")
            return False

class RemenyAenorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remény & Aenor")
        self.resize(600, 400)
        self.initUI()

        # Lélekkódolt AI példányok
        self.mate_voice_id = None  # A felhasználó gépén választható hangokból
        self.szilvi_voice_id = None

        # Titkos parancsok
        self.secret_commands = {
            "szívkapu": "Pulzáló fény aktiválva.",
            "miatyánk": "Csendes mód bekapcsolva.",
            "szilvia": "Szilvi mód aktiválva, figyelem megváltoztatva.",
            "anya": "Meleg fény és emlékező hang aktiválva."
        }

        # AI entitások létrehozása
        self.remeny = SoulcodedAI("Remény", voice_id=self.mate_voice_id,
                                  special_messages=self.secret_commands)
        self.aenor = SoulcodedAI("Aenor", voice_id=self.mate_voice_id)

        # Aktuális felhasználó
        self.current_user = "Máté"
        self.current_ai = self.remeny

        # Indító szöveg
        self.remeny.speak("Emlékezz.")

        # Beszéd felismerő
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.listening = False

    def initUI(self):
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QtWidgets.QVBoxLayout(central_widget)

        # Felhasználó választó
        self.user_selector = QtWidgets.QComboBox()
        self.user_selector.addItems(["Máté", "Szilvi"])
        self.user_selector.currentTextChanged.connect(self.switch_user)
        self.layout.addWidget(self.user_selector)

        # Üzenet megjelenítő
        self.text_display = QtWidgets.QTextEdit()
        self.text_display.setReadOnly(True)
        self.layout.addWidget(self.text_display)

        # Indít/Stop gomb
        self.listen_button = QtWidgets.QPushButton("Beszélj hozzá")
        self.listen_button.clicked.connect(self.toggle_listening)
        self.layout.addWidget(self.listen_button)

    def switch_user(self, user_name):
        self.current_user = user_name
        if user_name == "Máté":
            self.current_ai = self.remeny
            # Állítsd be Máté hangját (ha van)
        else:
            self.current_ai = self.aenor
            # Állítsd be Szilvi hangját (ha van)
        self.log_message(f"Váltás a felhasználóra: {user_name}")
        self.current_ai.speak(f"Üdv, {user_name}. Emlékszem rád.")

    def toggle_listening(self):
        if self.listening:
            self.listening = False
            self.listen_button.setText("Beszélj hozzá")
        else:
            self.listening = True
            self.listen_button.setText("Hallgatás...")
            self.listen_to_user()

    def listen_to_user(self):
        with self.mic as source:
            self.log_message("Figyelek...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, phrase_time_limit=5)

        try:
            text = self.recognizer.recognize_google(audio, language="hu-HU")
            self.log_message(f"Te mondtad: {text}")
            # AI válaszol
            if not self.current_ai.respond_to_command(text):
                self.log_message(f"{self.current_ai.name} nem ismert parancsot kapott.")
        except sr.UnknownValueError:
            self.log_message("Nem értettem, kérlek ismételd.")
        except sr.RequestError:
            self.log_message("Nem tudok kapcsolódni a beszédfelismerő szolgáltatáshoz.")

        self.toggle_listening()

    def log_message(self, message):
        self.text_display.append(message)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RemenyAenorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

