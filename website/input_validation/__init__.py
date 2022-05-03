# input validation module to figure out if all things inputted by the user
# are fine

import string

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
        self.__check_password()
      elif security_level == "medium":
        self.alphabetical_characters = 16
        self.numbers = 4
        self.special_characters = 4
        self.__check_password()
      elif security_level == "high":
        self.alphabetical_characters = 32
        self.numbers = 8
        self.special_characters = 8
        self.__check_password()
      elif security_level == "very_high":
        self.alphabetical_characters = 64
        self.numbers = 16
        self.special_characters = 16
        self.__check_password()
      else:
        self.alphabetical_characters = 8
        self.numbers = 2
        self.special_characters = 2
        self.__check_password()
    
  def __check_password(self):
    """checks inputted password against criteria

    Returns:
        boolean: returns True or False, whether or not the function went well
    """
    password_list = []
    for character in self.password:
      password_list.append(character)
    
    alpha = 0
    num = 0 
    spec = 0
    
    for item in password_list:
      if item in string.ascii_lowercase or string.ascii_uppercase:
        alpha += 1
      if item in string.digits:
        num += 1
      if item in string.punctuation:
        spec += 1
    
    if (alpha == self.alphabetical_characters and num == self.numbers and 
        spec == self.special_characters):
      return True
    else:
      return False


class ValidateInput:
  
  # This is a simple input validation class
  # just to help clean up some of the code but can be used 
  # for other stuff as well
  
  # This is designed to be somewhat configureable`2`
  # so that this code can be used in the future
  # such as item length, data type

  def __init__(self):
    pass
  

  def len_check(name, min = 0, max = 0):
    # check the length of a given string
    # name = thing you're checking
    # min, min length wanted
    # max = max length wanted
      if len(name) >= max:
        return False
      elif len(name) <= min:
        return False
      else:
        return True

  def type_check(data, data_type):
    # checks the type of a given variable against what is required
    
    # data = thing you're checking
    # data_type = type you're checking for
    
    # make sure you pass in a type like **int** into there, and not somthing like "number"
    # other wise it won't work
    try:
      data_type(data)
      return True
    except ValueError:
      return False
  
  def email_check(email):
    # checks that the input entered is an email
    # is this is a wonky way, yes, but it works
    email_list = []
    for characters in email:
      email_list.append(characters)
    
    AtSignBool = False
    PeriodBool = False
    for items in email_list:
      if items == "@":
        AtSignBool = True
      else: pass
    
    for items in email_list:
      if items == ".":
        PeriodBool = True
      else: pass
    
    if AtSignBool == True and PeriodBool == True:
      return True

  def secure_password_check(password, security_level):
    # this method is here just for ease of use, but using the
    # class directly is preferred
    PasswordCheck(password, security_level)