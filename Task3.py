import datetime


def logger(some_func):
    log_str = ''

    def new_some_func(*args, **kwargs):
        log_path = 'some_log3.txt'
        if kwargs.get('log'):
            log_path = kwargs['log']
        with open(log_path, 'a', encoding='utf-8') as logfile:
            nonlocal log_str
            log_str = f'{datetime.datetime.now()} : '
            log_str += f'функция <{some_func.__name__}>'
            log_str += f', аргументы *args: <{args}>, **kwargs: <{kwargs}>'
            result = some_func(*args, **kwargs)
            log_str += f'- возвращаемое значение <{result}>'
            logfile.write(f'{log_str}\n')
            return result

    return new_some_func


@logger
def adv_print(*args, **kwargs):
    """
    adv_print(text: str, start_text: str, max_line=int, in_file=path_to_file: str)
    """
    str_result = ''
    if len(args) > 1:
        str_result += args[1] + '\n'
    max_line = kwargs.get('max_line')
    if max_line:
        counter = 0
        text = ''
        for liter in args[0]:
            text += liter
            counter += 1
            if counter == max_line:
                counter = 0
                text += '\n'
        str_result += text
    else:
        str_result += args[0]
    path = kwargs.get('in_file')
    if path:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(str_result)
    print(str_result)


if __name__ == '__main__':
    adv_print('Контакт с именем Jhon и фамилией Smit в телефонной книге не найден', 'start_text', max_line=10,
              in_file='adv_print.txt', log='log3.txt')
