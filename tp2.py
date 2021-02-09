class Box:
    
    def __init__(self):
        self._contents = list()

    def __contains__(self, machin):
        return machin in self._contents

    def add(self, truc):
        self._contents.append(truc)

