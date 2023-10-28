import re

from tqdm import tqdm

from .paths import CLEAR_TXT_DIR, RAW_TXT_DIR

# Впишите нужное здесь:
SUBSTITUTIONS = [
    (r"...", "..."),
    (r"...", "..."),
    (r"...", "..."),
    ... ,
]

def clear_text(text: str) -> str:
    """Очистить один текст."""
    # Поочерёдно выполнить все замены из списка.
    for regex, replacement in SUBSTITUTIONS:
        text = re.sub(regex, replacement, text)
    return text

def clear_texts() -> None:
    """
    Очистить все тексты из папки с сырыми текстами.
    Сохранить одноименные файлы в папку с очищенными текстами.
    """
    # RAW_TXT_DIR существует и является директорией (не файлом)
    if not RAW_TXT_DIR.is_dir():
        raise NotADirectoryError(RAW_TXT_DIR)
    CLEAR_TXT_DIR.mkdir(parents=True, exist_ok=True)

    # Итератор чисел с индикатором выполнения
    iterator = tqdm(range(1, 77))

    for i in iterator:
        src_path = RAW_TXT_DIR / f"Глава_{i}.html"
        dst_path = CLEAR_TXT_DIR / f"Глава_{i}.txt"

        if not src_path.is_file():
            raise FileNotFoundError(src_path)

        with src_path.open("r", encoding="utf-8") as file:
            text = file.read()

        text = clear_text(text)

        with dst_path.open("w", encoding="utf-8") as file:
            file.write(text)
