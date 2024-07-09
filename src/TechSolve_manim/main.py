from .scenes.GridScene import GridScene

def greeting():
   return "Hello, TechSolve_manim!"

def startScene(outputFilePath: str = './pics', fileName: str = 'GridScene.png'):
   scene = GridScene(outputFilePath, fileName)
   scene.render()