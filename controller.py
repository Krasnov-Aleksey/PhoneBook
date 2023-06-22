from view import menu, show_contacts, print_message, input_contacts, input_return
import model
from view import text


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                model.save_file()
                print_message(text.save_successful)
            case 3:
                show_contacts(model.phone_book)
            case 4:
                name, phone, comment = input_contacts(text.input_new_contact)
                model.add_contact(name, phone, comment)
                print_message(text.contact_saved(name))
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contacts(text.input_change_contact)
                model.change(int(index), new)
                print_message(text.contact_changed())
            case 7:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.delete_index)
                model.delete_contact(int(index))
                print_message(text.delete_contact)
            case 8:
                break
