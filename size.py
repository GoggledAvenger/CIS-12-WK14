# Interactive Exercises from https://thartmanoftheredwoods.github.io/CIS-12/week_14py.html

class Size:
    """size of animal"""

    SUPPORTED_SIZES = ('large', 'medium', 'small')

    def __init__(self, size: str):
        if size in Size.SUPPORTED_SIZES:
            self.size = size
        else:
            raise (Exception("Invalid Size."))

    def __str__(self):
        return f'{self.size}'

    def __eq__(self, other):
        return self.size == other.size