# DarktraceAPI

Этот проект предназначен для изучения и парсинга Model Breach алертов с использованием Darktrace API.

## Состав репозитория
- `darktrace_api_client.py` — базовый Python-скрипт для подключения и получения алертов через Darktrace API.
- `PRD_Darktrace_Model_Breach_Parser.md` — подробный Product Requirements Document (PRD) по проекту.
- `Darktrace-API.md` — официальная документация по Darktrace API (оригинал).

## Быстрый старт
1. Установите зависимости:
   ```bash
   pip install requests
   ```
2. Заполните ваши токены и адрес Darktrace в начале файла `darktrace_api_client.py`.
3. Запустите скрипт:
   ```bash
   python darktrace_api_client.py
   ```

## Документация
- Подробное описание архитектуры, требований и примеров работы с API — в файле `PRD_Darktrace_Model_Breach_Parser.md`.
- Оригинальная документация по API — в файле `Darktrace-API.md`.

## Лицензия
Проект предназначен для внутреннего использования и обучения. 