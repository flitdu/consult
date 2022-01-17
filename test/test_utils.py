from sys import argv
from PIL import Image

if len(argv) !=4:
    exit("usage: python resize.py n file outfile")

n = int(argv[1])
infile = argv[2]
outfile = argv[3]

inimage = Image.open(infile)
width, height = inimage.size
outimage = inimage.resize((width * n, height * n))

outimage.save(outfile)
