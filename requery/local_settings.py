# *-* coding:utf-8 *-*
from django.conf import settings


SQL_STATEMENTS_NOT_ALLOWED = getattr(settings, 'SQL_STATMENTS_NOT_ALLOWED', (
    'DEFINE',
    'CREATE',
    'DROP',
    'INSERT',
    'UPDATE',
    'DELETE',
    'TRUNCATE',
    'GRANT',
    )
)

