from manim import  VMobject, Text, BLACK, RIGHT, DOWN, Line, UP
from CustomStealthTip import CustomStealthTip
from ..utils.constants import *

class CustomText(VMobject):
    def __init__(self, text, color=BLACK, isVector=False, font=Gost_AU_Font, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.main_text = Text(text, color=color, font=font)
        self.isVector = isVector
        self.index = None
        self.arrow = None
        self.add(self.main_text)

        if self.isVector:
            self.add_arrow()

    def add_index(self, index_text, font=Gost_BU_Font):
        self.index = Text(index_text, color=self.color, font=font).scale(0.58)
        self.index.next_to(self.main_text, RIGHT, buff=0.05)
        self.index.align_to(self.main_text, DOWN)
        self.add(self.index)
        return self

    def add_arrow(self):
        arrow_length = self.main_text.width + 0.2  # немного больше длины текста
        self.arrow = Line(
            start=self.main_text.get_top() + UP * 0.08 - RIGHT * arrow_length * 0.2,
            end=self.main_text.get_top() + UP * 0.08 + RIGHT * arrow_length * 0.6,
            buff=0,
            color=self.color,
            stroke_width=2
        )
        
        tip = CustomStealthTip(color=self.color)
        self.arrow.add_tip(tip)
        self.add(self.arrow)
