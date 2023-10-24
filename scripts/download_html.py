import requests
from requests.exceptions import RequestException
from tqdm import tqdm

from .paths import HTML_DIR

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200
STATUS_OK = requests.status_codes.codes["ok"]


def download_html() -> None:
    """Скачать веб-страницы с главами 'Гражданского кодекса РФ'."""
    HTML_DIR.mkdir(parents=True, exist_ok=True)

    # Итератор чисел с индикатором выполнения
    iterator = tqdm(range(1, 77))

    for i in iterator:
        # Скачивание страницы
        url = f"https://ru.wikisource.org/wiki/Гражданский_кодекс_РФ/Глава_{i}"
        page = requests.get(url, timeout=3)
        if page.status_code != STATUS_OK:
            raise RequestException(url)
        # Сохранение в файл
        html_path = HTML_DIR / f"Глава_{i}.html"
        with html_path.open("w", encoding="utf-8") as file:
            file.write(page.text)
