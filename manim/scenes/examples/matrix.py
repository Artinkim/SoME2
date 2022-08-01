from manim import *

class MatrixTransformations(Scene):
    def construct(self):
        a = MathTex("H_{11}")
        b = MathTex("H_{12}")
        c = MathTex("H_{21}")
        d = MathTex("H_{22}")
        e = MathTex("H = ").shift(LEFT).shift(LEFT)
        g = MathTex("(\\lambda-", "H_{11}",")(\\lambda-","H_{22}", ")-", "{","H_{12}","}^2= 0")
        #h = MathTex("\lambda_{\pm} = \\frac{","H_{11}", "+", "H_{22}","}{2} \pm \sqrt{(\\frac{", "H_{11}", "-", "H_{22}","}{2})^2 +", "H_{12}","^2}")
        h = MathTex("\lambda_{\pm} = { ","H_{11}","+", "H_{22}", "\\over ","2}", " \pm \sqrt{({    ","H_{11}","-","H_{22}","\\over {2}})^2 +","{","H_{12}","}^2}")
        print(h.submobjects)
        m0 = MobjectMatrix([[a, b], [c, d]])
        group = VGroup(a,b,c,d).copy()
        # self.add(h)
        # self.wait(1)
        self.add(e,m0)
        self.wait(1)
        self.play(TransformMatchingShapes(m0,group),Uncreate(e))
        self.play(TransformMatchingTex(group,g))
        self.wait(1)
        self.play(TransformMatchingTex(g,h))
        self.wait(1)