import sys


def get_Engine():
    current_engine = ('')  # Or placer le return à la place de l.14/l.17

    if 'maya' in sys.executable:
        from pipeline.engine import engine_maya as EngineM
        return EngineM.Maya_Engine()
    elif 'houdini' in sys.executable:
        from pipeline.engine import engine_hou as EngineH
        return EngineH.Houdini_Engine()
    else:
        from pipeline.engine import engine_base as EngineB
        return EngineB.Engine()

if __name__ == '__main__':
    test = get_Engine()
    print(test)
    print(test.implements)