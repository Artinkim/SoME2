from manim import *
import numpy as np
import scipy.stats

class FunctorEv:
    def __init__(self, i, eigenValues, vt):
        self.i, self.eigenValues, self.vt = i, eigenValues, vt
    
    def __call__(self, d):
        # print(np.linalg.eig(self.matrix[int(self.vt.get_value())]))
        d.set_value(self.eigenValues[int(self.vt.get_value())][self.i])


class FunctorD:
    def __init__(self, road, evs, i, shift=[0., 0., 0.]):
        self.road, self.evs, self.i, self.shift = road, evs, i, shift
    
    def __call__(self, d):
        d.move_to(self.road.number_to_point(self.evs[self.i].get_value())).shift(self.shift)


class FunctorB:
    def __init__(self, buses, i):
        self.buses, self.i = buses, i
    
    def __call__(self, b):
        b.become(BraceBetweenPoints(self.buses[self.i].get_center(), self.buses[self.i+1].get_center(), direction=DOWN)).shift(DOWN*0.3)


class FunctorDiff:
    def __init__(self, spaces, evs, i):
        self.spaces, self.evs, self.i = spaces, evs, i
    
    def __call__(self, d):
        d.set_value(self.evs[self.i+1].get_value()-self.evs[self.i].get_value()).next_to(self.spaces[self.i], direction=DOWN)


