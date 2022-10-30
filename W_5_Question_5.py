# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

# Write a program that stores the sentence. “ I am learning to code
# in Python ” in a variable (there are six spaces at the start and
# six spaces at the end of the sentence). The program will display
# the sentence all in upper case with no extra spaces at the start
# or end of the sentence.

v_one = '      I am learning to code in Python      '
print('variable one is: ', '"', v_one, '"')
v_one_upper = v_one.upper()
v_one_left_strip = v_one.lstrip()
v_one_right_strip = v_one.rstrip()
v_one_ls_applied = v_one_left_strip
v_one_ls_rs_applied = v_one_ls_applied.rstrip()
v_one_ls_rs_uc_applied = v_one_ls_rs_applied.upper()
v_one_formatted = v_one_ls_rs_uc_applied
print('Variable one formatted: ')
print('When the left and right spaces are stripped off and all')
print('characters are capitalised: ', '"', v_one_formatted, '"')
