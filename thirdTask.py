import types
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('thirdTask.log', 'a') as log:
            time = datetime.datetime.now()
            name = old_function.__name__
            result = old_function(*args, **kwargs)
            log.write(
                f'время вызова: {time}\n'
                f'имя функции: {name}\n'
                f'параметры: {args}\n'
                f'именованные параметры: {kwargs}\n'
                f'результат функции: {result}\n\n'
            )
            return result

    return new_function


@logger
def flat_generator(list_of_lists):
    for item in list_of_lists:
        if type(item) == list:
            for inner_item in item:
                yield inner_item
        else:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
