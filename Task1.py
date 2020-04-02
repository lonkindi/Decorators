import datetime


def logger(some_func):
    log_str = ''

    def new_some_func():
        with open('log1.txt', 'a', encoding='utf-8') as logfile:
            nonlocal log_str
            log_str = f'{datetime.datetime.now()} : '
            log_str += f'функция <{some_func.__name__}>'
            result = some_func() // 2
            log_str += f' - возвращаемое значение <{result}>'
            logfile.write(f'{log_str}\n')
            return result

    return new_some_func


@logger
def square():
    a = 10
    return a ** 2


if __name__ == '__main__':
    print(square())
