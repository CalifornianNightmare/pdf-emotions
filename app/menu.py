from app.pdf.reader import read_pdf
from app.model.predict import predict

from simple_term_menu import TerminalMenu
from app.definitions import ROOT_DIR

def main_menu():
    options = ["Select a PDF", "Manual text input", "About", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        PDFselect()
    if menu_entry_index == 1:
        manual_input()
    if menu_entry_index == 2:
        about()
    if menu_entry_index == 3:
        print('Goodbye')

def PDFselect():
    filelist = [name for name in  (ROOT_DIR / 'files').glob("*.pdf")]
    options = [filename.stem + '.pdf' for filename in filelist]
    terminal_menu = TerminalMenu(options, title=f'Found {len(filelist)} files. Choose:')
    menu_entry_index = terminal_menu.show()
    
    filename = options[menu_entry_index]
    text = read_pdf(filename)
    label = predict(text)
    continue_question(f'The predicted emotion is: {label}')

def continue_question(text: str):
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(options, title=text + '\n\nContinue?')
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        main_menu()
    if menu_entry_index == 1:
        print('Goodbye')

def manual_input():
    text = input()
    label = predict(text)
    continue_question(f'The predicted emotion is: {label}')

def about():
    title = 'This app will predict one of the four basic emotions (anger, sadness, fear, joy) based on the text in the pdf file\n' \
    'You also have the option to enter text by hand\n' \
    'PDF files are taken out of /files/ folder\n' \
    'Installation steps are described in README.md\n'

    options = ["Okay"]
    terminal_menu = TerminalMenu(options, title=title)
    terminal_menu.show()
    
    main_menu()