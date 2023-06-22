phone_book = []
path = 'phones.txt'
from contact import Contact

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment = contact.strip().split(':')
        phone_book.append(Contact(user_id, name, phone, comment))
    # print(phone_book)

def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        for cont in phone_book:
            file.write(f"{cont.uid}:{cont.name}:{cont.phone}:{cont.comment}\n")



def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(contact.uid)
        uid=max(uid_list)
        uid=int(uid)+1
    return uid


def add_contact(name, phone, comment):
    uid = check_id()
    phone_book.append(Contact(uid, name, phone, comment))


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        if word.lower() in contact.name.lower():
            result.append(contact)
        elif word.lower() in contact.phone.lower():
            result.append(contact)
        elif word.lower() in contact.comment.lower():
            result.append(contact)
    return result


def change(index: int, new: dict[str, str]):
    for contact in phone_book:
        if index == int(contact.uid):
            if new[0]!='': contact.name=new[0]
            if new[1]!='':contact.phone=new[1]
            if new[2]!='':contact.comment=new[2]


    # for key, field in new.items():
    #     if field != '':
    #         phone_book[index-1][key] = field




def delete_contact(index: int):
    phone_book.pop(index-1)
