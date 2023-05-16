import kivy
from kivy.app import App
from view.GerenciaTelas import GerenciaTelas

kivy.require('1.11.1')

__version__ = "0.1"


class crud(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root


if __name__ == '__main__':
    crud().run()
