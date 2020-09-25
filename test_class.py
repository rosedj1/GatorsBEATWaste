class PlasticItem:
    """A class to manage plastic items."""
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def get_weight(self):
        """Return the weight of this item."""
        return self.weight
