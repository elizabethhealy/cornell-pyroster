import json


"""
Represents a class level

Attributes
----------
key: str
    a shortened description representing the class level ex. 1000
"""
class ClassLevel:
  def __init__(self, key, description):
    self.key = key

  def __str__(self):
    return "ClassLevel(key="+self.key+")"

  def __eq__(self,other):
    if not isinstance(other, ClassLevel):
      return NotImplemented
    return self.key==other.key


"""
Construct an ClassLevel object from a json representing a class level

Parameters: json

Returns: an ClassLevel object
"""
def class_level_from_json(json):
  return AcademicLevel(key=json["descr"])

###
#example class level json
# {"value":"2000",
# "descr":2000}