# Мониторинг ресурсов

## Описание

Это настольное приложение, написанное на Python с использованием библиотек tkinter и psutil. Приложение предназначено для мониторинга загрузки ЦП, ОЗУ и ПЗУ на компьютере под управлением операционной системы Linux в реальном времени.

## Функциональные возможности

- Отображение уровня загруженности ЦП, ОЗУ и ПЗУ в реальном времени, а так же операции записи и чтения диска в Мб.
- Время обновления данных не менее одного раза в секунду с возможностью настройки.
- Кнопка «Начать запись», которая запускает запись данных в базу данных SQLite.
- После нажатия кнопки «Начать запись» она заменяется на кнопку «Остановить запись», которая отображает секундамер и начинает отсчёт.
- По окончании записи кнопка «Остановить» заменяется обратно на «Начать запись», и секундамер обнуляется.

## Установка

Для работы приложения необходимо установить Python и библиотеки, используемые в проекте. Убедитесь, что у вас установлен Python версии 3.x. Установите необходимые библиотеки, выполнив следующую команду:

```pip install psutil```


## Запуск приложения

1. Склонируйте репозиторий или скачайте код приложения.
2. Перейдите в директорию с проектом.
3. Запустите нужное приложение с помощью команды:

```python main.py```


## Использование

1. При запуске приложения вы увидите интерфейс с текущими уровнями загрузки ЦП, ОЗУ и ПЗУ.
2. Чтобы начать запись данных, нажмите кнопку «Начать запись».
3. Запись будет продолжаться до нажатия кнопки «Остановить запись», при этом будет отображаться секундамер.
4. После нажатия на кнопку «Остановить запись» данные больше не будут записываться в базу данных, и секундамер будет сброшен.

## Примечания

- Убедитесь, что у вас есть права доступа к записи в директорию, где создаётся база данных SQLite.
- БД будет созданно в директории со скриптом.