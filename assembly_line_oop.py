
class AssemblyError(Exception):
    pass

class Screen:
    def __init__(self, size = 0, resolution = 0, screen_type = ''):
        self.size = size
        self.resolution = resolution
        self.screen_type = screen_type
    def __str__(self) -> str:
        return f"Size: {self.size} Resolution: {self.resolution} Screen Type: {self.screen_type}"

class Base:
    def __init__(self, height = 0, base_size = 0):
        self.height = height
        self.base_size = base_size
    def __str__(self) -> str:
        return f"Height: {self.height} Base Size: {self.base_size}"

class Monitor:
    def __init__(self, screen: Screen, base: Base):
        self.screen = screen
        self.base = base
    def __str__(self) -> str:
        return f"Screen: {self.screen}\nBase: {self.base}"
    def turn_on(self):
        return True

class Factory:
    assembled = {}
    @classmethod
    def assemble(cls, screen: Screen, base: Base) -> Monitor:
        try:
            assert screen.size and screen.resolution and screen.screen_type
            assert base.height and base.base_size
        except AssertionError as e:
            raise AssemblyError("Some values were not provided") from e
        else:
            cls.assembled[id(Monitor(screen, base))] = {
                'screen': {
                    'size': str(screen.size),
                    'resolution': str(screen.resolution),
                    'screen_type': screen.screen_type
                },
                'base': {
                    'height': str(base.height),
                    'base_size': str(base.base_size)
                }
            }


try:
    Factory.assemble(Screen(100, 100, 'LED'), Base(20, 70))
    Factory.assemble(Screen(200, 150, 'LED'), Base(30, 90))
except AssemblyError as ae:
    print(ae)
finally:
    for monitor in Factory.assembled.items():
        print(f"{monitor}\n")