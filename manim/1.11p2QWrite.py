from manim import *


class Quick2(Scene):
    def construct(self):
        a = MathTex("H_{\\text{billiard}} = \\frac{p^2}{2}+V(x)")
        b = MathTex("V(x) =")
        c = MathTex(r"H(J_1,J_2,\triangle_z) &= J_1 \sum_i (\sigma_i^x\sigma_{i+1}^x + \sigma_i^y\sigma_{i+1}^y + \Delta_z \sigma_i^z\sigma_{i+1}^z) + J_2 \sum_i (\sigma_i^x\sigma_{i+2}^x + \sigma_i^y\sigma_{i+2}^y + \Delta_z \sigma_i^z\sigma_{i+2}^z).\\%&=  J \sum_i \vec{S}_i \cdot \vec{S}_{i+1} + J_2 \sum_i \vec{S}_i \cdot \vec{S}_{i+2}\\&= \text{nearest-neighbour interactions} + \text{next-nearest neighbour interactions}")
        c.scale(0.5)
        self.wait(1)
        self.play(Write(a))
        self.wait(1)
        self.play(FadeOut(a))
        self.wait(1)
        self.play(Write(b))
        self.wait(1)
        self.play(FadeOut(b))
        self.wait(1)
        self.play(Write(c))
        self.wait(1)
        self.play(FadeOut(c))
        self.wait(1)