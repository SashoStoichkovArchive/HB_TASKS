import json
import xml.etree.ElementTree as ET

class Jsonable:
    def to_json(obj, indent=4):
        d = dict()

        d.update({"type": obj.__class__.__name__, "dict": obj.__dict__})
        d = json.dumps(d, indent=4)

        return d

    @classmethod
    def from_json(cls, json_string):
        d = json.loads(json_string)

        return cls(**d["dict"])

class Xmlable:
    def to_xml(obj):
        s = "<" + obj.__class__.__name__ + ">"

        for k, v in enumerate(obj.__dict__):
            s += "<" + str(v) + ">" + str(obj.__dict__[str(v)]) + "</" + str(v) + ">"

        s += "</" + obj.__class__.__name__ + ">"

        return s

    @classmethod
    def from_xml(cls, xml_string):
        pass

class Panda(Jsonable, Xmlable):
    def __init__(self, **kvargs):
        for k, v in kvargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

if __name__ == "__main__":
    p = Panda(name="Ivo", age=4)

    # js = p.to_json()
    # p1 = p.from_json(js)
    # print(p == p1)

    print(p.to_xml())
    xs = p.to_xml()
    # p2 = p.from_xml(xs)
    # print(p == p2)
