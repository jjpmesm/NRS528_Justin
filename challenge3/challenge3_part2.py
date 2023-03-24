# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv, and does something to them. The rules:
#
# Minimum of three arguments to be used.
# You must do something simple in 15 lines or less within the Python file.
# Print or file generated output should be produced.
import sys

Argument_1 = sys.argv[1]
Argument_2 = sys.argv[2]
Argument_3 = sys.argv[3]
Argument_4 = sys.argv[4]

argument_list = [Argument_1, Argument_2, Argument_3, Argument_4]

for i in argument_list:
    print(i)