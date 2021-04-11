"""***************************************************************************

                               project1_blank.py

This is a blank program which shows the format to use and also includes some
example functions so you can see the overall structure.

***************************************************************************"""

"""
To run this program, start python and then type:
from blank2 import *
my_function1()
my_function2()

To make this into a program, do the following:
1. Update the box comment with the name of the program. Change the summary in
   the box to say what the program does.
2. Update the 'import' line above - how do you import your program and run
   it?
3. Add some functions at the bottom following exactly the format and style of
   my_function1() and my_function2()
4. Delete my_function1() and my_function2().
5. Finally, delete these comments 1-5.
"""

# We need library sys for command-line processing at the bottom.
import sys

"""----------------------------------------------------------------------------

This function when called accepts a number from the user and then prints out
the square of that number. It does not return a value. The number can be either
an int or a float.
"""

def my_function1():

    print( 'Enter a number and I will square it:' )
    x = float( input() )
    print( 'The square of %f is %f' % ( x, x * x ) )

"""----------------------------------------------------------------------------

This function takes as argument a number (either float or int) and returns as
result the square of that number.
"""

def my_function2( x ):

    return( x * x )

"""----------------------------------------------------------------------------

This function takes a .bmp file bmp_infile, a message file message_file, and
values of integers p and q. It encodes the message in the .bmp using p and q,
and writes the modified .bmp to bmp_outfile.

YOU NEED TO WRITE THIS FUNCTION WHICH SHOULD CALL OTHER FUNCTIONS AS REQUIRED.
YOU CAN USE CLASSES IF YOU WISH, BUT IT IS NOT COMPULSORY.
"""

def code_message( bmp_infile, bmp_outfile, message_file, p, q ):

    print( 'bmp_infile is', bmp_infile )
    print( 'bmp_outfile is', bmp_outfile )
    print( 'message_file is', message_file )
    print( 'p is', p )
    print( 'q is', q )

"""----------------------------------------------------------------------------

This function takes a .bmp file bmp_infile, the name of an output message file
message_outfile, and the values of integers p and q. It extracts the message
from bmp_infile using p and q, and writes the message to the file
message_outfile.

YOU NEED TO WRITE THIS FUNCTION WHICH SHOULD CALL OTHER FUNCTIONS AS REQUIRED.
YOU CAN USE CLASSES IF YOU WISH, BUT IT IS NOT COMPULSORY.
"""

def decode_message( bmp_infile, message_outfile, p, q ):

    print( 'bmp_infile is', bmp_infile )
    print( 'message_outfile is', message_outfile )
    print( 'p is', p )
    print( 'q is', q )

"""----------------------------------------------------------------------------

NB: THE FOLLOWING CODE  IS PURELY FOR US TO CHECK YOUR CODE.  IT IS NOT PART OF
THE PROGRAM YOU ARE WRITING. DO NOT MODIFY OR ALTER THIS CODE IN ANY WAY.

Allow the program to be run from the command line. Assuming your filename is
a1234567890.py:

To CODE message in a .bmp, call it like this:
python a1234567890.py code flower.bmp flower2.bmp msg.txt 1 2

To DECODE message in a .bmp, call it like this:
python a1234567890.py decode flower2.bmp msg2.txt 1 2

"""

if __name__ == '__main__':

    try:

        if len( sys.argv ) == 7 and sys.argv[ 1 ] == 'code':
            # code
            code_message( sys.argv[ 2 ], sys.argv[ 3 ], sys.argv[ 4 ], 
                          int( sys.argv[ 5 ] ), int( sys.argv[ 6 ] ) )

        elif len( sys.argv ) == 6 and sys.argv[ 1 ] == 'decode':
            # decode
            decode_message( sys.argv[ 2 ], sys.argv[ 3 ], 
                            int( sys.argv[ 4 ] ), int( sys.argv[ 5 ] ) )

        else:
            print( 'Usage:' )
            print( 'python a1234567890.py code flower.bmp ', end = '' )
            print( 'flower2.bmp msg.txt 1 2' )
            print( 'python a1234567890.py decode flower2.bmp msg2.txt 1 2' )

    except:

        print( 'Usage:' )
        print( 'python a1234567890.py code flower.bmp ', end = '' )
        print( 'flower2.bmp msg.txt 1 2' )
        print( 'python a1234567890.py decode flower2.bmp msg2.txt 1 2' )
