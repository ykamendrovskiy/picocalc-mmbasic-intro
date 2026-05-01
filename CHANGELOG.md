# Changelog

## 2026-05-01
- Сайт: scaffolding MkDocs Material для публикации курса на GitHub Pages — `mkdocs.yml`, `lessons/index.md` (карта курса), `requirements.txt`, GitHub Actions workflow `.github/workflows/deploy.yml`, `.gitignore`. Локальный preview через `uv run --with mkdocs-material mkdocs serve`.
- Курс: добавлен урок 02 (Данные и управление) — типы, OPTION EXPLICIT/DEFAULT, массивы, строки, IF/SELECT/FOR/DO, расширенная угадайка с ре-играми и счётом
- Курс: настроен живой REPL-канал к PicoCalc через USB-C (`/dev/cu.usbserial-10`), helper `.tools/picomite_repl.py`, процесс написания с проверкой команд описан в `.tools/AUTHORING.md`
- Уроки 00–02: поправки по итогам тестирования на устройстве (CHDIR не принимает префикс другого диска, Home×2 не работает, HELP без help.txt, FORMAT$ только для float)

## 2026-04-30
- Project initialized
- Курс: добавлен README с оглавлением, уроки 00 (Setup и REPL) и 01 (тур по MMBasic)
