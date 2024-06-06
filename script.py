# Python Script for converting several images to a single pdf file

# Importing Modules 
import os
from PIL import Image
from fpdf import FPDF 
pdf = FPDF()

# Defining variable for images and scanning root directory 
images = []
files = os.listdir("./") 

# Check if files are images (jpg / png), if they are, add them to images list, if not, quit...
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        images.append(file) 
        print(f"Scanned {len(images)} files from {len(files)}")
    elif len(images) == 0 and file == files[len(files)-1]: 
        print(f"No Suitable images found") 
        quit()
    else: 
        continue

# Take user input for the name of the pdf file to be saved... 
pdf_file_name = input("Name the pdf file you want to save (ignore .pdf): ") 

# go through images, and then add them to the pdf...
for image in images: 
    # Find out dimensions of image 
    img = Image.open(image)
    img_width, img_height = img.size

    # setting page orientation variable
    orientation = "P" if img_height >> img_width else "L"

    # setting page dimension variable 
    page_dimensions = (img_width, img_height) if orientation == "P" else (img_height, img_width) 

    # Add a new page to the document
    pdf.add_page(
        orientation = orientation, 
        format = page_dimensions 
        # same = False
    )

    # Put the image in the current page 
    pdf.image(
        name = image,  
        x = 0, 
        y = 0, 
        w = img_width, 
        h = img_height 
    )

# Save the pdf file 
pdf.output(name = f"{pdf_file_name}.pdf")

# Print closing message 
print("PDF Conversion Successful...")
