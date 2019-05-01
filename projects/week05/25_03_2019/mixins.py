import json
import xml.etree.ElementTree as ET

class Jsonable:
    def to_json(self, indent=4):
        json_str = json.dumps({"dict": self.__dict__, 
                               "type": self.__class__.__name__},
                              indent=indent)
        return json_str

    def save_json_data_to_file(self):
        with open(str(self.__hash__()) + '.json', 'wb'):
            pass

    @classmethod
    def from_json(cls, json_string):
        cls_data = json.loads(json_string)
        if cls_data['type'] != cls.__name__:
            raise(ValueError('Error, expected type {}, got {}'.format(cls.__name__, cls_data['type'])))
        return cls(**cls_data['dict'])
        # return Panda(name='ivo', age=45, is_adult=True)


class Xmlable:
    def to_xml(self):
        root = ET.Element(self.__class__.__name__)
        for key, value in self.__dict__.items():
            ET.SubElement(root, key).text = str(value)
        xml = ET.tostring(root)
        return xml

    @classmethod
    def from_xml(cls, xml_string):
        xml_data = ET.fromstring(xml_string)
        if xml_data.tag != cls.__name__:
            raise (ValueError('Error, expected type {}, got {}'.format(cls.__name__, xml_data.tag)))

        kwargs = {child.tag: child.text for child in xml_data}
        return cls(**kwargs)


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return str(self.__dict__)

    def print_attributes(self):
        for att, val in self.__dict__.items():
            print(att + ': ' + str(val))

if __name__ == "__main__":
    # p1 = Panda(name='ivo', age=45, is_adult=True, lst=[1, 2, 3])
    # panda_json = p1.to_json()
    # print(panda_json)
    # p2 = Panda.from_json(panda_json)
    # p1.print_attributes()
    # print('')
    # p2.print_attributes()
    # print(p1 == p2)

    px1 = Panda(name='ivo', age=45, is_adult=True, lst=[1, 2, 3])
    xml_str = px1.to_xml()
    px2 = Panda.from_xml(xml_str)
    print('')
    px2.print_attributes()

    # print(p1.__dict__)
    # print(p2.__dict__)
    print(px1.__dict__)
    print(px2.__dict__)
    
    # print(hash(p1))
    # print(hash(p2))
    # print(hash(px1))
    # print(hash(px2))