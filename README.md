# Производственный календарь
Функция для парсинга производственных календарей с сайта consultant.ru **после 2010 года**.
Принимает год или период и возвращает ключ-значение, где ключ дата, а значение статус.

**Статусы:**
- workday (рабочий)
- preholiday (предпраздничный, сокращенный)
- weekend (выходной)
- nowork (нерабочий)

**Используемые модули:**
- json
- requests
- re
- calendar
- datetime
- BeautifulSoup

**Пример за год**

```python
get_production_calendar(2021)
```

**Пример за период**

```python
get_production_calendar(2010,2021)
```
