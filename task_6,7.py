# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# 7. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().


def int_func(word):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(alphabet) else False


words = input('sdsffsf').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w))
