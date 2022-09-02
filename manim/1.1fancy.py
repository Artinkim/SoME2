from manim import *
import numpy as np

class Fancy(Scene):
    def construct(self):
        np.random.seed(1)

        # axes = ThreeDAxes(x_range=[-100, 100, 10], y_range=[-100, 100, 10], z_range=[-100, 100, 10])
        # self.set_camera_orientation(phi=75 * DEGREES, theta=35 * DEGREES)
        # lines = [Line3D(start=axes.c2p(100-150*np.random.rand(3))[0], end=axes.c2p(100-150*np.random.rand(3))[0]).set_color([random_color() for __ in range(1)]) for _ in range(10)]
        # self.add(axes)
        # self.wait(2)
        # self.play(*[Create(lines[i]) for i in range(len(lines))], run_time=1)
        # self.wait()

        # self.move_camera(focal_distance=6, added_anims=[FadeOut(axes, *lines)])
        # self.wait()

        # axes = Axes()
        # bsCoords = [[[4-8*np.random.random(), 4-8*np.random.random(), 0] for _ in range(4)] for i in range(5)]
        # for i in range(len(bsCoords)):
        #     bsCoords[i].sort()
        #     bsCoords[i][0][0] = -4
        #     bsCoords[i][3][0] = 4
        # # print(bsCoords)
        # bs = [CubicBezier(start_anchor=bsCoords[i][0], start_handle=bsCoords[i][1], end_handle=bsCoords[i][2], end_anchor=bsCoords[i][3]).set_color([random_color() for __ in range(3)]).scale(0.6) for i in range(len(bsCoords))]
        # self.play(*[Create(x) for x in bs])
        # self.wait()
        
        # # for i in range(8):
        # self.play(*[Rotate(x, angle=-8*PI, about_point=ORIGIN) for x in bs], run_time=2, rate_func=linear)
        # self.wait()

        # Arrow().mov
        # arrows = [Arrow(stroke_width=24).scale(1.5).move_to(RIGHT*i*4+2*DOWN).rotate(3*PI/2) for i in range(-1, 2)]
        # self.play(*[Write(arrow) for arrow in arrows])
        # self.wait(2)
        # self.play(*[Unwrite(arrow) for arrow in arrows])

        # funcTex = MathTex("\\zeta(z)").to_edge(edge=UP).shift(DOWN*1.5)
        # funcRight = MathTex(r"\cong \sum_{n=1}^{\infty}\frac{1}{n^z}").next_to(funcTex)
        # self.add(funcTex, funcRight)

        # tex = MathTex(r"H(J_1,J_2,\triangle_z)",  r" &= ",  r"J_1 \sum_i (\sigma_i^x\sigma_{i+1}^x + \sigma_i^y\sigma_{i+1}^y + \Delta_z \sigma_i^z\sigma_{i+1}^z)", " + ", r"J_2 \sum_i (\sigma_i^x\sigma_{i+2}^x + \sigma_i^y\sigma_{i+2}^y + \Delta_z \sigma_i^z\sigma_{i+2}^z)").scale(0.5)
        # b = [Brace(tex[2]), Brace(tex[4])]
        # bTex = [Tex("nearest-neighbour interactions").next_to(b[0], direction=DOWN).scale(0.5), Tex("next-nearest neighbour interactions").next_to(b[1], direction=DOWN).scale(0.5)]
        # self.play(Write(tex), run_time=1)
        # self.play(*[Write(x) for x in b], *[Write(x) for x in bTex], run_time=1)
        # self.wait(2)
        # self.wait()

