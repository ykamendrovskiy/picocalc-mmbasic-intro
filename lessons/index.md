# mmBasic — мини-курс

Погружение в **MMBasic** на устройстве **ClockworkPi PicoCalc** (предустановленная прошивка `PicoMite MMBasic RP2040 Edition v6.00.02 RC23`).

## Для кого

Для того, кто когда-то писал на QBasic / школьном BASIC и хочет быстро освоить современный MMBasic, плюс по дороге разобраться с фишками PicoCalc — экраном 320×320, клавиатурой, звуком и SD-карточкой.

## Как пользоваться

Уроки идут по порядку — каждый рассчитан на 10–20 минут чтения и пару коротких сниппетов, которые набираются прямо на устройстве через `EDIT`. После каждого урока — мини-упражнение, чтобы пощупать материал руками.

## Карта курса

### Готовые уроки

| # | Урок | О чём |
|---|------|-------|
| 00 | [Setup и REPL](00-setup.md) | REPL, `EDIT`, `LIST/RUN/SAVE/LOAD`, Flash-слоты, накопители `A:`/`B:` |
| 01 | [Язык: тур по MMBasic](01-language-tour.md) | Что осталось от QBasic, что выкинуто, что новое |
| 02 | [Данные и управление](02-data-and-control.md) | Типы, массивы, строки, IF/SELECT/FOR/DO + расширенная угадайка |

### В работе

| # | Урок | О чём |
|---|------|-------|
| 03 | SUB и FUNCTION | Параметры, скоуп, мини-библиотечка утилит |
| 04 | Графика | 320×320, `COLOUR`, `LINE`/`BOX`/`CIRCLE`/`TEXT`, FRAMEBUFFER |
| 05 | Ввод и клавиатура | `INKEY$`, `INPUT$`, polling vs blocking |
| 06 | Звук и время | `PLAY TONE`, `PAUSE`, `SETTICK`, метроном |
| 07 | Файлы и SD | `OPEN`/`PRINT #`/`INPUT #`, сохранение настроек |
| 08 | Capstone | Мини-проект, связывающий графику + ввод + звук + файл |

Уроки 03–08 будут добавляться по мере прохождения.

## Ссылки

- [PicoMite User Manual (Geoff Graham, последняя версия)](https://geoffg.net/picomite.html) — канонический справочник по командам.
- [Онлайн-зеркало мануала](https://yamavu.github.io/PicoMite_User_Manual/introduction.html) — удобно гуглить и линковать.
- [The Back Shed forum, ветка PicoMite](https://www.thebackshed.com/forum/ViewForum.php?FID=16) — где живёт коммьюнити, Geoff Graham и Peter Mather читают.
- [ClockworkPi PicoCalc DeepWiki](https://deepwiki.com/clockworkpi/PicoCalc/) — про железо и заводскую прошивку.

Если в уроке что-то не сходится с тем, что выводит твой PicoCalc, сначала смотри в `HELP <команда>` прямо в REPL и в актуальный мануал — версии RC что-то добавляют почти каждый месяц.
