##------------------------------------------------------------------------------
# Function: Apply_Brackets_Rule (input text)
def apply_bracket_rule (input_text):
    pass
#   copy input text into new variable output text
#   for every line in output text:
#       if there is a bracket:
#           check if it has anything before it
#           if it has non-whitespace characters before it:
#               put it on a new line after the current line
#           get number of indentations from line above
#           if it does not have the correct number of indentations:
#               add the correct number of indentations
#   return output text
    return  input_text+' bracket'

# Assumtions:
#   1. Apply_Indentation_Rule has already been invoked on the input