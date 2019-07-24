import sys
from apply_indentation_rule import apply_indentation_rule
from apply_bracket_rule import apply_bracket_rule
from apply_parenthesis_rule import apply_parenthesis_rule
from apply_for_loop_rule import apply_for_loop_rule

##------------------------------------------------------------------------------
# Function: Main ()
def main ():
#   get input file & text
    input_file = input_file_from_cmd()
    input_text = input_file.read()

#   create output file & text & initialize to input text
    output_file = open('reformatted_' + input_file.name, 'w+')
    output_text = input_text

#   apply rules
    output_text = apply_indentation_rule(output_text)
    output_text = apply_bracket_rule(output_text)
    output_text = apply_parenthesis_rule(output_text)
    output_text = apply_for_loop_rule(output_text)    

#   set output file to output text
    output_file.write(output_text)

#   save and close all files
    input_file.close()
    output_file.close()
    return 0


##------------------------------------------------------------------------------
# Function: Input_File ()
def input_file_from_cmd ():
#   get file from command line
    filename = sys.argv[1]
    file = open(filename)
    return file

if __name__ == '__main__':
    main()