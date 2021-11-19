import sys
import os


class Engine():
    def __init__(self):
        super(Engine, self).__init__()

    def get_Engine(self):
        current_engine = ('') #Or placer le return à la place de l.14/l.17

        if 'maya' in sys.executable:
            from engine import engine_maya as EngineM
            current_engine = ('Maya')
        elif 'houdini' in sys.executable:
            from engine import engine_hou as EngineH
            current_engine = ('Houdini')

        if current_engine == ('Maya'):
            return EngineM.Maya_Engine
        elif current_engine == ('Houdini'):
            return EngineH.Houdini_Engine