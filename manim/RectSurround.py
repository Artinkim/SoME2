from manim import *

class Rect(Scene):
    def construct(self):
        self.wait(0.5)
        tex = Tex("H").scale(3)
        r = SurroundingRectangle(tex)
        self.play(Create(r))
        self.wait(1)
        self.play(FadeOut(r))