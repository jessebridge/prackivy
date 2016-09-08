from kivy.app import App
from kivy.lang import Builder


class convert(App):

    def build(self):
        self.title = "convert m to km"
        self.root = Builder.load_file('convertkmtom.kv')
        return self.root
    def handle_calculate(self, value):
        result = value ** 2
        self.root.ids.output_label.text = str(result)
convert().run()