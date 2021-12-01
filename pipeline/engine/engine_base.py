class Engine(object):
    implements = ['test', 'test2']

    def __init__(self):
        super(Engine, self).__init__()

    def test(self, path):
        print('coucou, je suis le test')
        print(path)


