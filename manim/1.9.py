from manim import *
import numpy as np

class Pain(Scene):
    def construct(self):

        eq = [""]*113
        # eq1.26:    H&= \begin{pmatrix} H_{11} & H_{12}\\H_{21} & H_{22} \end{pmatrix}
        eq.extend(r"q(s) &= P(t>s), q(s+ds) &= q(ds|s), q(s+ds) &= q(s) q(ds), q(s+ds) &= q(s)[1- c\times ds], \frac{q(s+ds)-q(s)}{ds} &\equiv \frac{dq(s)}{ds}= - c q(s), q(s) = e^{-cs}, P(s) &= - \frac{dq(s)}{ds} = c e^{-cs}, q(s+ds) &= q(ds|s), q(s+ds) &= q(s) q_s(ds), q(s+ds) &= q(s) q_s(ds) = q(s) [1- c\times s \times ds], \frac{q(s+ds) - q(s)}{ds} &\equiv \frac{dq(s)}{ds} =   - c\times s\times  q(s), q(s) &= - c e^{-cs^2/2}, P(s) &= - \frac{dq(s)}{ds} \propto s e^{-cs^2/2}, H&= \begin{pmatrix} H_{11} & H_{12}\\H_{12} & H_{22} \end{pmatrix}, &(\lambda-H_{11})(\lambda-H_{22}) - H_{12}^2 = 0, \lambda_{\pm} &= \frac{H_{11} +H_{22}}{2} \pm \frac{1}{2}\sqrt{(H_{11}-H_{22})^2 + 4H_{12}^2}, s&\equiv \lambda_+ - \lambda_- = \sqrt{(H_{11}-H_{22})^2 + 4H_{12}^2}, P(s) &\propto \int dH_{11} dH_{22} dH_{12} \delta(s-\sqrt{(H_{11}-H_{22})^2 + 4 H_{12}^2}) P(H_{11}) P(H_{22}) P(H_{12}), &\propto \int dH_{11} dH_{22} dH_{12} \delta(s-\sqrt{(H_{11}-H_{22})^2 + 4 H_{12}^2}) e^{-\frac{1}{2}(H_{11}^2 +H_{22}^2 + 2H_{12}^2)}, P(s) &\propto \int du dv dw \delta(s-\sqrt{u^2 + w^2}) e^{-(u^2+v^2+w^2)}, P(s) &\propto \int du dw \delta(s-2\sqrt{u^2 + w^2}) e^{-(u^2+w^2)}, P(s) &\propto \int_0^\infty r dr \int_0^{2\pi} d\theta \delta(s-2r) e^{-r^2}, P(s) \propto s e^{-s^2}, P(M_{11},M_{12},...,M_{NN}) \rightarrow P(x_1,x_2,...,x_N)".split(", ")
            )
        eq.extend(r"M &\rightarrow U \Lambda U^{\dagger}, e^{-\frac{N}{2} Tr(MM^{\dagger})} &\rightarrow e^{-\frac{N}{2} \sum_i x_i^2} \times J^{-1}\bigg(\frac{\partial M_{ij}}{\partial x_i \partial u_{ij}}\bigg), P(M_{11},M_{12},...,M_{NN}) \rightarrow P(x_1,x_2,...,x_N), e^{-\frac{N}{2} Tr(MM^{\dagger})} \rightarrow e^{-\frac{N}{2} \sum_i x_i^2 + \log\big( J^{-1} (\{x_i\})\big)}, \int \prod_{i=1}^N dx_i e^{-\frac{N}{2} \sum_i V(x_i) + \log\big( J^{-1} (\{x_i\})\big)} \equiv     \int \prod_{i=1}^N dx_i e^{- N S(\{x_i\}]} \approx e^{-N S(\{x_i^*\})} \times \text{corrections}, \frac{\partial S(\{x_i\})}{\partial x_i} &=0 \>\> \text{determines} \>\>\{x_i^*\}, e^{-\frac{N}{2} Tr(MM^{\dagger})} \rightarrow e^{-\frac{N}{2} \sum_i x_i^2 + \log\big( J^{-1} (\{x_i\})\big)}, P_{Poisson}(s) &\propto e^{-s}, P_{WD}(s) &\propto se^{-s^2}, \lim_{s\rightarrow 0} P_{Poisson}(s) &= 1, \lim_{s\rightarrow 0} P_{WD}(s) &= 0".split(", ")
        )

        # eqTex = [MathTex(eq[0])]
        # for i in range(len(eq)):
        #     s = eq[i]
        #     eqTex.append(MathTex(s))
        #     if len(s) > 0:
        #         print("eq " + str(i) + ": " + s+"\n")
        #         self.play(FadeOut(eqTex[i-1]), FadeIn(eqTex[i]))

        
        eqTex = [MathTex(eq[i]) for i in range(len(eq))]
        # for i in range(1, len(eqTex)):
        #     self.play(FadeOut(eqTex[i-1]), FadeIn(eqTex[i]))


        mainPoints = [MathTex("\\text{Independent} \lambda"), MathTex("\\text{Dependent} \lambda"), MathTex("\\text{2x2}"), MathTex("\\text{NxN}")]
        VGroup(*mainPoints).arrange_in_grid(rows=4, cols=1, buff=MED_LARGE_BUFF)
        for i in range(len(mainPoints)):
            self.play(Write(mainPoints[i]))
        self.wait(1)

        distTex = MathTex("Distribution = ", "?")
        self.play(FadeOut(*mainPoints, scale=0.5), Write(distTex))
        self.playwait(Wiggle(distTex[1], scale_value=1.5, rotate_angle=0.02*TAU))
        self.playwait(Unwrite(distTex))

        self.playEq(eqTex, 113, 119)
        
        distTex = MathTex("Distribution = ", "Exponential")
        self.play(Write(distTex))
        self.playwait(Wiggle(distTex[1], scale_value=1.2, rotate_angle=0.02*TAU))
        self.playwait(Unwrite(distTex))

        self.playEq(eqTex, 120, 125)
        
        distTex = MathTex("Distribution = ", "Gaussian \\times Linear")
        self.play(Write(distTex))
        self.playwait(Wiggle(distTex[1], scale_value=1.2, rotate_angle=0.02*TAU))
        self.playwait(Unwrite(distTex))



        self.playEq(eqTex, 126, 129)

        t = ValueTracker(0)
        axes = NumberPlane()
        nums = [DecimalNumber(-4).add_updater(lambda d: d.set_value(-4-t.get_value()*1)), DecimalNumber(-3).add_updater(lambda d: d.set_value(-3-t.get_value()*-3)), DecimalNumber(-2).add_updater(lambda d: d.set_value(-2-t.get_value()*3))]
        m = MobjectMatrix([[nums[0], nums[1]], [nums[1].copy(), nums[2]]]).to_corner(corner=UP+LEFT)
        mTex = MathTex(r"s = \sqrt{(H_{11}-H_{22})^2 + 4H_{12}^2}").next_to(m)
        arrow = Arrow().add_updater(lambda a: a.put_start_and_end_on(ORIGIN, [nums[0].get_value()-nums[2].get_value(), nums[1].get_value(), 0]))
        dist = DecimalNumber().add_updater(lambda a: a.set_value(np.round(np.sqrt(np.square(nums[0].get_value()-nums[2].get_value())+4*np.square(nums[1].get_value())), decimals=2)).next_to(arrow.get_center()))
        arTex = MathTex("(H_{11}-H_{22}, H_{12})").add_updater(lambda a: a.next_to(arrow.get_end(), direction=LEFT).shift(DOWN*0.7))

        self.playwait(FadeIn(axes, m, arrow, distTex, arTex, mTex, dist))
        self.playwait(t.animate.set_value(1-0.000001), run_time=1)
        self.playwait(FadeOut(axes, m, arrow, distTex, arTex, mTex, dist))
        
        abeTex = Tex("Abe eq 1.30-1.35")
        self.add(abeTex)
        self.wait(2)
        self.remove(abeTex)
        self.wait(1)

        
        twoTex = Tex("2 $\lambda$ = 1 space")
        nTex = Tex("N $\lambda$ = N-1 spaces")
        self.playwait(FadeIn(twoTex))
        self.playwait(Transform(twoTex, nTex))
        self.playwait(FadeOut(twoTex))

        polyTex = [MathTex("c_0 + c_1x + c_2x^2"), MathTex("c_0 + c_1x + c_2x^2 + c_3x^3"), MathTex("c_0 + c_1x + c_2x^2 + c_3x^3 + c_4x^4 + c_5x^5 + ...")]
        self.playwait(FadeIn(polyTex[0]))
        self.playwait(TransformMatchingShapes(polyTex[0], polyTex[1]))
        self.playwait(TransformMatchingShapes(polyTex[1], polyTex[2]))
        self.playwait(FadeOut(polyTex[2]))

        self.playEq(eqTex, 136, 140)
        
        abeTex = Tex("Figure 1.1 (picture)")
        self.add(abeTex)
        self.wait(2)
        self.remove(abeTex)
        self.wait(1)

        self.playEq(eqTex, 141, 143)

        matrix = np.round(np.random.rand(5, 5), decimals=2)
        m = Matrix(matrix)
        det = MathTex("\det(M)=", str(np.round(np.linalg.det(matrix), decimals=2))).next_to(m, direction=DOWN*2)
        self.playwait(FadeIn(m, det))

        matrix2 = matrix.copy()
        for i in range(5):
            matrix2[2][i] = matrix2[0][i]
        m2 = Matrix(matrix2)
        det2 = MathTex("\det(M)=", str(np.linalg.det(matrix2))).next_to(m2, direction=DOWN*2)
        self.playwait(TransformMatchingShapes(m, m2), TransformMatchingTex(det, det2))

        self.playwait(FadeOut(m2, det2))

        abeTex = Tex("Abe eq 1.44-1.47")
        self.add(abeTex)
        self.wait(2)
        self.remove(abeTex)
        self.wait(1)

    def playwait(self, *args, **kwargs):
        self.play(*args, **kwargs)
        self.wait()
    
    def playEq(self, eqTex, start, end):
        if start == 141:
            eqTex[start].scale(0.5)
        self.playwait(FadeIn(eqTex[start]))
        for i in range(start, end):
            self.playwait(ReplacementTransform(eqTex[i], eqTex[i+1]))
        self.playwait(FadeOut(eqTex[end]))