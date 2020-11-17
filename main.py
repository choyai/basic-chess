from kivy.app import App
from kivy.uix.widget import Widget

from color_util import get_normalized_color

class ChessGame(Widget):
    pass

class ChessApp(App):
    def build(self):
        return ChessGame()

if __name__ == '__main__':
    ChessApp().run()