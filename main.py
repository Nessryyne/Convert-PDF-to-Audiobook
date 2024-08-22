import PyPDF2
import pyttsx3
from tkinter import Tk, filedialog


def pdf_to_speech(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    speaker = pyttsx3.init()

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            speaker.say(text)
            speaker.runAndWait()


if __name__ == "__main__":
    Tk().withdraw()
    pdf_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

    if pdf_path:
        pdf_to_speech(pdf_path)
    else:
        print("No File Selected")
