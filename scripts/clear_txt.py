import re
from pathlib import Path

from tqdm import tqdm

from .paths import CLEAR_TXT_DIR, RAW_TXT_DIR

# _________________________________________
# решил добавить скрипт который удаляет все строчки после
# "Категория:" тк дальше там идет мусор

# Путь к папке с файлами
folder_path = Path("/Users/gleb/Desktop/py/legal_code/clear_txt")

# Шаблон для поиска строк
pattern = r"Категория:.*"
# Поиск всех файлов .txt в папке
txt_files = folder_path.glob("*.txt")
for file in txt_files:
    with Path.open(file) as f:
        content = f.read()
    # Удаление строк после "Категория:"

    new_content = re.sub(pattern, "", content, flags=re.DOTALL)

    with Path.open(file, "w") as f:
        f.write(new_content)
# _________________________________________
#rvrvrvrvr
# 3d33
# Впишите нужное здесь:
SUBSTITUTIONS = [
    (r"\[править\]", ""),
    (r"Это произведение не охраняется авторским правом\..*", ""),
    (r"Источник — https://.*", ""),
    (r"←.*", ""),
    (r"Скачать", ""),
    (r".*Викитек\w", ""),
    (r"Перейти.*", ""),
    (r"<.*", ""),
    (r".*свободной биб\w*", ""),
    (r"\n{3,}", "\n\n"),
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
        src_path = RAW_TXT_DIR / f"Глава_{i}.txt"
        dst_path = CLEAR_TXT_DIR / f"Глава_{i}.txt"

        if not src_path.is_file():
            raise FileNotFoundError(src_path)

        with src_path.open("r", encoding="utf-8") as file:
            text = file.read()

        text = clear_text(text)

        with dst_path.open("w", encoding="utf-8") as file:
            file.write(text)
