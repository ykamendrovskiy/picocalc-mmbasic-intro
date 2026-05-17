# References — справочные материалы для курса

Папка-кладовка офлайновых копий и сводок ключевой документации MMBasic / PicoMite / PicoCalc. Используется как источник правды при написании уроков, чтобы курс ссылался на задокументированные best practices, а не на интуицию.

Не публикуется как часть сайта (не в `lessons/`). Не индексируется поиском MkDocs.

## Структура

```
references/
├── README.md                                     ← этот файл
├── manual/                                       ← официальный мануал PicoMite
│   ├── PicoMite_User_Manual.pdf                  (полный PDF, ~2.8 МБ)
│   ├── full_screen_editor.md                     (хоткеи редактора)
│   ├── first_steps.md                            (REPL / EDIT / Hello world)
│   ├── using_mmbasic.md                          (структура программ, MM.STARTUP / MM.PROMPT, библиотека)
│   ├── special_keyboard_keys.md                  (Appendix H: коды клавиш)
│   ├── edit_command.md                           (синтаксис EDIT / EDIT name / EDIT FILE)
│   └── graphics_quick_reference.md               (CLS/PIXEL/LINE/BOX/CIRCLE/TEXT/POLYGON/ARC + framebuffer)
├── picocalc/                                     ← PicoCalc-специфика
│   ├── PicoMite_RC23_release_notes.md            (madcock RC23 firmware: keyboard mapping)
│   ├── LennartHennigs_PicoCalc_Notes.md          (Lennart Hennigs: hardware pinout, options, tips)
│   ├── michaeladcock_examples_index.md           (Michael Adcock TiddlyWiki: библиотека программ)
│   ├── russian_locale.md                         (анализ кириллицы / CP1251 / DefineFont — 17.05.2026)
│   └── forum_threads.md                          (релевантные ветки forum.clockworkpi.com)
└── community/                                    ← сообщество
    ├── mmbasic_style_guide.md                    (Lennart Hennigs: стиль-гайд для PicoCalc, RC23)
    └── mmbasic_source_code_formatter.md          (Hugh Buckle / Geoff Graham: индентация-канон, FotS wiki)
```

## Что где брать (по теме)

| Нужно | Куда смотреть |
|---|---|
| Точное поведение `EDIT` и хоткеев | `manual/full_screen_editor.md`, `manual/edit_command.md` |
| Что REPL делает по умолчанию (F2/F3/F4/F10/F11/F12) | `manual/using_mmbasic.md` |
| Коды клавиш — какой `INKEY$` пришлёт стрелка/Fn/Esc | `manual/special_keyboard_keys.md` |
| Как PicoCalc меняет/режет стандартный keymap | `picocalc/PicoMite_RC23_release_notes.md` |
| Идиоматичный стиль (отступы, имена, OPTION EXPLICIT, `LOCAL`, no GOTO) | `community/mmbasic_style_guide.md` |
| Каноническая индентация (FORMAT.BAS-rules) | `community/mmbasic_source_code_formatter.md` |
| Графика: палитра, шрифты, рисующие команды, framebuffer | `manual/graphics_quick_reference.md` (краткая) или PDF (полная) |
| Образцы реальных программ под RC23 | `picocalc/michaeladcock_examples_index.md` |
| Распиновка и опции прошивки PicoCalc | `picocalc/LennartHennigs_PicoCalc_Notes.md` |
| Что обсуждает коммьюнити | `picocalc/forum_threads.md` |
| Русский язык / кириллица на LCD и serial | `picocalc/russian_locale.md` |

## Для каких уроков что пригодится

