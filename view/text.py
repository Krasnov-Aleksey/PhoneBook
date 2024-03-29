main_menu = '''Главное меню
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Создать новый контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
'''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите от 1 до 8'
boor_error = 'Телефонная книга пуста или файл не открыт'
open_successful = 'Телефонная книга успешна открыта'
input_new_contact = 'Введите данные нового контакта '
new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите комментарий: ']
search_word = 'Введите искомый элемент '
# input_change_contact = 'Введите данные нового контакта'
input_index = 'Введите индекс изменяемого контакта '
input_change_contact = 'Введите данные изменяемого контакта или Enter чтоб оставить без изменений '
save_successful = 'Телефонная книга успешна записана'
delete_index = 'Введите индекс удаляемого элемента '
delete_contact = 'Контакт удален'


def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'


def contact_changed():
    return f'Контакт успешно изменен'


def contact_delete(name: str):
    return f'Контакт {name} успешно удален'
