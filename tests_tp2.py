from tp2 import *

def test_box_create():
    b = Box()

def test_box_add():
    b = Box ()
    b.add("truc1")
    b.add("truc2")

def test_box_in():
    b = Box ()
    b.add("truc1")
    b.add("truc2")
    assert "truc1" in b
    assert "truc2" in b

def test_box_remove():
    b = Box ()
    b.add("truc1")
    b.add("truc2")
    b.remove("truc2")
    assert "truc2" not in b

def test_box_is_open():
    b = Box()
    
    b.open()
    assert b.is_open()

    b.close()
    assert not b.is_open()

def test_box_action_look():
    b = Box()
    b.add("truc")
    b.add("truc2")
    b.open()
    assert b.action_look() == "La boite contient : truc, truc2"
    b.close()
    assert b.action_look() == "La boite est fermee"

def test_box_set_capacity():
    b = Box()
    b.set_capacity(5)
    assert b.get_capacity() == 5

def test_box_has_room_for():
    b = Box()
    t1 = Thing(5)
    b.set_capacity(4)
    assert not b.has_room_for(t1)

# ---------------------------------------------------------------------

def test_thing_create():
    t = Thing(3)

def test_thing_volume():
    t = Thing(3)
    assert t.volume() == 3

