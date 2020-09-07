import json


"""
Represents an academic level

Attributes
----------
key: str
    a shortened description representing the academic level ex. "UG"
description: str
    a description of the academic level
"""
class AcademicLevel:
  def __init__(self, key, description):
    self.key = key
    self.description = description

  def __str__(self):
    return "AcademicLevel(key="+self.key+", description="+self.description+")"

  def __eq__(self,other):
    if not isinstance(other, AcademicLevel):
      return NotImplemented
    return self.key==other.key and self.description==other.description


"""
Construct an AcademicLevel object from a json representing an academic level

Parameters: json

Returns: an AcademicLevel object
"""
def academic_level_from_json(json):
  return AcademicLevel(key=json["value"], description=json["descr"])

###
#example academic level json
# {"value":"UG",
# "descr":"Undergraduate"}