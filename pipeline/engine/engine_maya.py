import pymel.core as pm

#hard_coded_path = 'G:/Artfx/TD4/WS_MicroFilm/MOVIE/ASSETS/CAR/MODELING/PUBLISH/CAR_MODELING_V002.mb'


class Maya_Engine():

    def open(self, path):
        pm.openFile(path, force=True)

    def save(self, *args):
        pm.saveFile(force=True)

    def tool(self, *args):
        pm.system.createReference(pm.fileDialog2(fileMode=1, caption="Tool Référence"))

    implements = ['open', 'save', 'tool']

'''if __name__ == '__main__':
    Maya_Engine.open(hard_coded_path)'''
