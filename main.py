from kivy.app import App
from kivy.uix.widget import Widget

from color_util import get_normalized_color
from Chessboard import Chessboard, Color, Square

class ChessGame(Widget):

    def on_touch_down(self, touch):
        return

class ChessApp(App):
    def build(self):
        game = ChessGame()

        return game

if __name__ == '__main__':
    ChessApp().run()