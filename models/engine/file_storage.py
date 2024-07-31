#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        if cls:
            result_dict = {}
            if cls is not str:
                try:
                    cls = cls.__name__
                except AttributeError:
                    pass
            for k in FileStorage.__objects.keys():
                if cls in k:
                    result_dict[k] = FileStorage.__objects[k]
            return result_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ deletes obj from __objects """
        if obj:
            del FileStorage.__objects[obj.to_dict()["__class__"] + '.' + obj.id]

    def cities(self, state_id):
        """ returns all cities with state id """
        cities = self.all(City)
        result_list = []
        for i in cities:
            if i.state_id == state_id:
                result_list.append(i)
        return result_list

    def reviews(self, place_id):
        """ returns all reviews with matching place id """
        reviews = self.all(Review)
        result_list = []
        for i in reviewss:
            if i.place_id == place_id:
                result_list.append(i)
        return result_list

    def close(self):
        self.reload()
