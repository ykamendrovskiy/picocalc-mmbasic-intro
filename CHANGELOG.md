# Changelog

## 2026-05-17
- Урок 00: добавлена заметка про per-drive cwd (после `CHDIR "lessons"` на `B:` смена диска `B:` возвращает в `B:/lessons`, а не в корень — поведение из DOS/CP/M)
- Урок 00: переименовано упражнение 1 — «Перенеси `hello.bas` с `A:` на `B:`» вместо «Повтори ещё раз и перенеси на SD» (заголовок не соответствовал содержанию: ничего повторять не надо, просто `COPY`+`KILL`)
- `.tools/AUTHORING.md`: добавлена gotcha #16 про per-drive cwd
- `references/`: собраны материалы от производителя и комьюнити (PicoMite User Manual, RC23 release notes, PicoCalc-специфичные заметки Ленарта Хеннигса, индекс примеров michaeladcock, форумные треды, MMBasic style guide, source-code formatter rules) + `references/picocalc/russian_locale.md` с разбором поддержки кириллицы
- Урок 00: переписан раздел про редактор `EDIT` по официальному мануалу — `F1=SAVE-to-memory`, `F2=RUN`, `Esc=DISCARD`; уточнён статус-бар; добавлены инструкции по выходу из редактора и набору `SAVE`
- Урок 00: упражнение разделено на копирование `A:`→`B:` (`COPY`/`KILL`/`RENAME` с пояснением кросс-дисковых ограничений) и написание новой программы `clock.bas` через `NEW + EDIT`
- Уроки 00–02: все строковые литералы в `PRINT`/`INPUT` переведены на ASCII (English) — встроенные шрифты PicoMite не содержат кириллицу, на LCD получалась каша. Комментарии остаются на русском
- README/index: добавлен раздел «Код на английском, комментарии на русском» с пояснением и ссылкой на `russian_locale.md`
- Урок 01: усилена позиция «No GOTO» по style guide; пример бесконечного цикла переписан через `DO/LOOP`
- Урок 02: добавлены замечания по style guide (`OPTION BASE 1`, избегать `:` для chaining), AUTOSAVE-нюанс для программ с `INPUT`, подсказка про `CONST` вместо магических чисел
- Урок 00: программа `hello.bas` обновлена с пояснительным блоком про ASCII в строках
- `.tools/picomite_repl.py`: автодетект serial-порта (`/dev/cu.usbserial-*`) и поддержка `PICOMITE_PORT`
- `.tools/AUTHORING.md`: добавлены gotchas #12–#15 (RENAME через `AS`, кросс-дисковые ограничения, EDIT hotkeys, `EDIT "name.bas"` создаёт файл)
- `.gitignore`: исключён `references/manual/*.pdf`

## 2026-05-01
- Сайт: scaffolding MkDocs Material для публикации курса на GitHub Pages — `mkdocs.yml`, `lessons/index.md` (карта курса), `requirements.txt`, GitHub Actions workflow `.github/workflows/deploy.yml`, `.gitignore`. Локальный preview через `uv run --with mkdocs-material mkdocs serve`.
- Курс: добавлен урок 02 (Данные и управление) — типы, OPTION EXPLICIT/DEFAULT, массивы, строки, IF/SELECT/FOR/DO, расширенная угадайка с ре-играми и счётом
- Курс: настроен живой REPL-канал к PicoCalc через USB-C (`/dev/cu.usbserial-10`), helper `.tools/picomite_repl.py`, процесс написания с проверкой команд описан в `.tools/AUTHORING.md`
- Уроки 00–02: поправки по итогам тестирования на устройстве (CHDIR не принимает префикс другого диска, Home×2 не работает, HELP без help.txt, FORMAT$ только для float)

## 2026-04-30
- Project initialized
- Курс: добавлен README с оглавлением, уроки 00 (Setup и REPL) и 01 (тур по MMBasic)
