"""
# Reserved admin

Create a regular expression that matches if for the following words:

- Admin
- admin
"""

import re

pattern = re.compile('(admin|Admin)')
is_Admin_matched = pattern.match('Admin')
print('\'Admin\' test:', is_Admin_matched)
is_admin_matched = pattern.match('admin')
print('\'admin\' test:', is_admin_matched)
is_cdmin_matched = pattern.match('cdmin')
print('\'cdmin\' test:', is_cdmin_matched)
is_dmin_matched = pattern.match('dmin')
print('\'dmin\' test:', is)
