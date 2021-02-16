class Box:
    
    def __init__(self):
        self._contents = list()
        self._open = False
        self.capacity = None

    # -------------[getter]-----------------
    def get_capacity(self):
        return self.capacity

    def is_open(self):
        return self._open
    # --------------------------------------

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

    def action_look(self):
        if self._open:
            str_contents = ", ".join(self._contents)
            return f"La boite contient : {str_contents}"

        return "La boite est fermee"

    def set_capacity(self, capacity):
        self.capacity = capacity

    def has_room_for(self, t):
        if self.capacity != None:
            return t.volume() <= self.capacity
        else:
            return True

    def action_add(self, t):
        if self._open:
            if self.has_room_for(t):
                self.add(t)
                self.capacity -= t.volume()
                return True
            else:
                return False
        else:
            return False

class Thing:

    def __init__(self, volume):
        self._volume = volume

    # -------------[getter]-----------------  
    def volume(self):
        return self._volume
    # --------------------------------------
