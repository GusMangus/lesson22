class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cuber(self):
        return self.z() * self.x() * self.y()


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.cuber()
