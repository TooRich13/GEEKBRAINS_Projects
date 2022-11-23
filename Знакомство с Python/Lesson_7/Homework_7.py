import phbook

def try_phonebook():
    
    book = phbook.Phonebook()
    book.print_book()

    book.add_contact()
    book.print_book()

    book.add_number()
    book.print_book()

    book.del_contact()
    book.print_book()

    book.del_number()
    book.print_book()

    book.export_csv("exp_db.csv")
    book.export_txt("exp_db.txt")

    book.clr_db()
    book.print_book()

    book.import_csv("exp_db.csv")
    book.print_book()

try_phonebook()
    