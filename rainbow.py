from interface import ColorButton as _ColorButton
from interface import Board as _Board
from interface import App as _App
from interface import Color as _Color
from tkinter import Tk, Label, Button, Entry, CENTER, X, END
import json


class App(_App):
    def __init__(self, path: str):
        root = Tk()
        root.title('Colors')

        self.__path = path
        self.__create_widgets()

        root.mainloop()

    def __create_widgets(self) -> None:
        with open(self.__path) as f:
            data_widget = json.load(f)

        board = None
        for element in data_widget:
            if element['widget'].capitalize() == 'Board':
                board = Board()
            elif element['widget'].capitalize() == 'Colorbutton':
                ColorButton(element['text'], Color(element['color']), board)


class Color(_Color):
    # todo: make color list, and check codes for # and that it is 16 bit
    color_codes = {"Red": "#ff0000", "Orange": "#ff7d00", "Yellow": "#ffff00", "Green": "#00ff00",
                   "Light blue": "#007dff", "Blue": "#0000ff", "Purple": "#7d00ff"}

    def __init__(self, color: str):
        self.__check_color(color)
        self.color = color.capitalize()
        self.code = self.color_codes[self.color]

    def __check_color(self, color: str) -> None:
        if color.capitalize() not in self.color_codes:
            raise ValueError(f'Color should be in {self.color_codes.keys()}. Got: {color}')


class Board(_Board):
    def __init__(self):
        self.label = Label(text='Color name', font=('System', 20))
        self.entry = Entry(justify=CENTER, font=('System', 20))
        self.entry.insert(0, 'Color code')
        self.label.pack()
        self.entry.pack()


class ColorButton(_ColorButton):
    def __init__(self, text: str, color: Color, board: Board):
        self.__color = color
        self.__check_board(board)
        self.__label = board.label
        self.__entry = board.entry
        Button(text=text, bg=self.__color.code, command=self.__change_color).pack(fill=X)

    @staticmethod
    def __check_board(board) -> None:
        if not isinstance(board, Board):
            raise TypeError(f'Third argument type should be Board. Got type: {type(board)}')

    def __change_color(self) -> None:
        self.__label['text'] = self.__color.color
        self.__label.config(fg=self.__color.color)

        self.__entry.delete(0, END)
        self.__entry.insert(0, self.__color.code)
        self.__entry.config(bg=self.__color.color)


if __name__ == '__main__':
    App('rainbow.json')
