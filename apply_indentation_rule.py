import math

##------------------------------------------------------------------------------
# Function: Apply_Indentation_Rule (input text)
def apply_indentation_rule(input_text):
    output_text = ''
#   for every line in input text:
    for line in input_text.splitlines():
#       check beginning of line for indentation
#       if indentation is using spaces
        if (line[0] == ' '):
            # count the number of spaces
            num_spaces = 0
            while(line[num_spaces] == ' '):
                num_spaces += 1
            # add tabs to output_text
            num_tabs = math.ceil(num_spaces / 4.0)
            for tab in range(num_tabs):
                output_text += '\t'
            # add the rest of the line to output_text
            output_text += line[num_spaces:] + '\n'
        else:
            output_text += line + '\n'
    return output_text