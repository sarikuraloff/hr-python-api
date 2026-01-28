from datetime import datetime, date
from typing import Optional, Union


# -------------------------------------------------
# ДАТЫ
# -------------------------------------------------
def parse_date(value: str) -> Optional[date]:
    """
    Принимает строку, пытается распарсить дату.
    Возвращает datetime.date или None.
    """
    if not value:
        return None

    value = value.strip()

    formats = [
        "%d.%m.%Y",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%Y-%m-%d",
        "%d.%m.%y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    # попытка из цифр: 01012024
    digits = "".join(ch for ch in value if ch.isdigit())
    if len(digits) == 8:
        try:
            return datetime.strptime(digits, "%d%m%Y").date()
        except ValueError:
            pass

    return None


def validate_date_range(d1: date, d2: date) -> Optional[str]:
    """
    Проверяет корректность диапазона дат.
    Возвращает None если всё ок, иначе текст ошибки.
    """
    if d2 < d1:
        return "❌ Дата увольнения не может быть раньше даты приёма."

    if d2 > date.today():
        return "⚠️ Дата увольнения в будущем. Проверьте ввод."

    return None


# -------------------------------------------------
# ЧИСЛА
# -------------------------------------------------
def parse_int(value: str, field_name: str) -> Union[int, str]:
    """
    Парсит целое число >= 0.
    Возвращает int или строку ошибки.
    """
    try:
        v = int(value)
    except (TypeError, ValueError):
        return f"❌ {field_name}: введите целое число."

    if v < 0:
        return f"❌ {field_name}: значение не может быть отрицательным."

    if v > 1000:
        return f"⚠️ {field_name}: слишком большое значение."

    return v


def parse_float(value: str, field_name: str) -> Union[float, str]:
    """
    Парсит число с плавающей точкой >= 0.
    Возвращает float или строку ошибки.
    """
    try:
        v = float(value.replace(",", "."))
    except (TypeError, ValueError):
        return f"❌ {field_name}: введите число."

    if v < 0:
        return f"❌ {field_name}: значение не может быть отрицательным."

    if v > 1000:
        return f"⚠️ {field_name}: слишком большое значение."

    return v
