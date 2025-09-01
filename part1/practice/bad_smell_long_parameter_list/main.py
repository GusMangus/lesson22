class Unit:
    def __init__(self, state, field):
        self.state = state
        self.field = field
        self.speed = 1

    def _speed_set(self):
        if self.state == 'fly':
            return self.speed *1.2
        elif self.state == 'crawl':
            return self.speed *0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction):
        speed = self._speed_set()
        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)



#
