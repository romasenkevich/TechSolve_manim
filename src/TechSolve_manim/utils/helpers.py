from manim import config, WHITE

def setupScene(outputFilePath: str = './pics', fileName: str = 'picture.png'):    
    
    config.images_dir = outputFilePath
    config.output_file = fileName
    config.background_color = WHITE
    config.save_last_frame
    config.pixel_height = 1920
    config.pixel_width = 1920
    config.preview = False
