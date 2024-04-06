from pdf2image import convert_from_path
import os

def pdf2png(pdf_path, png_path):
    images = convert_from_path(pdf_path, use_cropbox=True)
    for i, image in enumerate(images):
        image.save(png_path, 'PNG')

def main():
    for path in os.listdir("./images/"):
        if path.endswith(".pdf") and not os.path.exists("./images/" + path[:-4] + ".png"):
            pdf2png("./images/" + path, "./images/" + path.replace(".pdf", ".png"))

if __name__ == "__main__":
    main()