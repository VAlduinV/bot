def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return 'Error: Enter valid name and phone number.'

    return wrapper


@input_error
def add(name, phone):
    contacts[name] = phone
    return f'{name} added to contacts.'


@input_error
def change(name, phone):
    contacts[name] = phone
    return f'{name} phone number is changed.'


@input_error
def phone(name):
    return f'{name}\'s phone number is {contacts[name]}.'


def show_all():
    if len(contacts) == 0:
        return 'Empty contact book.'

    contact_list = ''
    for name, phone in contacts.items():
        contact_list += f'{name} : {phone}\n'
    return contact_list


contacts = {}

options = {
    'hello': 'How can I help you?',
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'goodbye': 'Goodbye!',
    'close': 'Goodbye!',
    'exit': 'Goodbye!'
}


def main():
    while True:
        user_input = input('Enter command: ')
        user_input = user_input.strip().lower()

        if user_input in options:
            if user_input == 'add':
                name, phone = input('Enter name and phone number: ').split()
                print(options[user_input](name, phone))
            elif user_input == 'change':
                name, phone = input('Enter name and new phone number: ').split()
                print(options[user_input](name, phone))
            elif user_input == 'phone':
                name = input('Enter name: ')
                print(options[user_input](name))
            else:
                print(options[user_input])
        elif user_input == '.':
            break
        else:
            print('Error: Command not found.')


if __name__ == '__main__':
    main()
