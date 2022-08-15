from manim import *
import numpy as np
from utils import ChangingMatrix

class RMT(Scene):
    def construct(self):
        np.random.seed(1)

        size = (5, 5)
        bounds = (-10, 10)
        iterations = 100
        original_vals = np.round(np.random.uniform(*bounds,size=(iterations,*size)), decimals=2)
        symMat = DecimalMatrix(np.tril(original_vals[0].T) + np.triu(original_vals[0], 1)).scale(0.5)
        self.playwait(FadeIn(symMat))
        
        array1 = np.random.uniform(*bounds,size=size)
        array2 = np.random.uniform(*bounds,size=size)
        array1 = np.tril(array1.T) + np.triu(array1, 1)
        array2 = np.tril(array2.T,-1) + np.triu(array2*-1, 1)
        symetric_conj = [[str(int(array1[x][y]))+("+"*(int(array2[x][y])>=0)+str(int(array2[x][y]))+"i")*(x!=y) for y in range(size[1])] for x in range(size[0])]
        compSymMat = Matrix(symetric_conj, h_buff = 2.6).scale(0.5)
        self.playwait(ReplacementTransform(symMat, compSymMat))

        mTex = MathTex("M = ").next_to(compSymMat, direction=LEFT)
        pTex = MathTex("P(M)= ", "?").next_to(compSymMat, direction=DOWN)
        self.playwait(Write(mTex), Write(pTex))

        self.playwait(FadeOut(mTex, compSymMat, shift=LEFT*5), pTex.animate.move_to(ORIGIN).scale(2))
        self.playwait(Wiggle(pTex[1], scale_value=1.5, rotation_angle=0.02*TAU))

        # t = ValueTracker(0)
        # axes = Axes(x_range=[-5, 5], y_range=[-5, 5], x_length=8, y_length=8)
        # wave = ParametricFunction(lambda x: (x, np.sin(x), 0), color=BLUE, t_range=[-15, 25])
        # dot = Dot()
        # self.play(FadeOut(pTex), FadeIn(wave, dot))
        # self.play(MoveAlongPath(dot, wave, rate_func=linear), wave.animate(rate_func=linear).shift(LEFT*15))

        self.playwait(FadeOut(pTex))

        gauMat = MobjectMatrix([[MathTex("\\text{Gaussian} (\mu,\sigma^{2})") for y in range(size[1])] for x in range(size[0])], h_buff = 3.8).scale(0.5)
        self.playwait(FadeIn(gauMat))
        self.playwait(FadeOut(gauMat))

        t = ValueTracker(0)
        iidMat = MobjectMatrix([[DecimalNumber(original_vals[0][x][y]) for x in range(size[1])] for y in range(size[0])], h_buff=2).move_to(LEFT*3).scale(0.5)
        iidCoord = (1, 1)
        iidMat.get_entries()[iidCoord[0]*size[0]+iidCoord[1]].add_updater(lambda d: d.set_value(original_vals[int(t.get_value())][iidCoord[0]][iidCoord[1]]))
        iidTitle = Tex("Iid entries").next_to(iidMat, direction=UP)
        iidTex = Tex("Unphysical but calculable").next_to(iidMat, direction=DOWN)

        physMat = ChangingMatrix(original_vals, t).move_to(RIGHT*3).scale(0.5)
        physTitle = Tex("Non-iid entries").next_to(physMat, direction=UP)
        physTex = Tex("Physical but incalculable").next_to(physMat, direction=DOWN)

        
        self.playwait(FadeIn(iidMat, iidTitle, iidTex, physMat, physTitle, physTex))

        iidRect = SurroundingRectangle(iidMat.get_entries()[iidCoord[0]*size[0]+iidCoord[1]])
        physRect = SurroundingRectangle(VGroup(*physMat.get_entries()))
        self.play(Create(iidRect), Create(physRect))
        self.play(t.animate.set_value(iterations-1), run_time=5)
        self.playwait(FadeOut(iidMat, iidTitle, iidTex, physMat, physTitle, physTex, iidRect, physRect))
        
        
        gauTex = Tex("Gaussian", "!").scale(2).shift(UP)
        traceTex = Tex("Tr($M^2$), Tr($M^3$), Tr($M^4$), ...?").next_to(gauTex, direction=DOWN*2)
        detTex = Tex("det($M$)?").next_to(traceTex, direction=DOWN)
        self.playwait(Write(gauTex[0]), Write(traceTex), Write(detTex), lag_ratio=0.3, run_time=1)

        self.playwait(Unwrite(traceTex), Unwrite(detTex), Indicate(gauTex, scale_factor=3, color=YELLOW), run_time=1)

    def playwait(self, *args, **kwargs):
        self.play(*args, **kwargs)
        self.wait()