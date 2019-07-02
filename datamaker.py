import os

input="someFile.pdf"
output="out.txt"
os.system(("ps2ascii %s %s") %( input , output))
#import textract
#text = textract.process("path/to/file.extension")