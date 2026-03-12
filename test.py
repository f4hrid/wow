from game.assetloader import AssetLoader
config = AssetLoader('player', resize=4)

class Entity:
    def __init__(self):
        self.image = None

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.image = 0
        self.animation = Animation(self)

    def mover(self):
        self.animation.setimage()
        print(self.image)

class Animation(Entity):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def setimage(self):
        self.player.image = 1

player = Player()
player.mover()
