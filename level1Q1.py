#lex_auth_0127135739583692801137

def add_string(str1):
 if len(str1) < 3:
  return str1
 elif str1[-3:] == 'ing':
  return str1 + 'ly'
 else:
  return str1 + 'ing'
  
if __name__ == '__main__':
  str1="com"
  print(add_string(str1))