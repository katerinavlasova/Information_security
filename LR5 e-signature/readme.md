ВОПРОСЫ:
как работает?

Создание подписи:
Считываем исходное сообщение из файла, хэшируем. Затем с помощью RSA алгоритма шифруем ЗАКРЫТЫМ ключом.
Это и есть электронная подпись, записываем её в файл (т.е. наша подпись - это зашифрованная хэш-функция).

Проверка подписи:
1.Считываем исходное сообщение из файла, хэшируем.
2.Также считываем созданную электронную подпись из файла. Расшифровываем ОТКРЫТЫМ ключом (после расшифровки у нас получается хэш-функция).
Сравниваем хэш-функции 1 и 2 (свойство хэш-функций: одно и то же сообщение хэшируется одинаково). Если хэш-функции совпадают, то всё хорошо.