from manim import *
import numpy as np
import string

class RadomMatrix(MobjectMatrix):
    
    def __init__(self, size, bounds, precision, vt):
        self.size = size
        self.bounds = bounds
        self.precision = precision
        self.nums = [[DecimalNumber() for _ in range(self.size[1])] for __ in range(self.size[0])]
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.nums[x][y].add_updater(lambda d: d.set_value(np.round(vt.get_value()*0+self.bounds[0]+(self.bounds[1]-self.bounds[0])*np.random.random(), decimals=self.precision)))

        super().__init__(self.nums, h_buff=2, element_alignment_corner=DR)
        

class RandomMatrix(Scene):
    totalChanges = 10

    def construct(self):
        np.random.seed(1)
        vt = ValueTracker(0)
        
        m = []
        size = (2, 2)
        bounds = (1, 10)
        m.append(MobjectMatrix([[DecimalNumber(np.round(np.random.uniform(*bounds), decimals=2)) for y in range(size[1])] for x in range(size[0])], h_buff = 1.6))
        m.append(MobjectMatrix([[MathTex("Gaussian(\mu,\sigma)") for y in range(size[1])] for x in range(size[0])], h_buff = 3.5))
        m.append(MobjectMatrix([[MathTex("Uniform (a,b)") for y in range(size[1])] for x in range(size[0])], h_buff = 3.5))
        signs = [" + ", " - "]
        m.append(MobjectMatrix([[MathTex(str(int(m[0][0][size[1]*x+y].get_value()))+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"i") for y in range(size[1])] for x in range(size[0])], h_buff = 2.6))
        m.append(MobjectMatrix([[MathTex(m[-1][0][size[1]*x+y].tex_string+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"j"+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"k") for y in range(size[1])] for x in range(size[0])], h_buff = 4.6))
        m.append(MobjectMatrix([[MathTex(m[-1][0][size[1]*x+y].tex_string+np.random.choice(signs)+"...") for y in range(size[1])] for x in range(size[0])], h_buff = 5.4))
        m.append(MobjectMatrix([
            [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1P}")],
            [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2P}")],
            [MathTex(), MathTex(), MathTex("..."), MathTex()],
            [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NP}")]], h_buff = 1.6))
        m.append(MobjectMatrix([
            [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1N}")],
            [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2N}")],
            [MathTex(), MathTex(), MathTex("..."), MathTex()],
            [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NN}")]], h_buff = 1.6))
        size = (5, 5)
        bounds = (-10, 10)
        m.append(DecimalMatrix(np.round(np.random.uniform(*bounds,size=size), decimals=2), h_buff = 1.6))
        m.append(RadomMatrix(size=size, bounds=bounds, precision=2, vt=vt))
        
        # scale matricies then add first matrix to the scene
        for x in m:
            x.scale(0.5)
        a = m[0].copy()
        self.add(a)
        self.wait(1)
        
        # # initialize axis and graphs for the two distributions
        # axes1 = Axes(x_range=[-5,6,1], y_range=[0,1.1, 0.2]).scale(0.5).add_coordinates().scale(0.5).move_to(UL*2+LEFT*2)
        # axes1.add(Tex("0").scale(0.4).next_to(axes1.x_axis.n2p(0), DOWN*0.5))
        # guas = axes1.plot(lambda x: np.exp(-(x/3)**2),color=BLUE)
        # guas_area = axes1.get_area(guas)
        # axes2 = axes1.copy().next_to(axes1)
        # uniform = axes2.plot(lambda x: 1 if x>-3 and x<3 else 0, discontinuities=[-3,3], color=GREEN)
        # uniform_area = axes2.get_area(uniform)

        # # play chaning the matrix and showing distributions
        # self.play(Transform(a, m[1]),Create(axes1),Create(guas),run_time=1)
        # self.play(FadeIn(guas_area))
        # self.wait(1)
        # self.play(Transform(a, m[2]),Transform(axes1,axes2,rate_function=lingering),Create(uniform,rate_func=rush_into),run_time=1)
        # self.play(FadeIn(uniform_area))
        # self.wait(1)
        
        # # create list of element types matrix can hold
        # element_types = VGroup(
        #     MathTex("a"),
        #     MathTex("a + bi"),
        #     MathTex("{\displaystyle a+b\ \mathbf {i} +c\ \mathbf {j} +d\ \mathbf {k} }"),
        #     MathTex("{\displaystyle a+b\ \mathbf {i} +c\ \mathbf {j} +d\ \mathbf {k} }","...")
        # ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.75).next_to(axes1)

        # # play changing the matrix and showing element types
        # self.play(Transform(a, m[0]), FadeOut(axes1), FadeIn(element_types[0]))
        # self.wait(1)
        # self.play(Transform(a, m[3]), FadeIn(element_types[1]))
        # self.play(Transform(a, m[4]), FadeIn(element_types[2]))
        # self.play(Transform(a, m[5]), FadeIn(element_types[3]))
        # self.wait(1)

        # # shows sizes of matrices 
        # b = Brace(m[6])
        # b1tex, b2tex = b.get_tex("N\\text{x}P"), b.get_tex("N\\text{x}N") 
        # self.play(Transform(a, m[6]),FadeIn(b,b1tex))
        # self.wait(1)
        # self.play(Transform(a, m[7]), Transform(b1tex, b2tex))
        # self.wait(1)
        
        # # show specific case of matrix 5x5 (-10,10)
        # axes3 = Axes(x_range=[-12,13,2], y_range=[0,1.1, 0.2]).scale(0.5).add_coordinates().scale(0.5).move_to(UL*2+LEFT)
        # axes3.add(Tex("0").scale(0.4).next_to(axes3.x_axis.n2p(0), DOWN*0.5))
        # uniformN = axes3.plot(lambda x: 1 if x>-10 and x<10 else 0, discontinuities=[-10,10], color=GREEN)
        # uniform_areaN = axes3.get_area(uniformN)
        # integer_tex = element_types.submobjects[0]
        # integer_texN = integer_tex.copy().next_to(axes3).shift(RIGHT)
        # element_types.remove(integer_tex)
        # self.play(
        #     Transform(a, m[8]),
        #     FadeOut(guas,guas_area,b,b1tex),
        #     Transform(uniform,uniformN),
        #     Transform(uniform_area,uniform_areaN),
        #     FadeIn(axes3),
        #     FadeOut(*element_types.submobjects),
        #     Transform(integer_tex,integer_texN),
        # )
        # integer_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(1.8,0.8),color=YELLOW)
        # self.play(Create(integer_arrow))
        # self.play(Create(MathTex("M_{ij} = ").scale(0.5).next_to(integer_texN,LEFT)))
        # self.wait(1)

        # # cycles through random matricies, moving arrow along distribution
        # self.remove(a)
        # a = m[9].copy()
        # self.add(a)
        # curr_arrow = integer_arrow.copy()
        # # integer_arrow.add_updater(lambda m: m.position_tip(vt.get_value()*0+axes3.c2p(np.random.uniform(-10,10),np.random.uniform(-10,10))))
        # # self.play(vt.animate.set_value(1), run_time=1)
        # left_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(-10,0.8),color=YELLOW)
        # right_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(10,0.8),color=YELLOW)
        # self.play(vt.animate.set_value(0.3), Transform(curr_arrow,left_arrow), run_time=2)
        # self.play(vt.animate.set_value(0.6), Transform(curr_arrow,right_arrow), run_time=2)
        # self.play(vt.animate.set_value(1), Transform(curr_arrow,integer_arrow), run_time=2)

        # show creation of 3 matricies then puts into row
        self.remove(a) 
        m_group = VGroup()
        original_vals = np.round(np.random.uniform(*bounds,size=(3,*size)), decimals=2)
        for i in range(3):
            temp = DecimalMatrix(original_vals[i], h_buff = 1.6).scale(0.5)
            self.add(temp)
            self.wait(0.25)
            self.play(temp.animate.scale(0.4).move_to(LEFT * 2*(1-i) + DOWN * 1.5))
            self.wait(0.25)
            m_group.add(temp)
        # show ensemble as collection of 3 previously created matricies
        m = m_group.submobjects
        left_brace, right_brace = MathTex("\\{").scale(1.7), MathTex("\\}").scale(1.7)
        ensemble = VGroup(MathTex("ensemble: "), left_brace, m[0].copy(), m[1].copy(), MathTex("..."), m[2].copy(), right_brace).arrange(RIGHT)
        self.play(TransformMatchingShapes(m_group, ensemble)) # tries tranforming all submobjects to ones in other group that match??? tranforming matching shapes does not work like normal transfrom method
        self.wait(1)
        a = DecimalMatrix(original_vals[0], h_buff = 1.6).scale(0.5)
        self.play(TransformMatchingShapes(ensemble,a))
        self.wait(1)
        
        # transform group to single matrix
        # vals = np.round(np.random.uniform(*bounds,size=size), decimals=2)
        # matrix_decimals = [[DecimalNumber(vals[y,x]) for y in range(size[1])] for x in range(size[0])] #.scale(0.5).arrange(RIGHT).next_to(a,DOWN)
        #d = DecimalMatrix(np.round(np.random.uniform(*bounds,size=size), decimals=2), h_buff = 1.6).scale(0.5)
        
        letter_matrix = Matrix(np.reshape(np.array(list(string.ascii_lowercase)[:-1]),(5,5))).scale(0.5)
        a = m[7]
        self.play(Transform(a, letter_matrix))
        entries = a.copy().get_entries()
        left_brace, right_brace = MathTex("["), MathTex("]")
        decimal_list = VGroup(*[left_brace,*entries[:3], MathTex("..."), *entries[-2:],right_brace]).arrange(RIGHT).next_to(a,DOWN)
        self.play(TransformMatchingShapes(a.copy(),decimal_list))
        [self.play(ShowPassingFlash(SurroundingRectangle(e1),time_width=1),ShowPassingFlash(SurroundingRectangle(e2),time_width=1),run_time=0.5) for e1,e2 in zip(a.get_entries(),decimal_list.submobjects[1:4])]
        surrounding_rect = SurroundingRectangle(decimal_list.submobjects[4])
        independent_tex1 = MathTex("P(M)=P(a)P(b)P(c)...P(x)P(y)").scale(0.5).next_to(a,RIGHT)
        independent_tex2 = MathTex("\prod_{ij=1}^{\infty} a_{i}").scale(0.5).next_to(a,DOWN)
        self.add(surrounding_rect,independent_tex1)
        self.add()
        [self.play(ShowPassingFlash(SurroundingRectangle(e),time_width=1),run_time=0.05) for e in a.get_entries()[3:23]]
        self.remove(surrounding_rect)
        [self.play(ShowPassingFlash(SurroundingRectangle(e1),time_width=1),ShowPassingFlash(SurroundingRectangle(e2),time_width=1),run_time=0.5) for e1,e2 in zip(a.get_entries()[23:],decimal_list.submobjects[5:7])]
        self.wait(1)
        # entries = decimal_list.copy().submobjects
        # padded_list = [*entries[1:4],*[entries[3]]*(len(a.get_entries())-7),*entries[-3:-1]]
        # print(len(padded_list),len(entries)) #22, 25
        # for mat_entry, list_entry in zip(a.get_entries(),padded_list):
        #self.play(Create(SurroundingRectangle(mat_entry)),Create(SurroundingRectangle(list_entry)),run_time=0.1)
        #self.wait(1) # ShowPassingFlash(time_width=0.1) or Create

        
