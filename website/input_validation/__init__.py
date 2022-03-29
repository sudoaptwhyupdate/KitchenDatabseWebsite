# input validation module to figure out if all things inputted by the user
# are fine

class ValidateInput:
  
  # This is a simple input validation class
  # just to help clean up some of the code but can be used 
  # for other stuff as well
  
  # This is designed to be somewhat configureable
  # so that this code can be used in the future
  # such as item length, and other stuff
  
  def __init__(
      self, 
      type, 
      name="", 
      name_min=0,
      name_max=0,
      password="", 
      password_min=0, 
      password_max=0,
      item="", 
      item_min=0,
      item_max=0
  ):
    

      # please forgive me, the way this code look pains me too
      # but the only other way was unreadable to my eyes 
      # and this is clear enough
      # if there is a better way to write it please fix it
      #
      # number_of_attempts_fixing_it = 3
      
      self.type = type
      self.name = name
      self.name_min = name_min
      self.name_max = name_max
      self.password = password
      self.password_min = password_min
      self.password_max = password_max
      self.item = item
      self.item_min = item_min
      self.item_max = item_max
      
      if self.type == self.name:
        self._len_check(self.name, self.name_min, self.name_max)
      if self.type == self.password:
        self._len_check(self.password, self.password_min, self.password_max)
      if self.type == self.item:
        self._len_check(self.item, self.item_min, self.item_max)
  
  @classmethod
  def _len_check(self, name, minimum, max):
      if len(name) >= max or name <= minimum:
        return "error"
      else:
        return "success"
