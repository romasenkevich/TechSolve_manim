import os
import shutil
from TechSolve_manim.main import startScene

MEDIA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')

def remove_media_dir():
    if os.path.exists(MEDIA_DIR) and os.path.isdir(MEDIA_DIR):
        shutil.rmtree(MEDIA_DIR)
        print(f"Removed directory: {MEDIA_DIR}")

def main():
    startScene('./tests/pics', 'test_pic.png')
    remove_media_dir()

if __name__ == "__main__":
    main()