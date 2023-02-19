"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable
import os

print(os.getcwd())
cur_dir = os.getcwd()
print(os.listdir(cur_dir))
#df = get_variable('cool_wood', 'load_csv', 'output_0')
