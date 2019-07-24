import mathematics.ceil

##------------------------------------------------------------------------------
# Function: Apply_Indentation_Rule (input text)
def apply_indentation_rule(input_text):
    output_text = ''
#   for every line in output text:
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
                output_text = output_text + '\t'

            

    return output_text