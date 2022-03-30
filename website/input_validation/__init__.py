# input validation module to figure out if all things inputted by the user
# are fine

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
    

      # please forgive me, the way this code look pains me too
      # but the only other way was unreadable to my eyes 
      # and this is clear enough
      # if there is a better way to write it please fix it
      #
      # number_of_attempts_fixing_it = 4
      
      self.data_type = data_type
      self.name = name
      self.name_min = name_min
      self.name_max = name_max

  @classmethod
  def _len_check(self, name, min, max):
      if len(name) >= max or name <= min:
        return "error"
      else:
        return "success"

  @classmethod
  def _type_check(self, data_type):
    pass
