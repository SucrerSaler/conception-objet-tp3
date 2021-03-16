import yaml
import io

def list_from_yaml(data):
    res = list()
    for elem in data:
        if elem.get("type") == "box":
            res.append(Box.from_yaml(elem))
        else:
            res.append(Thing.from_yaml(elem))
    return res


class Box:
    
    def __init__(self, is_open=False, capacity=None):
        self._contents = list()
        self._open = is_open
        self.capacity = capacity

    def __contains__(self, machin):
        return machin in self._contents

    # -------------[getter]-----------------
    def get_capacity(self):
        return self.capacity

    def is_open(self):
        return self._open
    # --------------------------------------

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

    def find(self, name):
        if self.is_open():
            for truc in self._contents:
                if truc.has_name(name):
                    return truc
            return None
        else:
            return None
    
    @staticmethod
    def from_yaml(data):
        is_open = data.get("is_open")
        capacity = data.get("capacity")
        return Box(is_open, capacity)

class Thing:

    def __init__(self, volume, name=None):
        self._volume = volume
        self._name = name

    def __repr__(self):
        return self._name

    # -------------[getter]-----------------  
    def volume(self):
        return self._volume
    # --------------------------------------

    def set_name(self, name):
        self._name = name

    def has_name(self, name):
        return self._name == name

    @staticmethod
    def from_yaml(data):
        volume = data.get("volume")
        name = data.get("name")
        return Thing(volume, name)