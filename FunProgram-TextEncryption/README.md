# Python Programming
## Specification

### Outline

Your task is to write functions to code and decode a secret missage into a .bmp file, as described in lectures.

## Function Specification

You need to write two functions:

```python
code_message( bmp_infile, bmp_outfile, message_file, p, q )
```

> bmp_infile is a string like 'flower.bmp'
>
> bmp_outfile is a string like 'flower_msg.bmp'
>
> message_file is a string like 'message.txt'
>
> p is an integer like 1
>
> q is an integer like 1

The filenames will be assumed to be in the current working directory. bmp_infile will be read, the message in bmp_outfile will be added to it, the modified image will be written to bmp_outfile.

```python
decode_message( bmp_infile, message_outfile, p, q )
```

> bmp_infile is a string like 'flower_msg.bmp'
>
> message_outfile is a string like 'secret_message.txt'
>
> p is an integer like 1
>
> q is an integer like 1

bmp_infile will be read, the text message will be extracted from it, the message will be written to
message_outfile.

I will provide code so these functions can be called from the command line.

## Project Steps

Here is a way of dividing each function into separate steps, each a separate function.

### code_message()

`read_image_file()`

- Read in the image as a binary file

- Put in a bytearray

- Close the image file

`read_message_file()`

- Read in the secret text

- Extract the letters of the text

- Extract the individual bits from the letters

`add_text_bits()`

- Use values of p, q specified

- Step through relevant bytes in the image file, adding the text bits

`save_image_file()`

- Write the modified image file

- Close the file

### decode_message()

`read_image_file() (same function as above)`

- Read in the image with secret message as a binary file

- Put in a bytearray

- Close the image file

`extract_text_bits()`

- Set p=1 q=2

- Step through relevant bytes in the file bytearray, extracting the text bits

`assemble_text_bits()`

- Put the text bits together into bytes

- Convert the bytes (numbers) into characters in a string

`save_message_file()`

- Open a text file and write the character string

- Close the file

If you are unsure, follow this structure and write these functions.

## Assessment

You need to submit the program to Moodle. We will also test your program in the lab.

As soon as your program is ready, you can demonstrate it during any lab session.

## Submission Deadline and Procedure

Set on Friday 18th October, NWU Week 8

Due on 21h59 Friday 1st November, NWU Week 10

Submit one .py file containing your program to Moodle. If you go to the appropriate week on Moodle you will see a file submission label called ‘Project 1’. Click on that and you can submit your file.

If your NWU ID number is 1234567890 then the file you submit should be called a1234567890.py . Note that we have added 'a' to the start of the filename because a filename
starting with a digit cannot be imported into Python.

### This is how we will check the format of the entire program:

- 5%: Comment at the start has the correct layout, has the correct filename and explains what
  program does.

- 5%: Comment 'To run this program' has been edited to show exactly how to run the program.

- 5%: Each function starts with a comment, exactly as shown in blank2.py etc.

- 5%: Four spaces are used for indentation throughout, no tabs are used at all.

- 5%: No line longer than 79 characters

## Extra Points

### Bit order

The bit order in the above is not specified. Suppose the message is ‘d’, i.e. code 100 or 0b01100100.

Bits should be added left-to-write to the .bmp file. Assuming header 54, p=1, q=2:
0   should be stored in .bmp byte   55
1                                                            57
1                                                            59
0                                                            61
0                                                            63
1                                                            65
0                                                            67
0                                                            69

### Binary arithmetic

Numbers in Python always appear in base 10. However, a base 10 number can be used in binary bit operations without conversion:

> x = 23 # 0b10111
>
> y = x & 0b00000001
>
> y # value is 1

## Further Work you can Do

### Note

If you have finished the above steps, you can try some more steps as shown below. These are not part of the official project marks, but if you are interested, you can try them.

### End of the Message

The project did not specify how to know when you have reached the end of the message. There are two main solutions to this:

Probably the easiest and best is to encode the length of the message in bytes at the start, in the first two bytes. For example, suppose your message is ‘hello’ - 5 Ascii characters, i.e. 5 bytes, 40 bits.

You can convert 5 into a two-byte hex number 05. You encode this in 16 bits at the start of the
message. So now our message is 56 bytes long.

When you decode the message, you extract the length from the first 16 bits and then use it to extract the remaining character.

The second suggestion which students have made is to put some special sequence of bytes at the end of the message. e.g. two bytes which are entirely ones. This means adding 16 bits to the end of the message, all ones. If you detect this, you know you are at the end of the message.

We also provide a longer message for you to test with. Can you see the connection between the
message and the flower?

### Chinese Text

The example message was in English. What about a Chinese message? Students have made suggestions about this as well. For example, you could encode it in UCS2 - two bytes per character.

Then encode it in pairs of bytes (16 bits) as before.

Python can convert to UCS2 - see the lecture notes.

Or, you can convert it to UTF-8 and send as a sequence of bytes. The lecture notes also say how to do this.

### Is there a Message

Another problem is we do not know if there is a message or not. Suppose we have a blank flower with no message; we can still decode, except we get a sequence of random characters.

There are two ways:

- Extract the bits, make into bytes and check that they are all ASCII characters (seven bit).

- look at the proportion of bits in the decoded message which are one (‘1’) relative to the proportion of bits which are zero (‘0’). If this proportion is less than 0.5, it is a valid message. Otherwise, it is random data. You can check on the internet about this method if you are interested.