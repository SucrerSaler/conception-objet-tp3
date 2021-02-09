class Box:
    
    def __init__(self):
        self._contents = list()
        self._open = False

    def __contains__(self, machin):
        return machin in self._contents

    def add(self, truc):
        self._contents.append(truc)

    def remove(self, truc):
        self._contents.remove(truc)

    def open(self):
        self._open = True
    
    def close(self):
        self._open = False

    def is_open(self):
        return self._open

    def action_look(self):
        if self._open:
            str_contents = ", ".join(self._contents)
            return f"La boite contient : {str_contents}"

        return "La boite est fermee"