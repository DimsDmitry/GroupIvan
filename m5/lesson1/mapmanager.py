# напиши здесь код создания и управления картой
class Mapmanager():
    # управление картой
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.color = (0.0, 0.6, 1.0, 1)  # rgba
        # создаём основной узел карты
        self.startNew()
        # создаём строительные блоки
        self.addBlock((0, 10, 0))

    def startNew(self):
        # создаёт основу для карты
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
