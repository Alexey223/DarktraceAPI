'''
Базовый клиент для взаимодействия с Darktrace API.
'''
import requests
import hmac
import hashlib
import time
from datetime import datetime, timezone
import json

# --- НАСТРОЙКИ КЛИЕНТА --- #
# Замените значения ниже вашими актуальными данными
APPLIANCE_IP = "YOUR_APPLIANCE_IP_OR_HOSTNAME"  # IP-адрес или хостнейм вашего Darktrace устройства
PUBLIC_TOKEN = "YOUR_PUBLIC_API_TOKEN"
PRIVATE_TOKEN = "YOUR_PRIVATE_API_TOKEN"

# Настройки для запроса Model Breaches
DEFAULT_START_TIME_HOURS_AGO = 24  # За какой период в часах запрашивать алерты по умолчанию

# --- ОСНОВНЫЕ ФУНКЦИИ --- #

def generate_dtapi_signature(private_token: str, public_token: str, api_request_path: str, date_str: str) -> str:
    '''
    Генерирует DTAPI-Signature для аутентификации запросов к Darktrace API.

    :param private_token: Приватный API токен.
    :param public_token: Публичный API токен.
    :param api_request_path: Путь запроса к API (например, "/modelbreaches?starttime=123...")
    :param date_str: Строка с датой и временем в формате, принимаемом API (например, "YYYYMMDDTHHIISS").
    :return: Строка с HMAC-SHA1 подписью.
    '''
    message = f"{api_request_path}\n{public_token}\n{date_str}"
    signature = hmac.new(
        private_token.encode('ASCII'),
        message.encode('ASCII'),
        hashlib.sha1
    ).hexdigest()
    return signature

def get_current_api_date() -> str:
    '''
    Возвращает текущую дату и время в UTC в формате YYYYMMDDTHHMMSS, подходящем для DTAPI-Date.
    '''
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")

def get_model_breaches(appliance_ip: str, 
                         public_token: str, 
                         private_token: str, 
                         starttime_ms: int = None, 
                         endtime_ms: int = None, 
                         limit: int = 50,
                         offset: int = 0,
                         min_score: int = None,
                         extra_params: dict = None) -> dict:
    '''
    Получает Model Breach алерты из Darktrace API.

    :param appliance_ip: IP-адрес или хостнейм Darktrace устройства.
    :param public_token: Публичный API токен.
    :param private_token: Приватный API токен.
    :param starttime_ms: Время начала выборки в миллисекундах (Unix timestamp).
                         Если None, используется DEFAULT_START_TIME_HOURS_AGO.
    :param endtime_ms: Время конца выборки в миллисекундах (Unix timestamp).
                       Если None, используется текущее время.
    :param limit: Максимальное количество алертов для возврата.
    :param offset: Смещение для пагинации.
    :param min_score: Минимальный скор угрозы для фильтрации (0-100).
    :param extra_params: Дополнительные параметры запроса в виде словаря.
    :return: Словарь с JSON-ответом от API или None в случае ошибки.
    '''
    base_url = f"https://{appliance_ip}"
    endpoint_path = "/modelbreaches"

    # Установка времени по умолчанию, если не задано
    if endtime_ms is None:
        endtime_ms = int(time.time() * 1000)
    if starttime_ms is None:
        starttime_ms = int((time.time() - DEFAULT_START_TIME_HOURS_AGO * 3600) * 1000)

    query_params = {
        "starttime": starttime_ms,
        "endtime": endtime_ms,
        "limit": limit,
        "offset": offset
    }

    if min_score is not None:
        query_params["minscore"] = min_score
        
    if extra_params:
        query_params.update(extra_params)

    # Формируем строку параметров для подписи и URL
    # Параметры должны быть отсортированы для консистентности подписи, 
    # хотя документация Darktrace не упоминает это явно, это хорошая практика.
    # Однако, следуя примеру Darktrace, они не сортируют, поэтому оставим как есть.
    query_string_parts = [f"{key}={value}" for key, value in query_params.items()]
    query_string = "&".join(query_string_parts)
    
    full_request_path_for_signature = f"{endpoint_path}?{query_string}"
    full_url = f"{base_url}{full_request_path_for_signature}"

    api_date_str = get_current_api_date()
    signature = generate_dtapi_signature(private_token, public_token, full_request_path_for_signature, api_date_str)

    headers = {
        "DTAPI-Token": public_token,
        "DTAPI-Date": api_date_str,
        "DTAPI-Signature": signature
    }

    try:
        print(f"Запрос к API: {full_url}")
        # В производственной среде следует использовать verify=True и настроить сертификаты
        response = requests.get(full_url, headers=headers, verify=False) 
        response.raise_for_status()  # Вызовет исключение для HTTP-ошибок 4xx/5xx
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
        print(f"Тело ответа: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Ошибка соединения: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Ошибка таймаута: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON. Ответ API не является валидным JSON.")
        print(f"Статус код: {response.status_code}, Ответ: {response.text}")
    return None

# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ --- #
if __name__ == "__main__":
    print("Запуск примера получения Model Breach алертов...")

    if PUBLIC_TOKEN == "YOUR_PUBLIC_API_TOKEN" or PRIVATE_TOKEN == "YOUR_PRIVATE_API_TOKEN" or APPLIANCE_IP == "YOUR_APPLIANCE_IP_OR_HOSTNAME":
        print("\nПРЕДУПРЕЖДЕНИЕ: Пожалуйста, заполните APPLIANCE_IP, PUBLIC_TOKEN и PRIVATE_TOKEN в начале скрипта!\n")
    else:
        # Пример: получить последние 10 алертов с минимальным скором 70
        # За последние 24 часа (по умолчанию)
        alerts = get_model_breaches(
            appliance_ip=APPLIANCE_IP,
            public_token=PUBLIC_TOKEN,
            private_token=PRIVATE_TOKEN,
            limit=10,
            min_score=70
            # extra_params={"ack": "false"} # Пример дополнительного параметра
        )

        if alerts:
            print(f"\nПолучено {len(alerts)} алертов:")
            # Вывод в сокращенном виде для наглядности
            for i, alert in enumerate(alerts):
                print(f"  Алерт #{i+1}:")
                print(f"    ID (pbid): {alert.get('pbid')}")
                print(f"    Время: {datetime.fromtimestamp(alert.get('timestamp') / 1000) if alert.get('timestamp') else 'N/A'}")
                print(f"    Скор: {alert.get('score')}")
                print(f"    Описание: {alert.get('description', 'N/A')}")
                print(f"    Устройство (did): {alert.get('did')}")
                print("-" * 20)
            
            # Можно вывести и полный JSON одного из алертов для детального изучения
            # if len(alerts) > 0:
            #     print("\nПолный JSON первого алерта:")
            #     print(json.dumps(alerts[0], indent=2, ensure_ascii=False))
        else:
            print("\nАлерты не получены или произошла ошибка.")

    # Пример получения алертов за конкретный временной диапазон (прошлый час)
    # current_time_ms = int(time.time() * 1000)
    # one_hour_ago_ms = int((time.time() - 3600) * 1000)
    # print(f"\nЗапрос алертов за последний час ({one_hour_ago_ms} - {current_time_ms})...")
    # alerts_last_hour = get_model_breaches(
    #     appliance_ip=APPLIANCE_IP,
    #     public_token=PUBLIC_TOKEN,
    #     private_token=PRIVATE_TOKEN,
    #     starttime_ms=one_hour_ago_ms,
    #     endtime_ms=current_time_ms,
    #     limit=5
    # )
    # if alerts_last_hour:
    #     print(f"Получено {len(alerts_last_hour)} алертов за последний час.")
    #     # (дальнейшая обработка или вывод)
    # else:
    #     print("Алерты за последний час не получены.")

print("\nСкрипт завершил работу.") 