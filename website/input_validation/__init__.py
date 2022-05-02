# input validation module to figure out if all things inputted by the user
# are fine


class PasswordCheck:
    # check if a password is secure enough
    
    # arguments: 
    # passsword, the password being checked
    # security level: the security level you want the password checker to be
    # security level: levels to be passed are, none, minimum, medium, high, very_high
    
    # minimum security:
    # at least 8 alphabetical characters (2 have to be caps)
    # at least 2 numbers
    # at least 2 special characters
    
    # medium security:
    # at least 16 alphabetical characters (4 have to be caps)
    # at lease 4 numbers (scattered or together)
    # at lease 4 special characters
    
    # all other security levels after this will be multiplied by 2
    # to get to the next level
  def __init__(self, password, security_level) -> None:
      self.password = password
      self.alphabetical_characters = 0
      self.numbers = 0
      self.special_characters = 0
      
      if security_level == "none":
        # don't even know why, but for testing pourposes
        pass
      elif security_level == "minimum":
        self.alphabetical_characters = 8
        self.numbers = 2
        self.special_characters = 2
      elif security_level == "medium":
        self.alphabetical_characters = 16
        self.numbers = 4
        self.special_characters = 4
      elif security_level == "high":
        self.alphabetical_characters = 32
        self.numbers = 8
        self.special_characters = 8
      elif security_level == "very_high":
        self.alphabetical_characters = 64
        self.numbers = 16
        self.special_characters = 16
      else:
        pass
    
  def __check_password__(self):
    password_list = []
    for character in self.password:
      password_list.append(character)
    

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
    # check the length of a given string
    # name = thing you're checking
    # min, min length wanted
    # max = max length wanted
      if len(name) >= max:
        return "error"
      elif len(name) <= min:
        return "error"
      else:
        return "success"

  @classmethod
  def type_check(self, data, data_type):
    # checks the type of a given variable against what is required
    
    # data = thing you're checking
    # data_type = type you're checking for
    
    # make sure you pass in a type like **int** into there, and not somthing like "number"
    # other wise it won't work
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

  def secure_password_check(self, password, security_level):
    # this method is here just for ease of use, but using the
    # class directly is preferred
    PasswordCheck(password, security_level)