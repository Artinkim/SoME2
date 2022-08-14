from manim import *
import numpy as np
import matplotlib.pyplot as plt

def CreateWave():
    axes = Axes().scale(0.1)
    shift = np.random.rand(3)*2*PI
    axes.add(axes.plot(lambda x: np.sin(x+shift[0])+np.sin(x+shift[1])+np.sin(x+shift[2])).set_color(BLUE))
    return axes

    
class Intro1(Scene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(1)
            
    def construct(self):
        entry_matrix = MobjectMatrix([
            [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1P}")],
            [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2P}")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NP}")]], h_buff = 1.6)
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
        schrodinger_equation6 = VGroup(entry_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation7 = VGroup(entry_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("(\\lambda_{1}, \\lambda_{2}, \\ldots)"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation8 = VGroup(MathTex("H = "),unkown_matrix).arrange(RIGHT,buff=0.05).to_edge(LEFT,buff=1).shift(DOWN)
        curr_equation = schrodinger_equation1.copy()
        
        eigen_list = MathTex("(\\lambda_{1}, \\lambda_{2}, \\ldots)").next_to(entry_matrix, DOWN)
        
        self.playWait(Write(curr_equation))
        self.playWait(Transform(curr_equation, schrodinger_equation2))
        self.playWait(Transform(curr_equation, schrodinger_equation3))
        self.playWait(Transform(curr_equation, schrodinger_equation1))
        self.playWait(Transform(curr_equation, schrodinger_equation4))
        self.playWait(Transform(curr_equation, schrodinger_equation5))
        self.playWait(Transform(curr_equation, schrodinger_equation6))
        self.playWait(Write(eigen_list))
        self.playWait(Transform(eigen_list,schrodinger_equation7.submobjects[3]),Transform(curr_equation, schrodinger_equation7))
        self.remove(eigen_list)
        self.playWait(Transform(curr_equation, schrodinger_equation1))
        self.play(curr_equation.animate.to_edge(UL,buff=1))
        brace = Brace(unkown_matrix,UP)
        brace_tex = brace.get_text("? X ?")
        self.playWait(ReplacementTransform(curr_equation.copy(), schrodinger_equation8),Create(brace), Write(brace_tex))


# class Intro2(Scene):
#     def playWait(self, *args,**kwargs):
#             self.play(*args,**kwargs)
#             self.wait(1)    
               
#     def construct(self):    
#         max_entropy = MathTex("P(E_i) &= \\frac{e^{-\\beta E_i}}{Z};\>\> Z = \sum_i e^{-\\beta E_i}, \>\>").to_edge(UR,buff=1)
       
       
#         exact_state = MathTex("(x_1,...,x_N ; p_1, ..., p_N)").shift(LEFT*3)
#         weight_factor1 = MathTex("&\\rightarrow P(E) \propto e^{-E(x_1,...x_N; p_1,...,p_N) }").next_to(exact_state,RIGHT)
        
#         phase_state = MathTex("(\sigma_1,...,\sigma_N )").next_to(exact_state,DOWN)
#         weight_factor2 = MathTex("&\\rightarrow P(E) \propto e^{-E(\sigma_1,...,\sigma_N)").next_to(phase_state,RIGHT)
        
#         energy_tex= MathTex("E({x1, ..., xN ; p1, ..., pN })")
#         energy_state = MathTex(r"E &\rightarrow \langle E \rangle = \hspace{-.2cm} \sum_{\text{states of systems}} \hspace{-.2cm}E(\text{state}) P(E(\text{state}))\\ \text{exact energy} &\rightarrow \text{statistical prediction by averaging over states}")
        
        
#         self.playWait(Write(max_entropy))
        
#         self.playWait(Write(exact_state))
#         self.playWait(ReplacementTransform(exact_state.copy(),weight_factor1))
        
#         self.playWait(Write(phase_state))
#         entry_matrix = MobjectMatrix([
#             [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1P}")],
#             [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2P}")],
#             [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
#             [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NP}")]], h_buff = 1.6)
#         unkown_matrix = MobjectMatrix([
#             [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
#             [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
#             [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
#             [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")]], h_buff = 1.6)
#         self.playWait(ReplacementTransform(unkown_matrix,RANDOM MATRIX))
        
#         self.playWait(
#             Write(energy_tex),
#             FadeOut(exact_state,weight_factor1,phase_state,weight_factor2,max_entropy)
#         )
#         self.playWait(ReplacementTransform(energy_tex,energy_state))
        
#         hamiltonian_weight = MathTex(r"H & \rightarrow P(M) \propto e^{-\frac{N}{2} Tr(HH^{\dagger})} \\ \text{exact system} & \rightarrow \text{weight factor for each system}\notag\\")
#         self.playWait(Write(hamiltonian_weight))
        
#         self.playWait(ReplacementTransform())
#         example1 = MathTex("x10 = 0.310231").next_to(energy_state,DOWN,buff=1).shift(LEFT)
#         example2 = MathTex("s = 1.2").next_to(example1,RIGHT,buff=1)
#         self.playWait(Write(example1))
#         self.playWait(Write(example2))
        
#         tex_final = MathTex(r"(x_1,...,x_N) & \rightarrow \langle x_1\rangle, \>\> \langle x_1-x_2\rangle, ... \> \langle f(x_1,..,x_N)\rangle \\\text{exact spectrum} & \rightarrow \text{statistical properties of spectrum}\notag\\ \text{requires: knowing $\&$ diagonalizing $H$} & \rightarrow \>\> \rho(x), P(s)")
#         tex_final.scale(0.75).shift(LEFT*1.5)
#         self.playWait(FadeOut(energy_state,example1,example2))
#         self.playWait(Write(tex_final))
        
        
        
#         # self.playWait(Write(hamiltonian_weight))
        
        
        
        
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