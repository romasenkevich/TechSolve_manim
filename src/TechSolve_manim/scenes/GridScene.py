from manim import *
        
class GridScene(Scene):
    
    def __init__(self, outputFilePath, fileName, **kwargs):
        self.setupScene(outputFilePath, fileName)
        super().__init__(**kwargs)
    
    def construct(self):
        grid_size = 5
        self.camera.frame_width = grid_size * 2 
        self.camera.frame_height = grid_size * 2 
        grid_lines = self.create_grid_lines()
        self.add(grid_lines)
        
    def setupScene(self, outputFilePath, fileName):    
        config.images_dir = outputFilePath
        config.output_file = fileName
        config.background_color = WHITE
        config.save_last_frame
        config.pixel_height = 1920
        config.pixel_width = 1920
        config.preview = False

    def create_grid_lines(self, grid_size = 5, step_size = 0.5, line_thickness = 0.5, grid_color = GRAY):
        vertical_lines = VGroup()
        for i in range(int(grid_size * 2 / step_size) + 1):
            x = -grid_size + i * step_size
            line = Line([x, -grid_size, 0], [x, grid_size, 0], stroke_width=line_thickness, color=grid_color)
            vertical_lines.add(line)
        horizontal_lines = VGroup()
        for i in range(int(grid_size * 2 / step_size) + 1):
            y = -grid_size + i * step_size
            line = Line([-grid_size, y, 0], [grid_size, y, 0], stroke_width=line_thickness, color=grid_color)
            horizontal_lines.add(line)
        return VGroup(vertical_lines, horizontal_lines)
