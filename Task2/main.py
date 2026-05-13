import random
import logging
import requests
from typing import Tuple

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

class HTTPErrorException(Exception):
    def __init__(self, status_code: int, url: str, response_body: str):
        self.status_code = status_code
        self.url = url
        self.response_body = response_body
        super().__init__(f"HTTP {status_code} ошибка при запросе к {url}")


def make_request(url: str, timeout: int = 10) -> Tuple[int, str]:
    try:

        response = requests.get(url, timeout=timeout)
        status_code = response.status_code
        body = response.text.strip()

        if 100 <= status_code < 400:

            logger.info(f"  Статус: {status_code}")
            logger.info(f"  URL: {url}")
            logger.info(
                f"  Тело ответа: {body[:500]}{'...' if len(body) > 500 else ''}"
            )
            return status_code, body

        elif 400 <= status_code < 600:

            logger.error(f" Статус: {status_code}")
            logger.error(f" URL: {url}")
            logger.error(
                f" Тело ответа: {body[:500]}{'...' if len(body) > 500 else ''}"
            )
            raise HTTPErrorException(status_code, url, body)

    except requests.exceptions.Timeout:

        logger.error(f"Таймаут при запросе к {url}")
        raise


def main():

    base_url = "https://tools-httpstatus.pickup-services.com"

    test_requests = [
        {"code": 100},
        {"code": 101},
        {"code": 102},
        {"code": 103},
        {"code": 200},
        {"code": 201},
        {"code": 202},
        {"code": 203},
        {"code": 204},
        {"code": 205},
        {"code": 206},
        {"code": 207},
        {"code": 208},
        {"code": 226},
        {"code": 300},
        {"code": 301},
        {"code": 302},
        {"code": 303},
        {"code": 304},
        {"code": 305},
        {"code": 306},
        {"code": 307},
        {"code": 308},
        {"code": 400},
        {"code": 401},
        {"code": 402},
        {"code": 403},
        {"code": 404},
        {"code": 405},
        {"code": 406},
        {"code": 407},
        {"code": 408},
        {"code": 409},
        {"code": 410},
        {"code": 411},
        {"code": 412},
        {"code": 413},
        {"code": 414},
        {"code": 415},
        {"code": 416},
        {"code": 417},
        {"code": 418},
        {"code": 421},
        {"code": 422},
        {"code": 423},
        {"code": 424},
        {"code": 425},
        {"code": 426},
        {"code": 428},
        {"code": 429},
        {"code": 431},
        {"code": 451},
        {"code": 419},
        {"code": 420},
        {"code": 440},
        {"code": 444},
        {"code": 449},
        {"code": 450},
        {"code": 460},
        {"code": 463},
        {"code": 494},
        {"code": 495},
        {"code": 496},
        {"code": 497},
        {"code": 498},
        {"code": 499},
        {"code": 500},
        {"code": 501},
        {"code": 502},
        {"code": 503},
        {"code": 504},
        {"code": 505},
        {"code": 506},
        {"code": 507},
        {"code": 508},
        {"code": 510},
        {"code": 511},
        {"code": 520},
        {"code": 521},
        {"code": 522},
        {"code": 523},
        {"code": 524},
        {"code": 525},
        {"code": 526},
        {"code": 527},
        {"code": 530},
        {"code": 561},
    ]

    logger.info("Скрипт запущен")

    random_codes = random.sample(test_requests, 5)
    results = []

    for i, test in enumerate(random_codes, 1):
        url = f"{base_url}/{test['code']}"
        logger.info(f"URL: {url}")

        try:

            make_request(url)

        except HTTPErrorException as e:

            logger.exception(f"ИСКЛЮЧЕНИЕ: {str(e)}")
            results.append(
                {
                    "request": i,
                    "url": url,
                    "status_code": e.status_code,
                    "success": False,
                    "error": str(e),
                }
            )

        except requests.exceptions.RequestException as e:

            logger.exception(f"СЕТЕВАЯ ОШИБКА: {str(e)}")
            results.append(
                {
                    "request": i,
                    "url": url,
                    "status_code": None,
                    "success": False,
                    "error": str(e),
                }
            )


if __name__ == "__main__":
    main()
