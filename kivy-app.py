from kivy.app import App
from kivy.lang import Builder

# Design of the app
kv = '''
FloatLayout:
    Button:
        text: 'Hello World!'
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.5,}
        canvas.before: 
            PushMatrix
            Rotate: 
                angle: 45
                origin: self.center
        canvas.after:
            PopMatrix
'''

# Build app
class SuperApp(App):
    def build(self):
        return Builder.load_string(kv)

SuperApp().run()


