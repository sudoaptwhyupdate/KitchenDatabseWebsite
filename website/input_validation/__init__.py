# input validation module to figure out if all things inputted by the user
# are fine

class ValidateInput:
  
  # This is a simple input validation class
  # just to help clean up some of the code but can be used 
  # for other stuff as well
  
  # This is designed to be somewhat configureable
  # so that this code can be used in the future
  # such as item length, data type

  def __init__(self):
    pass
  
      
  @classmethod
  def len_check(self, name, min=0, max=0):
      if len(name) >= max:
        return "error"
      elif len(name) <= min:
        return "error"
      else:
        return "success"

  @classmethod
  def type_check(self, data, data_type):
    try:
      data_type(data)
      return "success"
    except ValueError:
      return "error"
  
  def email_check(self, email):
    # checks that the input entered is an email
    # is this is a wonky way, yes, but it works
    email_list = []
    for characters in email:
      email_list.append(characters)
    
    AtSignBool = False
    PeriodBool = False
    for items in email_list:
      if email_list[items] == "@":
        AtSignBool = True
      else: pass
    
    for items in email_list:
      if email_list[items] == ".":
        PeriodBool = True
      else: pass
    
    if AtSignBool == True and PeriodBool == True:
      return "success"