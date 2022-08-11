from manim import *
import numpy as np
import matplotlib.pyplot as plt

def CreateWave():
    axes = Axes().scale(0.1)
    shift = np.random.rand(3)*2*PI
    axes.add(axes.plot(lambda x: np.sin(x+shift[0])+np.sin(x+shift[1])+np.sin(x+shift[2])).set_color(BLUE))
    return axes

    
class Intro(Scene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(1)
            
    def construct(self):
        unkown_matrix = MobjectMatrix([
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")]], h_buff = 1.6)
        waves1 = VGroup(*[CreateWave() for _ in range(7)]).arrange(DOWN)
        waves2 = VGroup(*[CreateWave() for _ in range(7)]).arrange(DOWN)
        schrodinger_equation1 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation2 = VGroup(MathTex("H"), MathTex("\psi_n").scale(2).set_color(BLUE), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n").scale(2).set_color(BLUE)).arrange(RIGHT,buff=0.05)
        schrodinger_equation3 = VGroup(MathTex("H"), waves1, MathTex(" &= "), MathTex("E_n"),waves2).arrange(RIGHT,buff=0.05)
        schrodinger_equation4 = VGroup(MathTex("H").scale(2).set_color(RED), MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation5 = VGroup(MathTex("H").scale(2).set_color(RED), MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n").scale(2).set_color(YELLOW), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation6 = VGroup(unkown_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        curr_equation = schrodinger_equation1.copy()
        
        
        self.playWait(Write(curr_equation))
        self.playWait(Transform(curr_equation, schrodinger_equation2))
        self.playWait(Transform(curr_equation, schrodinger_equation3))
        self.playWait(Transform(curr_equation, schrodinger_equation1))
        self.playWait(Transform(curr_equation, schrodinger_equation4))
        self.playWait(Transform(curr_equation, schrodinger_equation5))
        self.playWait(Transform(curr_equation, schrodinger_equation6))
        brace = Brace(unkown_matrix,UP)
        brace_tex = brace.get_text("? X ?")
        self.playWait(Create(brace), Write(brace_tex))
        
        
        
        # def Hpm1(N):
        #     h = np.random.randint(0, 2,size=(N,N))
        #     h[h==0]=-1
        #     h = np.tril(h.T) + np.triu(h, 1)
        #     return h
        
        # N=500
        # niter
        # evals = np.zeros((niter,N))
        # delta = np.zeros((niter,N-1))
        # matricies = np.zeros((niter,N,N))
        # histograms = np.zeros((niter,100))
        # for n in range(niter):
        #     h=Hpm1(N)
        #     matricies[n]=h
        #     evals[n,:]=np.linalg.eigvalsh(h)
        #     delta[n,:] = evals[n,1:]-evals[n,:-1]
        #     histograms[n,:] = np.histogram(delta,bins=np.linspace(0.0, 1,101),density=True)[0]


        # chart = BarChart(values=histograms[-1])
        # decimal = Integer(0)
        # t = ValueTracker(0)
        
        # chart.add_updater(lambda c: c.change_bar_values(histograms[int(t.get_value())]))
        # decimal.add_updater(lambda x: x.set_value(t.get_value()+1))

        # self.add(chart,decimal)
        # self.play(t.animate(rate_func=smooth).set_value(niter-1),run_time=5)
        # self.wait(1)