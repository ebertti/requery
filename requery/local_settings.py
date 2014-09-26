# coding=utf-8
from django.conf import settings

# Define here statements that are not allowed in the querys you will run.
# Queries that contains this statements still can be stored by requery.
SQL_STATEMENTS_NOT_ALLOWED = getattr(settings, 'SQL_STATMENTS_NOT_ALLOWED', (

    )
)

