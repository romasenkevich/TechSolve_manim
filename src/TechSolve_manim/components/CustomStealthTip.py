from manim import ArrowTip, VMobject, DEFAULT_ARROW_TIP_LENGTH, PI, BLACK, np

class CustomStealthTip(ArrowTip):

    def __init__(
        self,
        fill_opacity=1,
        stroke_width=3,
        length=DEFAULT_ARROW_TIP_LENGTH / 2,
        start_angle=PI,
        color = BLACK,
        **kwargs,
    ):
        self.start_angle = start_angle
        VMobject.__init__(
            self, fill_opacity=fill_opacity, stroke_width=stroke_width, **kwargs
        )
        self.set_points_as_corners(
            [
                [2, 0, 0],  # tip
                [-1.2, 1.6, 0],
                [0, 0, 0],  # base
                [-1.2, -1.6, 0],
                [2, 0, 0],  # close path, back to tip
            ]
        )
        self.color = color
        arrow = self.get_arrow()
        self.become(arrow)
        
    def rotate_point(self, point, angle):
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        return np.dot(rotation_matrix, point[:2])
        
    def get_arrow(self, hScale = 0.7, wScale = 1, scale = 0.1):
        
        hScale = hScale * scale
        wScale = wScale * scale
        
        p1 = np.array([0, 0, 0])
        c1 = np.array([0, 0, 0])
        c2 = np.array([0, 0, 0])
        p2 = np.array([-0.1 * hScale, 0, 0])

        p3 = np.array([-0.1 * hScale, 0, 0])
        c3 = np.array([-0.1 * hScale, 0.3 * wScale, 0])
        c4 = np.array([-0.5 * hScale, 0.5 * wScale, 0])
        p4 = np.array([-0.5 * hScale, 0.5 * wScale, 0])
        
        p5 = np.array([-0.5 * hScale, 0.5 * wScale, 0])
        c5 = np.array([-0.5 * hScale, 0.5 * wScale, 0])
        c6 = np.array([-0.5 * hScale, 0.5 * wScale, 0])
        p6 = np.array([2 * hScale, 0, 0])
        
        p7 = np.array([2 * hScale, 0, 0])
        c7 = np.array([2 * hScale, 0, 0])
        c8 = np.array([2 * hScale, 0, 0])
        p8 = np.array([-0.5 * hScale, -0.5 * wScale, 0])
        
        p9 = np.array([-0.5 * hScale, -0.5 * wScale, 0])
        c9 = np.array([-0.5 * hScale, -0.5 * wScale, 0])
        c10 = np.array([-0.1 * hScale, -0.3 * wScale, 0])
        p10 = np.array([-0.1 * hScale, 0, 0])

        arrow = VMobject(); arrow2 = VMobject()
        arrow.append_points([p1, c1, c2, p2])
        arrow.append_points([p3, c3, c4, p4])
        arrow.append_points([p5, c5, c6, p6])
        arrow.append_points([p7, c7, c8, p8])
        arrow.append_points([p9, c9, c10, p10])
        arrow.close_path()
        arrow.set_fill(self.color, opacity=1)
        arrow.set_color(self.color)
        arrow.set_stroke(width=4 * scale)
        arrow2.add(arrow)
        arrow2.set_points_as_corners([p1])
        arrow2.append_points([p1, c1, c2, p2])
        return arrow2

    @property
    def length(self):
        return np.linalg.norm(self.vector)        