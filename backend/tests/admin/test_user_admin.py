from django.test import TestCase

import pytest

from ..factories import UserFactory
from ..mixins import AdminTests

pytestmark = pytest.mark.django_db


class UserAdminTests(AdminTests, TestCase):
    factory_class = UserFactory  # type: ignore
    query_count = 7