class Cars(Scene):
    def construct(self):
        np.random.seed(1)

        size = 10
        iterations = 10000
        t = ValueTracker(0)

        NTex = Text("N = " + str(size) + " (" + str(size) + " buses in one hour)").scale(0.5).to_corner(corner=LEFT+UP, buff=0.5)
        self.add(NTex)

        pvs = [scipy.stats.poisson.rvs(20000, size=size) for _ in range(iterations)]

        evTexs = [MathTex("x_" + str(i+1) + " = ") for i in range(size)]
        Group(*evTexs).arrange(direction=DOWN).to_corner(corner=LEFT+UP, buff=0.5)
        for i in range(len(pvs)):
            pvs[i] = np.sort(pvs[i])
            pvs[i] = (pvs[i]-20000)/100*2
        evs = [DecimalNumber(fill_opacity=0).add_updater(FunctorEv(i, pvs, t)).update().next_to(evTexs[i]) for i in range(size)]
        # self.play(*[Write(evTexs[i]) for i in range(len(evTexs))], *[Write(evs[i]) for i in range(len(evs))])
        self.add(*evs)
        
        road = NumberLine(x_range=[-8, 8, 1], length=5).to_edge(buff=0.5).add_numbers(font_size=22)
        shownRoad = NumberLine(x_range=[0, 60, 5], length=5).to_edge(buff=0.5).add_numbers(font_size=22)
        buses = [Dot().add_updater(FunctorD(road, evs, i)).update() for i in range(size)]
        busImages = [ImageMobject("../bus.png").scale(0.1).add_updater(FunctorD(road, evs, i, UP*0.5)).update() for i in range(size)]
        self.add(shownRoad)
        temp = [evTexs[i].copy() for i in range(len(evTexs))]
        # self.play(*[Transform(temp[i], buses[i].copy()) for i in range(size)])
        self.add(*buses)
        # self.remove(*temp)
        # self.play(*[FadeIn(busImages[i], scale=1.5) for i in range(len(busImages))])

        spaces = [BraceBetweenPoints(ORIGIN, ORIGIN).add_updater(FunctorB(buses, i)).update() for i in range(size-1)]
        spaceNums = [DecimalNumber(font_size=18).add_updater(FunctorDiff(spaces, evs, i)).update() for i in range(size-1)]
        self.add(*spaces, *spaceNums)
        self.wait(3)
        self.remove(*spaceNums)


        freqs = np.zeros((len(pvs), 40))
        totalFreqs = [(size-1)*(i+1) for i in range(len(freqs))]
        for i in range(len(pvs)):
            freqs[i] = freqs[i-1].copy()
            for j in range(size-1):
                freqs[i][np.abs(int(4/2*size/5*(pvs[i][j+1]-pvs[i][j])))] += 1
        def chartFunc(c: BarChart, values, total):
            values = values/total
            # np.ceil()
            top = np.ceil(np.max(values)*(10**2))/(10**2)
            c.become(BarChart(values=values, y_range=[0, top, np.round(top/10, decimals=3)], x_length=5, y_length=5).move_to(RIGHT*3))
        # chart = BarChart(values=freqs[0], y_range=[0,10000,1000], x_length=5, y_length=5).add_updater(lambda c: c.change_bar_values(freqs[int(t.get_value())])).update().move_to(RIGHT*3)
        chart = BarChart(values=freqs[0], y_range=[0,10000,1000], x_length=5, y_length=5).add_updater(lambda c: chartFunc(c, freqs[int(t.get_value())], totalFreqs[int(t.get_value())])).update()
        x_label = chart.get_x_axis_label("s", direction=RIGHT)
        y_label = chart.get_y_axis_label("P(s)", direction=UP)
        self.add(chart, x_label, y_label)
        # return
        # chartPrev = BarChart(values=freqs[-1], y_range=[0,10000,1000], x_length=5, y_length=5).move_to(LEFT*3)
        chartPrev = BarChart(values=freqs[-1])
        chartFunc(chartPrev, freqs[-1], totalFreqs[-1])
        chartPrev.move_to(LEFT*3)


        self.play(t.animate(rate_func=rate_functions.ease_in_expo).set_value(iterations-1), run_time=7)
        self.wait(3)
        # return
        self.play(*[FadeOut(x, shift=LEFT*10) for x in self.mobjects])






        t = ValueTracker(0)
        # matricies = [[[-5, 10], [10, 10]], *[np.random.randint(low=bounds[0], high=bounds[1], size=(size, size)) for _ in range(iterations)]]
        # matricies = [[[np.random.randn() for y in range(size)] for x in range(size)] for _ in range(iterations)]
        matricies = [np.round(np.random.randn(size, size), decimals=2) for _ in range(iterations)]
        for m in matricies:
            for x in range(len(m)):
                for y in range(x):
                    m[x][y] = m[y][x]
        eigenValues = [np.sort(np.linalg.eig(m)[0]) for m in matricies]
        matrix = Matrix([]).add_updater(lambda m: m.become(Matrix(matricies[int(t.get_value())])).to_corner(corner=LEFT+UP, buff=0.5)).update()
        evTexs = [MathTex("\lambda_" + str(i+1) + " = ") for i in range(size)]
        Group(*evTexs).arrange(direction=DOWN).next_to(matrix)
        evs = [DecimalNumber(fill_opacity=0).add_updater(FunctorEv(i, eigenValues, t)).update().next_to(evTexs[i]) for i in range(size)]
        # self.add(matrix)
        self.add(*evs)
        # self.play(*[Write(evTexs[i]) for i in range(len(evTexs))], *[Write(evs[i]) for i in range(len(evs))])

        road = NumberLine(x_range=[-8, 8, 1], length=5).to_edge(buff=0.5).add_numbers(font_size=22)
        shownRoad = NumberLine(x_range=[0, 60, 5], length=5).to_edge(buff=0.5).add_numbers(font_size=22)
        buses = [Dot().add_updater(FunctorD(road, evs, i)).update() for i in range(size)]
        busImages = [ImageMobject("../bus.png").scale(0.1).add_updater(FunctorD(road, evs, i, UP*0.5)).update() for i in range(size)]
        self.add(shownRoad)
        temp = [evTexs[i].copy() for i in range(len(evTexs))]
        # self.play(*[Transform(temp[i], buses[i].copy()) for i in range(size)])
        self.add(*buses)
        # self.remove(*temp)
        # self.play(*[FadeIn(busImages[i], scale=1.5) for i in range(len(busImages))])

        spaces = [BraceBetweenPoints(ORIGIN, ORIGIN).add_updater(FunctorB(buses, i)).update() for i in range(size-1)]
        spaceNums = [DecimalNumber(font_size=18).add_updater(FunctorDiff(spaces, evs, i)).update() for i in range(size-1)]
        self.add(*spaces, *spaceNums)
        self.wait(3)
        self.remove(*spaceNums)

        freqs = np.zeros((len(matricies), 40))
        for i in range(len(matricies)):
            freqs[i] = freqs[i-1].copy()
            for j in range(size-1):
                freqs[i][int(4*size/5/1.5*(eigenValues[i][j+1]-eigenValues[i][j]))] += 1
        # chart = BarChart(values=freqs[0], y_range=[0,10000,1000], x_length=5, y_length=5).add_updater(lambda c: c.change_bar_values(freqs[int(t.get_value())])).update().move_to(RIGHT*3)
        chart = BarChart(values=freqs[0], y_range=[0,10000,1000], x_length=5, y_length=5).add_updater(lambda c: chartFunc(c, freqs[int(t.get_value())], totalFreqs[int(t.get_value())])).update()
        x_label = chart.get_x_axis_label("s", direction=RIGHT)
        y_label = chart.get_y_axis_label("P(s)", direction=UP)
        self.add(chart, x_label, y_label)


        self.play(t.animate(rate_func=rate_functions.ease_in_expo).set_value(iterations-1), run_time=7)
        self.wait(3)


        self.remove(*self.mobjects)
        self.add(chart, NTex, x_label, y_label)
        xPrev_label = chartPrev.get_x_axis_label("s", direction=RIGHT)
        yPrev_label = chartPrev.get_y_axis_label("P(s)", direction=UP)
        self.play(FadeIn(chartPrev, shift=RIGHT), FadeIn(xPrev_label, shift=RIGHT), FadeIn(yPrev_label, shift=RIGHT))


        poissonFunc = ParametricFunction(lambda x: (x*0.5, 5.3*np.exp(-x), 0), t_range=[0, 3.5]).move_to(LEFT*4.0+UP*0.1)
        gaussianFunc = ParametricFunction(lambda x: (x*0.75, 0.98*6.5*0.5*np.pi*x*np.exp(-0.25*np.pi*x*x), 0), t_range=[0, 3]).move_to(RIGHT*2.25+DOWN*1.25+UP*1.2+LEFT*0.1)
        self.play(Create(poissonFunc), Create(gaussianFunc), run_time=3)

        # poissonTex = MathTex("\lim_{s\\rightarrow0} P_{Poisson}(s) = 1").next_to(chartPrev, direction=DOWN)
        poissonTex = MathTex("P(s) \propto e^{-s}").next_to(chartPrev, direction=DOWN)
        # gaussianTex = MathTex("\lim_{s\\rightarrow0} P_{WD}(s) = 0").next_to(chart, direction=DOWN)
        gaussianTex = MathTex("P(s) \propto s e^{-s^2}").next_to(chart, direction=DOWN)
        self.play(Write(poissonTex), Write(gaussianTex), run_time=1)

        self.wait(5)