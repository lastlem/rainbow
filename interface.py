from abc import ABC, abstractmethod
from tkinter import Label, Entry


class App(ABC):
    @abstractmethod
    def __init__(self, path: str):
        """
        Creates window with given information

        :param path: path to json file which describes interface
        """
        raise NotImplementedError()


class Color(ABC):
    @abstractmethod
    def __init__(self, color):
        """
        Creates color and its code

        :param color: any color
        """

    @property
    @abstractmethod
    def color_name(self) -> str:
        """

        :return: Color name
        """

    @property
    @abstractmethod
    def color_code(self) -> str:
        """
        Color code is in 16 bit.
        Example: Red -> #FF0000

        :return: Color code
        """


class Board(ABC):
    @abstractmethod
    def __init__(self):
        """
        Creates Board with Label and Entry, which shows color
        """

    @property
    @abstractmethod
    def label(self) -> Label:
        """
        Labels which shows color name

        :return: class label
        """

    @property
    @abstractmethod
    def entry(self) -> Entry:
        """
        Entry which shows color code

        :return: class Entry
        """


class ColorButton(ABC):
    @abstractmethod
    def __init__(self, text: str, color: Color, board: Board):
        """
        Creates button with given color, which changes colors of the label and entry in the board

        :param text: text on the button
        :param color: class Color
        :param board: class Board
        """
