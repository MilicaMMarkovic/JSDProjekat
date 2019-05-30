from execute import execute
import os

execute(os.path.split(__file__)[0], 'grammar.tx', 'example.run', True, True)
