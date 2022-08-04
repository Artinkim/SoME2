from manim import *

class Integral(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [1, 2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()
        
        t1 = ValueTracker(0.0)
        t2 = ValueTracker(0.3)

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
    
        riemann_area = always_redraw(lambda: ax.get_riemann_rectangles(curve_1, x_range=[0.0, t1.get_value()], dx=t2.get_value(), color=BLUE, fill_opacity=0.5))
        self.add(ax, curve_1, line_1)
        self.add(riemann_area)
        self.play(t1.animate(rate_func=linear).set_value(4),run_time=1)
        self.play(t2.animate(rate_func=linear).set_value(0.03),run_time=1)
        t2.set_value(0.03)
        self.play(t1.animate(rate_func=linear).set_value(4),run_time=1)
        self.wait(1)
