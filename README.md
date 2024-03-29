### Идея
Все мы сталкивались с различными "сокращателями ссылок". Почему бы нам не использовать их, для хранения какой-нибудь информации? Скрипт на Python получает пользовательскую информацию, используя сокращенную ссылку.<br>
Обычно сервисы совсем НЕ проверяют валидность "длинной" ссылки, а значит можно ввести абсолютно любой URL.

### Как записать информацию
1. Переходим на сайт: https://shorturl.at/
2. Пишем любой домен (даже несуществующий), а после знака `/` вписываем любую текстовую информацию
3. Получаем сокращенную ссылку

**Пример:**<br>
![](https://media.discordapp.net/attachments/766382334067867668/969020277847646238/unknown.png?width=798&height=471)


### Как пользоваться скриптом
1. Запускаем `app.py` в Вашем терминале
2. Вставляем сокращенную ссылку

**Пример:**<br>
![](https://media.discordapp.net/attachments/766382334067867668/969022759734763531/unknown.png)


### Подробная информация
- Код, который получает информацию из сокращенной ссылки, находится в файле `shortdataparser.py`
- Вы свободно можете использовать его в качестве библеотеки в вашем проекте! Для этого, там существует функция `get`, принимающая аргумент `id`
- Функция `get` возращает обычную строку
- В коде присутсвует базовая документация, очень просто адаптировать его под другие сервисы "сокращателей ссылок"

### Лицензия
- используйте там, где ваша душа пожелает
- редактируйте так, как ваша душа хочет
