from ..backend import database

admins = database.root.admins
for a in admins:
    admin = admins[a]
    print(admin.get_email())
import sys
print(sys.path)
