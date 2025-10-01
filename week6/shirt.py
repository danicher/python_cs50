import sys
from PIL import Image, ImageOps

def main():
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    elif not (is_image(sys.argv[1]) and is_image(sys.argv[2])):
        sys.exit("Invalid input")
    elif not (is_same_extension(sys.argv[1], sys.argv[2])):
        sys.exit("Input and output have different extensions")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    try:
        shirt = Image.open("shirt.png")
        image = Image.open(infile)
    except FileNotFoundError:
        sys.exit("File not found")

    image = ImageOps.fit(image, shirt.size)

    image.paste(shirt, shirt)

    image.save(outfile)

def is_image(file):
    return (file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"))

def is_same_extension(file1, file2):
    ext1 = file1.split(".")
    ext2 = file2.split(".")
    return (ext1[1] == ext2[1])

if __name__ == "__main__":
    main()