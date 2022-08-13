from manim import *
import mpmath

class RiemannZeta(Scene):
    ANIMATIONTYPE = 0

    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        if self.ANIMATIONTYPE == 0:
            self.play(Create(ParametricFunction(lambda x: plane.n2p(mpmath.zeta(0.5+1j*x)), t_range=[0, 100])), run_time=15)
        elif self.ANIMATIONTYPE == 1:
            planes = [ComplexPlane(x_range=[0.5, 3, 0.1], y_range=[-4, 4, 0.1]), ComplexPlane(x_range=[0.5, 7, 0.1], y_range=[-2, 2, 0.1]), ComplexPlane(x_range=[0.5, 7, 0.5], y_range=[-4, 4, 0.5])]
            for p in planes:
                p.shift(RIGHT*((p.x_range[1]-p.x_range[0])/2+0.5))
            def f(x):
                # print(x, mpmath.zeta(x))
                return mpmath.zeta(x)
            self.play(*[ApplyComplexFunction(function=f, mobject=planes[i]) for i in range(len(planes))], run_time=10)
        self.wait(5)
        