def triple(sentence):
#{
  # initialise the result string to empty
  result = ""

  # go through each letter
  for i in range(0, len(sentence)):
  #{
    # get the ith letter
    letter = sentence[i]
    
    # add letter 3 times to the result
    result = result + (letter * 3)
  #}

  return result
#}

# MAIN PROGRAM:
# ... type your code here ...
input_sentence = input("Enter a sentence: ")
print(f"Triple effect: {triple(input_sentence)}")
