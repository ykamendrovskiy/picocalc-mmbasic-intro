# Урок 02 — Данные и управление

Цель: углубиться в типы, массивы, строки и управляющие конструкции. После этого урока ты пишешь нормальные структурированные программы, а не «строки, склеенные двоеточием».

## Типы — ещё раз и подробнее

Три базовых типа:

| Тип | Суффикс | Размер / диапазон |
|-----|---------|-------------------|
| `INTEGER` | `%` | 64-битное целое со знаком (`-9.2e18 … 9.2e18`) |
| `FLOAT` | `!` | Double precision (~15–16 значащих цифр) |
| `STRING` | `$` | Строка переменной длины (по умолчанию до 255 символов) |

Объявляются двумя эквивалентными способами:

```basic
DIM count AS INTEGER
DIM count%             ' то же самое
DIM ratio AS FLOAT
DIM ratio!
DIM name AS STRING
DIM name$
```

Можно сразу с инициализацией:

```basic
DIM lives AS INTEGER = 3
DIM pi! = 3.14159
DIM player$ = "Alice"
```

Можно несколько в одной строке:

```basic
DIM x%, y%, z%
DIM age%, label$
```

### Какой тип когда

- **`INTEGER`** — счётчики, координаты на экране, очки, состояние enum'ов. Скорость вычислений выше, чем у `FLOAT`.
- **`FLOAT`** — там, где нужны дробные значения: физика мячика, тригонометрия, проценты.
- **`STRING`** — текст, очевидно. Также как «универсальный буфер» — когда не уверен, удобно начать со строк, потом сузить.

### Строгий режим: `OPTION EXPLICIT` + `OPTION DEFAULT NONE`

Поставь в начало любой программы серьёзнее, чем «hello world»:

```basic
OPTION EXPLICIT
OPTION DEFAULT NONE
```

Что это даёт:
- **`OPTION EXPLICIT`** — каждая переменная должна быть `DIM`-нута до использования. Опечатался в имени — сразу `Error: XXX is not declared` вместо тихо живущего «фантома».
- **`OPTION DEFAULT NONE`** — если у переменной не указан тип (ни через `AS`, ни через суффикс) — это ошибка. Без этого опции переменная без типа считается `FLOAT` — а это редко то, что хочется.

> ⚠️ **Важное следствие** для QBasic-головы: при `OPTION EXPLICIT` **счётчики FOR тоже надо `DIM`-ать заранее**. В QBasic `FOR i = 1 TO 5` создавал `i` сам, в MMBasic в строгом режиме это уже ошибка `Error: I is not declared`. Решение:
>
> ```basic
> OPTION EXPLICIT
> OPTION DEFAULT NONE
> DIM i AS INTEGER
> FOR i = 1 TO 5
>   PRINT i
> NEXT i
> ```

## Массивы

Одномерный массив:

```basic
DIM scores(9) AS INTEGER     ' 10 элементов: scores(0) ... scores(9)
```

По умолчанию **индексация с нуля** — `OPTION BASE 0`. Если хочешь как в Pascal, с единицы:

```basic
OPTION BASE 1
DIM scores(10) AS INTEGER    ' тоже 10 элементов, но scores(1) ... scores(10)
```

> ⚠️ `OPTION BASE` нужно поставить **до первого `DIM` или `LOCAL`** в программе. Если уже что-то задекларировал — `Error: Must be before DIM or LOCAL`.

Многомерные массивы:

```basic
DIM grid(7, 7) AS INTEGER     ' 8×8, индексы 0..7 по обоим измерениям
DIM cube(3, 3, 3) AS FLOAT    ' трёхмерный
```

Заполнение через цикл:

```basic
DIM i AS INTEGER
DIM total AS INTEGER = 0
DIM nums(4) AS INTEGER

FOR i = 0 TO 4
  nums(i) = i * 10
NEXT i

FOR i = 0 TO 4
  total = total + nums(i)
NEXT i
PRINT "Сумма: "; total      ' 100 (0+10+20+30+40)
```

Строковые массивы — точно так же:

```basic
DIM names$(2)
names$(0) = "Alice"
names$(1) = "Bob"
names$(2) = "Carol"
PRINT names$(1)              ' Bob
```

