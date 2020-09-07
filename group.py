import json


"""
Represents an academic group

Attributes
----------
key: str
    a shortened description representing the group ex. "AG"
description: str
    a description of the group
"""
class Group:
  def __init__(self, key, description):
    self.key = key
    self.description = description

  def __str__(self):
    return "Group(key="+self.key+", description="+self.description+")"
  
  def __eq__(self,other):
    if not isinstance(other, Group):
      raise NotImplemented
    return self.key==other.key and self.description==other.description


"""
Construct a group object from a json representing an academic group

Parameters: json

Returns: a Group object
"""
def group_from_json(json):
  return Group(key=json["value"], description=json["descr"])

###
#example group json
# {"value":"AG",
# "descr":"Agriculture and Life Sciences"}