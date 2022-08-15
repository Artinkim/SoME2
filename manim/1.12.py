from manim import *
import mpmath
import numpy as np

class RiemannZeta(Scene):
    
    def construct(self):
        np.random.seed(1)
        
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        
        funcTex = MathTex("\\zeta(z)").to_corner(corner=LEFT+UP).shift(DOWN*0.5)
        funcRight = MathTex(r"\cong \sum_{n=1}^{\infty}\frac{1}{n^z}").next_to(funcTex)
        
        self.playwait(Write(funcTex), Write(funcRight))
        self.playwait(Wiggle(funcTex))
        
        locations = [(0, 0), *np.random.randint(low= -4, high= 5, size=(3, 2)), (0.5, 2)]
        a, b = ValueTracker(locations[0][0]), ValueTracker(locations[0][1])
        inputDot = Dot(plane.n2p(a.get_value()+1j*b.get_value()), color=RED).add_updater(lambda m: m.move_to(plane.n2p(a.get_value()+1j*b.get_value())))
        outputDot = Dot(plane.n2p(a.get_value()+1j*b.get_value()), color=BLUE).add_updater(lambda m: m.move_to(plane.n2p(mpmath.zeta(a.get_value()+1j*b.get_value()))))
        funcArrow = Arrow(start=inputDot.get_center(), end=outputDot.get_center()).add_updater(lambda m: m.put_start_and_end_on(inputDot.get_center(), outputDot.get_center()))
        
        
        self.add(inputDot, outputDot, funcArrow)
        self.playwait(outputDot.animate.move_to(plane.n2p(mpmath.zeta(a.get_value()+1j*b.get_value()))))
        
        for i in range(1, len(locations)-1):
            self.play(a.animate.set_value(locations[i][0]-0.00001), b.animate.set_value(locations[i][1]-0.00001))
        self.playwait(FadeOut(inputDot, outputDot, funcArrow))
        
        x1 = DashedLine(config.top, config.bottom, dash_length=0.2).shift(plane.n2p(1))
        rhs1 = Rectangle(height=config.frame_height, width=config.frame_width, stroke_width=0, fill_color=BLUE, fill_opacity=0.5).next_to(x1, buff=0)
        func1 = MathTex(r"=\frac{1}{1^z}+\frac{1}{2^z}+\frac{1}{3^z}+...").next_to(funcRight)
        self.play(FadeIn(x1, rhs1))
        self.playwait(Write(func1))
        
        lhs1 = Rectangle(height=config.frame_height, width=config.frame_width, stroke_width=0, fill_color=RED, fill_opacity=0.5).next_to(x1, buff=0, direction=LEFT)
        func2 = Tex(r"= Divergent").next_to(funcRight)
        self.playwait(FadeIn(lhs1), FadeOut(rhs1), FadeOut(func1))
        self.playwait(Write(func2))
        

        eq159 = MathTex(r"\zeta(z) =", r"\prod_{\text{primes } p} \left(\sum_{k = 0}^{\infty} \frac{1}{p^k}\right)")
        self.playwait(FadeOut(lhs1, x1, func2, plane, funcRight, scale=0.5), TransformMatchingTex(funcTex, eq159))
        # return
        
        self.playwait(FadeOut(eq159), FadeIn(plane, scale=1.5))
        
        dots = [Dot([-2*i-2, 0, 0]) for i in range(3)]
        self.playwait(FadeIn(*dots, scale=0.5))

        stripRect = Rectangle(height=config.frame_height, width=plane.n2p(1)[0], stroke_width=0, fill_color=BLUE, fill_opacity=0.5).next_to(x1, buff=0, direction=LEFT)
        self.playwait(FadeOut(*dots, scale=1.5), FadeIn(stripRect))

        x5 = Line(config.top, config.bottom).shift(plane.n2p(0.5)).set_color(RED)
        self.playwait(FadeIn(x5), FadeOut(stripRect))

        rzFunc = ParametricFunction(lambda x: plane.n2p(mpmath.zeta(0.5+1j*x)), t_range=[0, 100]).set_color([PINK,YELLOW])
        self.play(FadeOut(x5))
        self.playwait(Create(rzFunc), run_time=15)

        self.play(FadeOut(rzFunc), FadeIn(x5))
        self.playwait(Wiggle(x5))
        
        self.playwait(FadeOut(plane, x5))

        # self.add(Tex("Fade in chart 2 from 1.9cars.py\n along with Figure 3 from 1_12 in slack"))

        self.wait(5)
        
    def playwait(self, *args, **kwargs):
        self.play(*args, **kwargs)
        self.wait()