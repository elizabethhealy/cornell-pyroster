import requests
import json
from util import *
from roster import Roster, roster_from_json
from group import Group, group_from_json
from academic_level import AcademicLevel, academic_level_from_json
from class_level import ClassLevel, class_level_from_json
from subject import Subject, subject_from_json

##Constants
FORMAT = ".json"
API_BASE = "https://classes.cornell.edu/api/"
VERSION = str(2.0)
BASE_URL = API_BASE+VERSION+"/"


def available_rosters():
  """
  Get all available rosters

  Returns: [Roster] -- a list of Roster instances
  """
  #returns list of roster objects
  return simple_parse("config/rosters",
                      "rosters",
                      roster_from_json)

def academic_levels(roster):
  """
  Get all academic levels for a particular roster

  Parameters:
  roster <str> -- a string representing the term and year of desired roster
  ex: "FA19"

  Returns: 
  [AcademicLevel] -- a list of AcademicLevel instances
  """
  #returns list of academic level objects
  return simple_parse("config/acadCareers",
                      "acadCareers",
                      academic_level_from_json,
                      roster)

def academic_groups(roster):
  """
  Get all academic groups for a particular roster

  Parameters:
  roster <str> -- a string representing the term and year of desired roster
  ex: "FA19"

  Returns: 
  [Group] -- a list of Group instances
  """
  #returns a list of academic group objects
  return simple_parse("config/acadGroups",
                      "acadGroups",
                      group_from_json,
                      roster)

def class_levels(roster):
  """
  Get all class levels for a particular roster

  Parameters:
  roster <str> -- a string representing the term and year of desired roster
  ex: "FA19"

  Returns: 
  [ClassLevel] -- a list of ClassLevel instances
  """
  #returns a list of class level objects
  return simple_parse("config/classLevels",
                      "classLevels",
                      class_level_from_json,
                      roster)

def subjects(roster):
  """
  Get all subjects for a particular roster

  Parameters:
  roster <str> -- a string representing the term and year of desired roster
  ex: "FA19"

  Returns: 
  [Subject] -- a list of Subject instances
  """
  #returns a list of subjects
  return simple_parse("config/subjects",
                      "subjects",
                      subject_from_json,
                      roster)


