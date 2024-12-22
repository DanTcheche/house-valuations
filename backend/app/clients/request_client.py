from abc import ABC
import logging
from typing import Any, Optional, Tuple

import requests

from app.core.config import settings

from app.core.config import get_settings

settings = get_settings()

logger = logging.getLogger(__name__)


class RequestClient:
    base_url: Optional[str] = None

    def make_request(
        self,
        endpoint: str,
        method: str,
        headers: Optional[dict] = None,
        data: dict | str | None = None,
        files: Optional[list] = None,
        params: Optional[dict] = None,
        auth: Optional[Tuple[str, str]] = None,
    ) -> Any | None:
        try:
            response = requests.request(
                method=method,
                url=(
                    f"{self.base_url}{endpoint}" if self.base_url else endpoint
                ),
                headers=headers,
                data=data,
                files=files,
                params=params,
                auth=auth,
                timeout=settings.REQUESTS_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as error:
            logger.error(str(endpoint))
            logger.error(str(error))
            logger.error(str(data))
            logger.error(str(params))
            logger.error(
                f"response: {error.response.text if error.response else None}"
            )
            return None
