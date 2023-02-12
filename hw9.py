def input_error(func):           # декоратор
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Sorry, give me name and phone please.'
        except KeyError:
            return 'Give me comand please.'
        except ValueError:
            return 'Try again'
    return wrapper


@input_error
def greeting(*args):                  # приветствие
    return 'How can I help you?'


contacts = {}


@input_error
def add(*args):            # додаємо ім'я та номер тел, записуємо в контакти
    name = args[0]
    phone = args[1]
    contacts.update({name: phone})
    return 'These name and phone add to contacts'


@input_error
def change(*args):          # зміна номера телефону
    if args[0] in contacts:
        contacts[args[0]] = args[1]
        return f'New contacts {contacts}'
    else:
        return "This name is not in contacts"


@input_error
def phone(*args):            # показати номер телефону
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return 'This name is not in contacts'


@input_error
def show_all(*args):              # показати всі контакти
    return f'Contacts: {contacts}'


COMMANDS = {
    greeting: "hello",
    add: 'add',
    change: 'change',
    phone: 'phone',
    show_all: 'show all',
}


def command_parser(user_input: str):
    for command, key_words in COMMANDS.items():

        if user_input.startswith(key_words):
            return command, user_input.replace(key_words, '').strip().split(' ')

    return None, None


def main():
    while True:
        user = input(">>> ")
        user_input = user.casefold()
        if user_input == ".":
            break
        if user_input.startswith(('good bye', 'exit', 'close')):
            print("Good bay!")
            break
        command, data = command_parser(user_input)

        if not command:
            print('Sorry, unknown command.')
        else:
            print(command(*data))


if __name__ == '__main__':
    main()
