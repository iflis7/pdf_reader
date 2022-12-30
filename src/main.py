# Import necessary libraries:
import pyttsx3
import PyPDF2

# Initialize the text-to-speech engine using "pyttsx3".
engine = pyttsx3.init('dummy')

# Open the PDF file using "PyPDF2".
book = open('books/think_and_grow_rich.pdf', 'rb')
with open('books/think_and_grow_rich.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)

# Extract the text from each page of the PDF using the getPage()
# and extractText() methods of the PdfFileReader object.
pages = []
for page in range(len(pdf_reader.pages)):
    pages.append(pdf_reader.getPage(page).extractText())

# Use the say() method of the pyttsx3 engine to read each page of the PDF out loud.

for page in pages:
    engine.say(page)
engine.runAndWait()
