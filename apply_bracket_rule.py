##------------------------------------------------------------------------------
# Function: Apply_Brackets_Rule (input text)
def apply_bracket_rule (input_text):
    output_text = ''
#   for every line in input text:
    for line in input_text.splitlines():
#       if there is a bracket:
        if (input_text.find('\{') >= 0):
#           if it has non-whitespace characters before it:
            if (line[:input_text.find('\{')] ):
#               put it on a new line after the current line
                pass
#           get number of indentations from line above
#           if it does not have the correct number of indentations:
#               add the correct number of indentations
#   return output text
    return  input_text+' bracket'

# Assumtions:
#   1. Apply_Indentation_Rule has already been invoked on the input

# TESTING FOR COMMIT