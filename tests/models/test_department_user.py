# -*- coding: utf-8 -*-
# Stalker a Production Asset Management System
# Copyright (C) 2009-2016 Erkan Ozgur Yilmaz
#
# This file is part of Stalker.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation;
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import unittest
from stalker import DepartmentUser


class DepartmentUserTestCase(unittest.TestCase):
    """tests for DepartmentUser class
    """

    def test_role_argument_is_not_a_role_instance(self):
        """testing if a TypeError will be raised when the role argument is not
        a Role instance
        """
        from stalker import Department, User

        with self.assertRaises(TypeError) as cm:
            DepartmentUser(
                department=Department(name='Test Department'),
                user=User(
                    name='Test User',
                    login='tuser',
                    email='u@u.com',
                    password='secret'
                ),
                role='not a role instance'
            )

        self.assertEqual(
            str(cm.exception),
            'DepartmentUser.role should be a stalker.models.auth.Role '
            'instance, not str'
        )