Размер массива можно изменить позже — `REDIM`. И прочесть текущий размер — функцией `BOUND(array, dimension)`. Но в этом курсе нам это не понадобится.

## Строки и функции

Конкатенация — `+`:

```basic
DIM greeting$ = "Hello, " + "PicoCalc!"
```

Ключевые функции:

```basic
LEN("test")              ' 4
LEFT$("hello", 2)        ' "he"
RIGHT$("hello", 3)       ' "llo"
MID$("hello", 2, 3)      ' "ell" — со 2-й позиции, 3 символа (1-based!)
INSTR("hello world", "world")   ' 7  (позиция, 1-based; 0 если не нашёл)
UCASE$("abc")            ' "ABC"
LCASE$("XYZ")            ' "xyz"
STR$(42)                 ' "42"
VAL("3.14")              ' 3.14
CHR$(65)                 ' "A"
ASC("A")                 ' 65
SPACE$(5)                ' "     "
STRING$(3, "*")          ' "***"
```

Форматирование чисел — через `FORMAT$()`:

```basic
PRINT FORMAT$(3.14159, "%.2f")     ' "3.14"
PRINT FORMAT$(3.14, "%6.2f")       ' "  3.14" (ширина 6, выравнивание справа)
PRINT FORMAT$(1000, "%g")          ' "1000" (компактный научный)
```

> ⚠️ В PicoMite `FORMAT$` принимает **только float-спецификаторы** — `%f`, `%g`, `%e`. Целочисленные `%d`, `%i` и группировка `%,d` дают `Error: Illegal character in format specification`. Чтобы напечатать целое со ведущими нулями — преобразуй явно: `FORMAT$(n, "%07.0f")` или собери строку через `STR$()` и `STRING$()`.

> 📌 Все позиции в строковых функциях **1-based**: первый символ — это позиция 1, не 0. Соглашение, унаследованное от классического BASIC. Не путай с массивами, где базу выбираешь сам через `OPTION BASE`.

## IF — однострочный и многострочный

**Однострочный** хорош для коротких проверок:

```basic
IF lives = 0 THEN PRINT "Game over"
IF score > best THEN best = score : PRINT "Record!"
```

`ELSE` тоже работает в одной строке:

```basic
IF score > 100 THEN PRINT "win" ELSE PRINT "try again"
```

Но **`ELSEIF`-цепочки и многоблочные конструкции пиши только в многострочной форме**. Однострочный IF в MMBasic не разделяет ветки через `:` так, как ты ожидаешь — `IF a THEN x : ELSEIF b THEN y` интерпретируется не как ветвление, а как «всё после `THEN` до конца строки — это блок THEN». Поэтому:

```basic
IF age < 13 THEN
  label$ = "kid"
ELSEIF age < 18 THEN
  label$ = "teen"
ELSEIF age < 65 THEN
  label$ = "adult"
ELSE
  label$ = "senior"
ENDIF
```

Вложенные IF — без проблем, главное закрывать каждый своим `ENDIF`.

## SELECT CASE

Когда сравниваешь одну величину с кучей значений — `SELECT CASE` чище, чем лестница `ELSEIF`:

```basic
DIM x AS INTEGER = 7

SELECT CASE x
  CASE 1 TO 5
    PRINT "small"
  CASE 6 TO 10
    PRINT "mid"
  CASE IS > 10
    PRINT "big"
  CASE ELSE
    PRINT "negative or zero"
END SELECT
```

Поддерживает:
- **списки**: `CASE 1, 3, 5, 7`
- **диапазоны**: `CASE 0 TO 9`
- **сравнения**: `CASE IS > 100`, `CASE IS <= 0`
- **строки**: `CASE "yes", "y", "Y"`

Заметь: `END SELECT` пишется в **два слова**, в отличие от `ENDIF`.

## FOR

Базовая форма:

```basic
DIM i AS INTEGER
FOR i = 1 TO 10
  PRINT i
NEXT i
```

С шагом (в том числе обратным):

```basic
DIM i AS INTEGER
FOR i = 100 TO 0 STEP -10
  PRINT i
NEXT i
```

Досрочный выход:

```basic
DIM i AS INTEGER
DIM found AS INTEGER = 0
FOR i = 1 TO 1000
  IF check(i) THEN found = i : EXIT FOR
NEXT i
```

После `EXIT FOR` управление переходит сразу за `NEXT`. Имя переменной в `NEXT` указывать не обязательно (`NEXT` — само поймёт), но при вложенных циклах это сильно помогает читателю.

## DO ... LOOP

Самая универсальная конструкция — бесконечный цикл с условием выхода в любом месте:

```basic
DIM j AS INTEGER = 0
DO
  j = j + 1
  IF j = 3 THEN EXIT DO
LOOP
PRINT j     ' 3
```

С условием в начале:

```basic
DIM lives AS INTEGER = 3
DO WHILE lives > 0
  play_turn
LOOP
```

С условием в конце:

```basic
DO
  play_turn
LOOP UNTIL lives = 0
```

Разница: `DO WHILE` может вообще не выполниться (если условие сразу ложно), `DO ... LOOP UNTIL` гарантированно прокрутится минимум один раз.

## Финальный проект урока: расширенная угадайка

Сложим всё вместе. Расширим «угадайку» из урока 01 — теперь с именем игрока, повторными раундами и счётом побед.

```basic
' guess2.bas — угадайка с именем, ре-играми и подсчётом побед
OPTION EXPLICIT
OPTION DEFAULT NONE

DIM player$
DIM secret AS INTEGER
DIM guess AS INTEGER
DIM tries AS INTEGER
DIM wins AS INTEGER = 0
DIM answer$

INPUT "Как тебя зовут? ", player$
PRINT "Привет, " + player$ + "! Я загадываю числа от 1 до 100."

RANDOMIZE TIMER

DO
  secret = INT(RND * 100) + 1
  tries = 0

  DO
    INPUT "Твой вариант: ", guess
    tries = tries + 1
    SELECT CASE guess
      CASE IS < secret
        PRINT "Больше."
      CASE IS > secret
        PRINT "Меньше."
      CASE ELSE
        PRINT "В точку! Попыток: "; tries
        wins = wins + 1
        EXIT DO
    END SELECT
  LOOP

  PRINT player$ + ", побед в сессии: "; wins
  INPUT "Ещё раунд? (Y/N) ", answer$
LOOP WHILE UCASE$(answer$) = "Y"

PRINT "До встречи, " + player$ + "!"
```

Что здесь нового:
- **`OPTION EXPLICIT` + `OPTION DEFAULT NONE`** — все переменные явно объявлены.
- **Вложенные `DO ... LOOP`** — внешний для ре-игр, внутренний для угадывания.
- **`SELECT CASE`** с диапазонами `IS <`, `IS >` — чище чем три IF.
- **`UCASE$()`** — сравниваем с `"Y"` независимо от регистра, чтобы и `y`, и `Y` работали.
- **`LOOP WHILE`** в конце — повторяем, пока ответ начинается с `Y`.

Сохрани, запусти, поиграй. Сравни читаемость с однораундовой версией из урока 01.

## Упражнение

1. Запусти `guess2.bas`. Поиграй пару раундов.
2. Доработай:
   - **Сложность.** Перед началом сессии спроси, какой диапазон чисел использовать (`Easy: 1–50`, `Normal: 1–100`, `Hard: 1–500`). Реализуй через `SELECT CASE` по введённой букве.
   - **Лимит попыток.** В режиме `Hard` дай только 10 попыток. Если не угадал — програмный сообщает ответ и засчитывает поражение.
   - **Статистика.** В конце сессии выведи общую статистику: побед, поражений, средняя попытка на победу. Подсказка: суммируй `tries` только для побед.
3. Если хочешь — сохрани финальную версию в Flash-слот 1 (`FLASH SAVE 1`), чтобы запускать по `FLASH RUN 1` с любого момента.

Когда `OPTION EXPLICIT` стало рефлексом, а структура программы — это «вложенные DO с явными EXIT» вместо «GOTO в чистилище», переходим к **Уроку 03 — SUB и FUNCTION** (в работе), где разберём, как нарезать программу на куски, чтобы она не превращалась в один длинный свиток.
