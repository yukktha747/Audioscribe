import pyttsx3
from PyPDF2 import PdfReader
import threading
import time

stop_reading = False

def check_for_stop():
    global stop_reading
    while not stop_reading:
        user_input = input("Press Enter to stop reading: ")
        if user_input == "":
            stop_reading = True

def read_pdf(file_path):
    global stop_reading
    try:
        print(f"Opening file: {file_path}")
        book = open(file_path, 'rb')
        pdfReader = PdfReader(book)
        pages = len(pdfReader.pages)
        print(f"Number of pages: {pages}")
        speaker = pyttsx3.init()

        # Start a thread to listen for user input
        stop_thread = threading.Thread(target=check_for_stop)
        stop_thread.daemon = True
        stop_thread.start()

        for num in range(1, pages):
            if stop_reading:
                print("Stopping the reading.")
                break
            
            page = pdfReader.pages[num]
            text = page.extract_text()
            texts=text.split()
            print(f"Reading page {num + 1}: {text[:100]}...")
            for chunk in texts:
                if stop_reading:
                    break
                speaker.say(chunk)
                speaker.runAndWait()
                

        book.close()
        print("Finished reading PDF.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the correct path to your PDF file
pdf_file_path = 'yukkthas (1).pdf'
print("Press Enter at any time to stop reading.")
read_pdf(pdf_file_path)