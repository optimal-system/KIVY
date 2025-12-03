import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
# from kivy.lang import Builder

class FormApp(App):
    def build(self):
        self.ports = ['Arcachon','La Rochelle','Quimper','Lorient','Brest','Morlaix',"Ploumanac'h",'Paimpol','Le Havre','Dunkerke']
#         Builder.load_file('boma-config-04.kv')
        return BoxLayout(orientation='vertical', padding=10, spacing=10)

    def on_start(self):
        # On remplit le Spinner avec la liste des ports au démarrage de l'application
        self.root.ids.port_spinner.values = self.ports
        self.root.ids.ssid_input.text = "CITRONEL"

    def submit_form(self):
        try:
            data = {
                'SSID': self.root.ids.ssid_input.text,
                'password': self.root.ids.password_input.text,
                'port': self.root.ids.port_spinner.text,
                'seuil': float(self.root.ids.seuil_input.text),
                'depart': int(self.root.ids.depart_input.text),
                'retour': int(self.root.ids.retour_input.text)
            }

            with open('config.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.root.add_widget(
                Label(text='Configuration sauvegardée !', color=(0, 1, 0, 1))
            )
        except ValueError:
            self.root.add_widget(
                Label(text='Erreur : seuil, départ ou retour invalide.', color=(1, 0, 0, 1))
            )

if __name__ == '__main__':
    FormApp().run()
