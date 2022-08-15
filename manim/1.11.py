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
       
        ham_matrix = MobjectMatrix([
            [MathTex("(1 -> 1"), MathTex("(1 -> 2)"), MathTex("(1 -> 3)"), MathTex("...   "), MathTex("(1 -> N)")],
            [MathTex("(2 -> 1)"), MathTex("(2 -> 2)") ,MathTex("(2 -> 3)"), MathTex("...  "), MathTex("(2 -> N)")],
            [MathTex("(3 -> 1)"), MathTex("(3 -> 2)"), MathTex("(3 -> 3)"), MathTex("...  "), MathTex("(3 -> N)")],
            [MathTex(), MathTex(), MathTex(), MathTex("\ddots  "), MathTex()],
            [MathTex("(N -> 1)"), MathTex("(N -> 2)"), MathTex("(N -> 3)"), MathTex("...  "), MathTex("(N -> N)")]
            ], h_buff = 2.5).scale(0.5)
        H_def = VGroup(VGroup(Tex("Encodes probablility to"),Tex("transition from state"),Tex("i $\\rightarrow$ j in a small time $\\Delta$t.")).arrange(DOWN)).next_to(ham_matrix,UP)
        H_def.add(MathTex("H_{ij} \sim").next_to(H_def,LEFT))
        H_letter = MathTex("H")
        waves1 = VGroup(*[CreateWave() for _ in range(7)]).arrange(DOWN)
        waves2 = VGroup(*[CreateWave() for _ in range(7)]).arrange(DOWN)
        schrodinger_equation1 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("\\lambda_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation2 = VGroup(MathTex("H"), MathTex("\psi_n").scale(2).set_color(BLUE), MathTex(" &= "), MathTex("\\lambda_n"), MathTex("\psi_n").scale(2).set_color(BLUE)).arrange(RIGHT,buff=0.05)
        schrodinger_equation3 = VGroup(MathTex("H"), waves1, MathTex(" &= "), MathTex("\\lambda_n"),waves2).arrange(RIGHT,buff=0.05)
        schrodinger_equation4 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("\\lambda_n").scale(2).set_color(ORANGE), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation5 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n").scale(2).set_color(YELLOW), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation6 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("(\\lambda_{1}, \\lambda_{2}, \\ldots)").scale(1.5).set_color(ORANGE), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation7 = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("(E_{1}, E_{2}, \\ldots)").scale(1.5).set_color(YELLOW) , MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        
        schrodinger_equation1E = VGroup(MathTex("H"), MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation8 = VGroup(entry_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation9 = VGroup(unkown_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        
        #schrodinger_equation8 = VGroup(MathTex("H = "),unkown_matrix).arrange(RIGHT,buff=0.05).to_edge(LEFT,buff=1).shift(DOWN)
        curr_equation = schrodinger_equation1.copy()
        
        #eigen_list = MathTex("(\\lambda_{1}, \\lambda_{2}, \\ldots)").next_to(entry_matrix, DOWN)
        
        self.playWait(Write(H_letter))
        self.playWait(Write(H_def),ReplacementTransform(H_letter,ham_matrix))
        self.playWait(FadeOut(H_def),ReplacementTransform(ham_matrix,curr_equation[0]),FadeIn(curr_equation[1:]))
        
        def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(0.2)
            
        self.playWait(Transform(curr_equation, schrodinger_equation2))
        self.playWait(Transform(curr_equation, schrodinger_equation3))
        
        self.playWait(Transform(curr_equation, schrodinger_equation1))
        self.playWait(Transform(curr_equation, schrodinger_equation4))
        self.playWait(Transform(curr_equation, schrodinger_equation5))
        self.playWait(Transform(curr_equation, schrodinger_equation6))
        self.playWait(Transform(curr_equation, schrodinger_equation7))

        self.playWait(Transform(curr_equation, schrodinger_equation1E))
        self.playWait(Transform(curr_equation, schrodinger_equation8))
        self.playWait(Transform(curr_equation, schrodinger_equation9))
        brace = Brace(unkown_matrix,UP)
        brace_tex = brace.get_text("? X ?")
        self.playWait(Create(brace),Write(brace_tex))

class Intro1P2(Scene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs) 
            self.wait(1)
    def construct(self):
        unkown_matrix = MobjectMatrix([
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("?"), MathTex("?"), MathTex("..."), MathTex("?")]], h_buff = 1.6)
        random_matrix = MobjectMatrix([
            [MathTex("2.6"), MathTex("-6.32"), MathTex("..."), MathTex("9.47")],
            [MathTex("-4.71"), MathTex("2.42"), MathTex("..."), MathTex("-1.13")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("6.90"), MathTex("-1.52"), MathTex("..."), MathTex("8.51")]], h_buff = 1.6)
        schrodinger_equation1 = VGroup(unkown_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        schrodinger_equation2 = VGroup(random_matrix, MathTex("\psi_n"), MathTex(" &= "), MathTex("E_n"), MathTex("\psi_n")).arrange(RIGHT,buff=0.05)
        brace = Brace(unkown_matrix,UP)
        brace_tex = brace.get_text("? X ?")
        self.add(schrodinger_equation1,brace,brace_tex)
        self.wait(1)
        self.playWait(Transform(schrodinger_equation1, schrodinger_equation2), FadeOut(brace,brace_tex))
         


class Intro2(Scene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(1)    
               
    def construct(self):    
        max_entropy = MathTex("P(E_i) &= \\frac{e^{-\\beta E_i}}{Z};\>\> Z = \sum_i e^{-\\beta E_i}, \>\>").to_edge(UR,buff=1)
       
       
        exact_state = MathTex("(\\lambda_1,...,\\lambda_N ; p_1, ..., p_N)").shift(LEFT*3)
        weight_factor1 = MathTex(r"\rightarrow P(E) \propto e^{-E(\lambda_1,...\lambda_N; p_1,...,p_N) }").next_to(exact_state,RIGHT)
        exact_state.add(Tex("exact state").next_to(exact_state, DOWN, buff=0.5))
        weight_factor1.add(MathTex(r"\rightarrow \text{weight factor for each state} }").next_to(weight_factor1, DOWN, buff=0.5))
        
        phase_state = MathTex("(\sigma_1,...,\sigma_N )")
        weight_factor2 = MathTex("&\\rightarrow P(E) \propto e^{-E(\sigma_1,...,\sigma_N)").next_to(phase_state,RIGHT)
        
        energy_tex= MathTex("E({\\lambda_1, ..., \\lambda_N ; p_1, ..., p_N })")
        energy_state = MathTex(r"E &\rightarrow \langle E \rangle = \hspace{-.2cm} \sum_{\text{states of systems}} \hspace{-.2cm}E(\text{state}) P(E(\text{state}))\\ \text{exact energy} &\rightarrow \text{statistical prediction by averaging over states}")
        
        
        self.playWait(Write(max_entropy))
        
        self.playWait(Write(exact_state))
        self.playWait(ReplacementTransform(exact_state.copy(),weight_factor1))
        self.playWait(FadeOut(exact_state,weight_factor1))
        
        self.playWait(Write(phase_state))
        self.playWait(ReplacementTransform(phase_state.copy(),weight_factor2))
        self.playWait(FadeOut(phase_state,weight_factor2))
        
        self.playWait(Write(energy_tex))
        self.playWait(ReplacementTransform(energy_tex,energy_state))
        
        hamiltonian_weight = MathTex(r"H & \rightarrow P(M) \propto e^{-\frac{N}{2} Tr(HH^{\dagger})} \\ \text{exact system} & \rightarrow \text{weight factor for each system}\notag\\")
        self.playWait(FadeOut(energy_state))
        self.playWait(Write(hamiltonian_weight))
        self.playWait(FadeOut(hamiltonian_weight))
        
        
        
        example1 = MathTex("\\lambda_{10} = 0.310231").next_to(energy_state,DOWN,buff=1).shift(LEFT)
        example2 = MathTex("s = 1.2").next_to(example1,RIGHT,buff=1)
        self.playWait(Write(example1))
        self.playWait(Write(example2)) 
        self.playWait(FadeOut(example1,example2))
        
        tex_final = MathTex(r"(\lambda_1,...,\lambda_N) \rightarrow \langle \lambda_1\rangle, \>\> \langle \lambda_1-\lambda_2\rangle, ... \> \langle f(\lambda_1,..,\lambda_N)\rangle \\\text{exact spectrum} & \rightarrow \text{statistical properties of spectrum}\notag\\ \text{requires: knowing $\&$ diagonalizing $H$} & \rightarrow \>\> \rho(x), P(s)")
        tex_final.scale(0.75).shift(LEFT*0.1)
        self.playWait(Write(tex_final))

        
        
        
        
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