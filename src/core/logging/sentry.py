import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from src.config import settings


def init_sentry():
    if settings.SENTRY_DSN:
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            integrations=[
                FastApiIntegration(),
                StarletteIntegration(),
                SqlalchemyIntegration(),
            ],
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
        )
