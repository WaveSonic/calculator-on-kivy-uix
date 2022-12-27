from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.widget import Widget

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class MyApp(App):
    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ""
        self.formula += instance.text
        self.label.text = self.formula

    def add_operator(self, instance):
        self.formula += instance.text
        self.label.text = self.formula

    def equel(self, instance):
        try:
            self.label.text = str(eval(self.formula))
            self.formula = self.label.text
        except:
            self.label.text = 'Error'
            self.formula = '0'

    def delete(self, instance):
        self.formula = '0'
        self.label.text = '0'


    def build(self):
        self.formula = '0'
        self.label = Label(text=self.formula, size_hint=(1, .4), font_size=40, halign='right', valign='center', text_size=(400-50, 500*.4-50))
        al = BoxLayout(orientation='vertical', padding=25)
        al.add_widget(self.label)
        gl = GridLayout(cols=4, spacing=5, size_hint=(1, .6))

        gl.add_widget(Button(text='CC', on_press=self.delete))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='/', on_press=self.add_operator))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operator))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operator))

        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.equel))
        gl.add_widget(Button(text='+', on_press=self.add_operator))
        al.add_widget(gl)

        return al



if __name__ == '__main__':
    MyApp().run()
