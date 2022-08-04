from manim import *

class Transformations(Scene):
    def construct(self):
        a = MathTex("f(M) = f(U^\dagger M U)") #1.1 
        b = MathTex("\langle\\text{Tr}(M^2)\\rangle_\\text{Gaussian} = \left(\\frac{N-1}{N} + 2\\right)\sigma^2") #1.2
        c = MathTex("\\sigma^2_{ij} \\equiv var(M_{ij}) = c^2/N") #1.3
        d = MathTex("Z&= \int dM e^{-\\frac{N}{2} \\text{Tr}(MM^{\dagger})}") #1.4
        e = MathTex("P(M) \propto \prod_{i=1}^N f_i(M_{ii}) \prod_{i<j}^N f_{ij}(M_{ij})") #1.5
        f = MathTex("P(M) = P(UMU^{\dagger})") #1.6
        g = MathTex("Z&= \int \>e^{-\\frac{(x^2+y^2)}{2}} dx \>dy") # 1.7
        h = MathTex()
        group1 = VGroup(d,a,b,c).arrange(DOWN, buff=0.8)
        group2 = VGroup(d,e,g).arrange(DOWN, buff=0.8)

        self.play(Create(d),run_time=2)
        self.play(Create(a),run_time=2)
        self.play(Create(b),run_time=2)
        self.play(Create(c),run_time=2)
        self.play(Uncreate(a),Uncreate(b),Uncreate(c),run_time=2)
        self.play(Create(e),run_time=2)
        self.play(TransformMatchingShapes(e,f),run_time=2)
        # self.play(TransformMatchingShapes(f.copy(),g),run_time=2)
        self.play(Create(g),run_time=2)
        self.wait(1)
