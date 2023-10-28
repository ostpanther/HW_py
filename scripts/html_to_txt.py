import bs4
from tqdm import tqdm

from .paths import HTML_DIR, RAW_TXT_DIR


def html_to_txt() -> None:
    """Извлечь текст из html-файлов и сохранить в одноименные txt-файлы."""
    # HTML_DIR существует и является директорией (не файлом)
    if not HTML_DIR.is_dir():
        raise NotADirectoryError(HTML_DIR)
    RAW_TXT_DIR.mkdir(parents=True, exist_ok=True)

    # Итератор чисел с индикатором выполнения
    iterator = tqdm(range(1, 77))

    for i in iterator:
        html_path = HTML_DIR / f"Глава_{i}.html"
        txt_path = RAW_TXT_DIR / f"Глава_{i}.txt"

        if not html_path.is_file():
            raise FileNotFoundError(html_path)

        with html_path.open("r", encoding="utf-8") as file:
            soup = bs4.BeautifulSoup(file, "html.parser")

        with txt_path.open("w", encoding="utf-8") as file:
            file.write(soup.text)
