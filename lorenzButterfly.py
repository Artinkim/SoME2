from manim import *


class LorenzButterfly(ThreeDScene):
    coords = (1, 1, 1)
    axes = ThreeDAxes(x_range=[-100, 100, 10], y_range=[-100, 100, 10], z_range=[-100, 100, 10])
    a, b, c, d = 10, 25, 8/3, 0.01
    totalTime = 36

    def next(self):
        a, b, c, d = self.a, self.b, self.c, self.d  
        x, y, z = self.coords
        self.coords = x+d*(a*(y-x)), y+d*(x*(b-z)-y), z+d*(x*y-c*z)
        return self.coords

    def construct(self):
        axes = self.axes
        a, b, c, d = self.a, self.b, self.c, self.d        

        d1 = Dot3D(point=axes.coords_to_point(1, 1, 1), color=RED)
        for _ in range(5):
            d1.add_updater(lambda p: p.move_to(axes.c2p(self.next())[0]))
        def update_path1(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([d1.get_center()])
            path.become(previous_path)
            path.make_smooth().set_stroke(None,1)
        path1 = VMobject()
        path1.set_color(RED)
        path1.set_stroke(width=0.5)
        path1.set_points_as_corners([d1.get_center(), d1.get_center()])
        path1.add_updater(update_path1)
        
        self.add(d1, path1)

        d2 = Dot3D(point=axes.coords_to_point(1, 1, 1.05), color=BLUE)
        for _ in range(5):
            d2.add_updater(lambda p: p.move_to(axes.c2p(self.next())[0]))
        def update_path2(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([d2.get_center()])
            path.become(previous_path)
            path.make_smooth().set_stroke(None,1)
        path2 = VMobject()
        path2.set_color(BLUE)
        path2.set_stroke(width=0.5)
        path2.set_points_as_corners([d2.get_center(), d2.get_center()])
        path2.add_updater(update_path2)
        
        self.add(d2, path2)

        t = ValueTracker(0)
        self.set_camera_orientation(phi=75 * DEGREES, theta=35 * DEGREES)
        # self.add_updater(lambda _: self.set_camera_orientation(phi=75 * DEGREES, theta=360 * DEGREES * t.get_value()))
        self.add(axes)
        self.begin_ambient_camera_rotation(0.1)
        self.play(t.animate.set_value(1), run_time=self.totalTime)