import json


"""
Represents a subject

Attributes
----------
key: str
    a shortened description representing the subject ex. "AEM"
description: str
    a description of the subject
"""
class Subject:
  def __init__(self, key, description):
    self.key = key
    self.description = description

  def __str__(self):
    return "Subject(key="+self.key+", description="+self.description+")"
  
  def __eq__(self,other):
    if not isinstance(other, Subject):
      raise NotImplemented
    return self.key==other.key and self.description==other.description


"""
Construct a subject object from a json representing a subject

Parameters: json

Returns: a Subject object
"""
def subject_from_json(json):
  return Subject(key=json["value"], description=json["descrformal"])

#example subject json
# {"value":"AAS",
# "descr":"Asian American Studies",
# "descrformal":"Asian American Studies"}