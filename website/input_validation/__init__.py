# input validation module to figure out if all things inputted by the user
# are fine

from flask import Flask


class ValidateInput:
  
  # This is a simple input validation class
  # just to help clean up some of the code but can be used 
  # for other stuff as well
  
  # This is designed to be somewhat configureable
  # so that this code can be used in the future
  # such as item length, data type

  def __init__(
      self,
      data_type="int", 
      name="", 
      name_min=0,
      name_max=0,
  ):
      
      self.data_type = data_type
      self.name = name
      self.name_min = name_min
      self.name_max = name_max

  def __error_message_generator(self, bad_data, length=0, minimum=0, exceeds=0, type=""):
    
    if length == 0 and exceeds == 0:
      type_problem = True
    else: 
      type_problem = False
    
    bounds_error_message = f"""
    
    There was a problem detected in the input given:
    
      {bad_data}
    
    This input either exceeds or does not meet the minimum length requested
    by developer.
    
    Given Data: {bad_data}
    Data Length: {length}
    Length Requested: needs to be less than {exceeds} but more than {minimum} 
    
    """
    
    type_error_message = f"""
    
    There was a problem detected in the input given 

      {bad_data}
    
    This input does not meet the requirements (data_type) requested
    by the developer.
    
    Given Data: {bad_data}
    Data Type Given: {type(bad_data)}
    Data Type Requested: {type}
    
    """
    
    if type_problem == False:
      return bounds_error_message
    if type_problem == True:
      return type_error_message
      
  
  @classmethod
  def _len_check(self, name, min, max):
      if len(name) >= max or name <= min:
        self.__error_message_generator(name, len(name), min, max)
        return "error"
      else:
        return "success"

  @classmethod
  def _type_check(self, data_type):
    pass
