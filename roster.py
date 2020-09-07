import json


"""
Represents a roster

Attributes
----------
key: str
    a shortened description representing the roster ex. "FA19"
description: str
    a description of the roster
"""
class Roster:
  def __init__(self, key, description):
    self.key = key
    self.description = description

  def __str__(self):
    return "Roster(key="+self.key+", description="+self.description+")"

  def __eq__(self,other):
    if not isinstance(other, Roster):
      return NotImplemented
    return self.key==other.key and self.description==other.description


"""
Construct a roster object from a json representing a roster

Parameters: json

Returns: a Roster object
"""
def roster_from_json(json):
  return Roster(key=json["slug"], description=json["descr"])

###
#example roster json
# {"slug":"FA14",
# "isDefaultRoster":"N",
# "strm":"2573",
# "descr":"Fall 2014",
# "descrshort":"2014FA",
# "defaultSessionCode":"1",
# "defaultCampus":"MAIN",
# "defaultLocation":"ITH",
# "defaultInstructionMode":"P",
# "sharing":"N",
# "archiveMode":"Y",
# "version":
#   {"status":"COMPLETE",
#   "referenceDttm":"2015-01-14T18:16:01-0500",
#   "catalogDttm":"2015-01-14T18:21:04-0500",
#   "descriptionSource":"CATALOG",
#   "showCatalogNote":"Y",
#   "catalogCourseNote":null,
#   "catalog":
#     {"descrshort":"CoS 14-15",
#     "descr":"Courses of Study 2014-2015",
#     "acalogCatalogId":22,
#     "version":
#       {"status":"COMPLETE"}
#     }
#   },
# "lastModifiedDttm":"2020-08-09T19:31:01-0400"
# }