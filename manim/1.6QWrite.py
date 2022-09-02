from manim import *


class Quick(Scene):
    def construct(self):
        a = MathTex("a+bi").scale(3)
        a1 = Arrow(-2,-1).scale(3).shift(RIGHT*3)
        b = MathTex("RR^T = 1").scale(3)
        c = MathTex("UU^{\dagger} = 1").scale(3)
        self.wait(1)
        self.play(Write(a),Create(a1))
        self.wait(1)
        self.play(FadeOut(a,a1))
        self.wait(1)
        self.play(Write(b))
        self.wait(1)
        self.play(FadeOut(b))
        self.wait(1)
        self.play(Write(c))
        self.wait(1)
        self.play(FadeOut(c))
        self.wait(1)