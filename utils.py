
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self) -> str:
        return "{} {}".format(self.x, self.y)
    

    def __getitem__(self, key):
        if key == 'x': return self.x
        elif key == 'y': return self.y 
        else: KeyError(f"Passed key '{key}' does not exist in Point object")
        