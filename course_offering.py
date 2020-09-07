import json


"""
Represents a course

Attributes
----------
key: str
    a shortened description representing the subject ex. "AEM"
description: str
    a description of the subject
"""
class CourseOffering:
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

# {"strm":2573,
# "crseId":352045,
# "crseOfferNbr":1,
# "subject":"MATH",
# "catalogNbr":"1011",
# "titleShort":"Academic Support for Math 1110",
# "titleLong":"Academic Support for MATH 1110",
# "enrollGroups":[
#   {
#     "classSections":
#     [
#       {
#         "ssrComponent":"TA",
#         "ssrComponentLong":"TA\/Tutor Group",
#         "section":"651",
#         "classNbr":6556,
#         "meetings":
#           [
#             {
#               "classMtgNbr":1,
#               "timeStart":"04:30PM",
#               "timeEnd":"06:00PM",
#               "startDt":"08\/26\/2014",
#               "endDt":"12\/05\/2014",
#               "instructors":
#                 [
#                   {
#                     "instrAssignSeq":4,
#                     "netid":"maj29",
#                     "firstName":"Mark",
#                     "middleName":"",
#                     "lastName":"Jauquet"
#                   }
#                 ],
#               "pattern":"W",
#               "facilityDescr":"Malott Hall 251",
#               "bldgDescr":"Malott Hall",
#               "facilityDescrshort":"MLT251",
#               "meetingTopicDescription":""
#             }
#           ],
#         "notes":[],
#         "campus":"MAIN",
#         "campusDescr":"Ithaca",
#         "location":"ITH",
#         "locationDescr":"Ithaca, NY (Main Campus)",
#         "startDt":"08\/26\/2014",
#         "endDt":"12\/05\/2014",
#         "addConsent":"N",
#         "addConsentDescr":"No Special Consent Required",
#         "isComponentGraded":true,
#         "instructionMode":null,
#         "instrModeDescrshort":null,
#         "instrModeDescr":null,
#         "topicDescription":""
#       }
#     ],
#   "unitsMinimum":1,
#   "unitsMaximum":1,
#   "componentsOptional":[],
#   "componentsRequired":["TA"],
#   "gradingBasis":"SUS",
#   "gradingBasisShort":"Sat\/UnSat",
#   "gradingBasisLong":"Satisfactory - Unsatisfactory",
#   "simpleCombinations":[],
#   "sessionCode":"1",
#   "sessionBeginDt":"08\/26\/2014",
#   "sessionEndDt":"12\/05\/2014",
#   "sessionLong":"Regular Academic Session"
#   },
# {
#   "classSections":
#   [
#     {"ssrComponent":"TA",
#     "ssrComponentLong":"TA\/Tutor Group",
#     "section":"652",
#     "classNbr":6797,
#     "meetings":
#     [
#       {
#         "classMtgNbr":1,
#         "timeStart":"02:55PM",
#         "timeEnd":"04:25PM",
#         "startDt":"08\/26\/2014",
#         "endDt":"12\/05\/2014",
#         "instructors":
#         [
#           {
#             "instrAssignSeq":4,
#             "netid":"maj29",
#             "firstName":"Mark",
#             "middleName":"",
#             "lastName":"Jauquet"
#             }
#         ],
#         "pattern":"F",
#         "facilityDescr":"Malott Hall 251",
#         "bldgDescr":"Malott Hall",
#         "facilityDescrshort":"MLT251",
#         "meetingTopicDescription":""
#         }
#       ],
#     "notes":[],
#     "campus":"MAIN",
#     "campusDescr":"Ithaca",
#     "location":"ITH",
#     "locationDescr":"Ithaca, NY (Main Campus)",
#     "startDt":"08\/26\/2014",
#     "endDt":"12\/05\/2014",
#     "addConsent":"N",
#     "addConsentDescr":"No Special Consent Required",
#     "isComponentGraded":true,
#     "instructionMode":null,
#     "instrModeDescrshort":null,
#     "instrModeDescr":null,
#     "topicDescription":""
#     }
#   ],
#   "unitsMinimum":1,
#   "unitsMaximum":1,
#   "componentsOptional":[],
#   "componentsRequired":["TA"],
#   "gradingBasis":"SUS",
#   "gradingBasisShort":"Sat\/UnSat",
#   "gradingBasisLong":"Satisfactory - Unsatisfactory",
#   "simpleCombinations":[],
#   "sessionCode":"1",
#   "sessionBeginDt":"08\/26\/2014",
#   "sessionEndDt":"12\/05\/2014",
#   "sessionLong":"Regular Academic Session"
#   }
# ],
# "description":"Reviews material presented in MATH 1110\u00a0lectures, provides problem-solving techniques and tips as well as prelim review. Provides further instruction for students who need reinforcement. Not a substitute for attending MATH 1110\u00a0lectures.",
# "catalogBreadth":"",
# "catalogDistr":"",
# "catalogLang":"",
# "catalogForbiddenOverlaps":"",
# "catalogWhenOffered":"Fall, spring.",
# "catalogComments":"Students should contact their college for the most up-to-date information regarding if and how credits for this course will count toward graduation and\/or be considered regarding academic standing.",
# "catalogPrereqCoreq":"",
# "catalogFee":"",
# "catalogSatisfiesReq":"",
# "catalogPermission":"",
# "catalogCourseSubfield":"",
# "catalogOutcomes":null,
# "acadCareer":"UG",
# "acadGroup":"AS"
# }