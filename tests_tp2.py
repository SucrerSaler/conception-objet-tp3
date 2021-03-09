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
    t = Thing(1)
    t1 = Thing(5)
    assert b.has_room_for(t)
    b.set_capacity(4)
    assert b.has_room_for(t)
    assert not b.has_room_for(t1)

def test_box_action_add():
    b = Box()
    t1 = Thing(5)
    t2 = Thing(10)
    b.set_capacity(6)
    assert not b.action_add(t1)
    assert not t1 in b
    b.open()
    assert b.action_add(t1)
    assert t1 in b
    assert not b.action_add(t2)
    assert not t2 in b

def test_box_find():
    b = Box(is_open=False, capacity=6)
    t1 = Thing(2, "ballon")
    t2 = Thing(1, "gant")
    b.open()
    b.action_add(t1)
    b.close()
    assert b.find("ballon") is None
    b.open()
    assert b.find("ballon") == t1
    assert b.find("gant") is None
    b.action_add(t2)
    assert b.find("gant") == t2

# ---------------------------------------------------------------------

def test_thing_create():
    t = Thing(3)

def test_thing_volume():
    t = Thing(3)
    assert t.volume() == 3

def test_thing_set_name():
    t = Thing(5)
    t.set_name("ballon")
    assert repr(t) == "ballon"

def test_thing_has_name():
    t = Thing(3, "ballon")
    assert t.has_name("ballon")
    assert not t.has_name("roue")