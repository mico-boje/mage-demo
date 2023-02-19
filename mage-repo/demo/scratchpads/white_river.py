"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
import os

root = os.getcwd()
print(root)

print(os.listdir(root))

print(os.listdir(os.path.join(root, "demo")))