- **00 (Setup и REPL)** — `using_mmbasic.md`, `full_screen_editor.md`, `edit_command.md`. Уже использовано в текущем уроке: реальные F1=SAVE / F2=RUN / Esc=discard.
- **01 (Тур по MMBasic)** — `using_mmbasic.md`, `mmbasic_style_guide.md` (no GOTO, no line numbers, KISS/DRY/YAGNI).
- **02 (Данные и управление)** — `mmbasic_style_guide.md` (variable naming, `LOCAL` scope, OPTION EXPLICIT), `mmbasic_source_code_formatter.md` (отступы под IF/FOR/DO).
- **03 (SUB/FUNCTION)** — `mmbasic_style_guide.md` (короткие функции, единственная ответственность, `LOCAL` обязательно).
- **04 (Графика)** — `graphics_quick_reference.md`, PDF chapter "Graphics", `michaeladcock_examples_index.md` (рабочие примеры под 320×320).
- **05 (Ввод)** — `special_keyboard_keys.md`, `PicoMite_RC23_release_notes.md` (что PicoCalc реально шлёт за `INKEY$`).
- **06 (Звук и время)** — PDF `PLAY TONE` (есть известная опечатка в текущем мануале — см. `forum_threads.md`); `using_mmbasic.md` про `SETTICK`.
- **07 (Файлы и SD)** — PDF `OPEN/CLOSE/PRINT #/INPUT #/EOF`, `using_mmbasic.md` про `VAR SAVE/RESTORE`.
- **08 (Capstone)** — собрать всё; стиль и архитектуру брать из `mmbasic_style_guide.md`.

## Источники и даты

| Файл | URL | Дата фиксации |
|---|---|---|
| `manual/PicoMite_User_Manual.pdf` | <https://geoffg.net/Downloads/picomite/PicoMite_User_Manual.pdf> | 2026-05-17, объявленная ревизия V6.02.01 от 25.03.2026 |
| `manual/*.md` | <https://yamavu.github.io/PicoMite_User_Manual/> | 2026-05-17 |
| `picocalc/PicoMite_RC23_release_notes.md` | <https://github.com/madcock/PicoMiteAllVersions/releases/tag/V6.00.02RC23> | 2026-05-17 (release published 2025-05-08) |
| `picocalc/LennartHennigs_PicoCalc_Notes.md` | <https://github.com/LennartHennigs/PicoCalc-Notes> | 2026-05-17 |
| `picocalc/michaeladcock_examples_index.md` | <https://michaeladcock.info/temp/PicoCalc_MMBasic.html> | 2026-05-17 (содержание датировано 30.06.2025) |
| `community/mmbasic_style_guide.md` | <https://github.com/LennartHennigs/PicoCalc-Notes/blob/main/src/CLAUDE.md> | 2026-05-17 (последнее обновление в репо — 04.09.2025) |
| `community/mmbasic_source_code_formatter.md` | <https://fruitoftheshed.com/wiki/doku.php?id=mmbasic_original%3Ammbasic_source_code_formatter> | 2026-05-17 (исходник 20.04.2013, MMBasic 4.x — устаревший, но правила индентации актуальны) |
| `picocalc/forum_threads.md` | <https://forum.clockworkpi.com/c/picocalc/> (несколько тредов) | 2026-05-17 |

## Лицензии и происхождение

- **PicoMite User Manual** — Geoff Graham и др. CC BY-NC-SA 3.0 Australia. Воспроизведено для офлайн-справки в рамках того же CC-режима. Атрибуция в каждом файле.
- **MMBasic style guide** (Lennart Hennigs) — лицензия не указана явно в файле; репозиторий `PicoCalc-Notes` под GPL-3.0. Используется как референс с атрибуцией.
- **MMBasic Source Code Formatter** (Hugh Buckle / Geoff Graham, 2013) — воспроизведено на FotS wiki "with kind permission". Здесь — конспект правил, не исходник.
- **PicoCalc RC23 release notes** (Michael Adcock / madcock) — публичная страница релиза GitHub.
- Форумные ветки — публичная переписка на forum.clockworkpi.com.

Все материалы используются исключительно как справочный контекст для написания этого учебного курса. Полный текст и обновления — по ссылкам в источниках.

## Когда обновлять

- Когда выходит новый PicoMite User Manual (объявления — на forum.clockworkpi.com или geoffg.net).
- Когда меняется RC-сборка под PicoCalc (madcock публикует release notes).
- Перед тем, как писать новый урок: пройтись по соответствующим файлам, проверить, что цитируемые формулировки и синтаксис не устарели.
