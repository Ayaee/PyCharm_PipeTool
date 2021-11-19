import hou as hou

hard_coded_path = 'G:/Artfx/TD4/WS_MicroFilm/MOVIE/ASSETS/ROAD/MODELING/PUBLISH/ROAD_MODELING_v001.hipnc'


class Houdini_Engine():
    def open(path):
        hou.hipFile.load(path)

    def save(self):
        hou.hipFile.saveAndIncrementFileName()

    def tool(self):
        pass

if __name__ == '__main__':
    Houdini_Engine.open(hard_coded_path)
