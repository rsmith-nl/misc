# From: https://stackoverflow.com/a/73514522/1219295
# Provides information about the sqlite module in python.
import sqlite3
import pprint


con = sqlite3.connect(":memory:")
cur = con.cursor()

meta_scalar_sql = {
    "sqlite_version": "SELECT sqlite_version();",
    "sqlite_source_id": "SELECT sqlite_source_id();",
    "function_count": "SELECT count(*) FROM pragma_function_list();",
    "module_count": "SELECT count(*) FROM pragma_module_list();",
    "collation_count": "SELECT count(*) FROM pragma_collation_list();",
    "pragma_count": "SELECT count(*) FROM pragma_pragma_list();",
}

for item, query in meta_scalar_sql.items():
    print(item + " " * (25 - len(item)) + str(cur.execute(query).fetchone()[0]))

meta_list_sql = {
    "compile_options": "SELECT * FROM pragma_compile_options() ORDER BY compile_options;",
    "function_list": "SELECT name || '__' || narg AS name FROM pragma_function_list() ORDER BY name;",
    "module_list": "SELECT * FROM pragma_module_list() ORDER BY name;",
    "pragma_list": "SELECT * FROM pragma_pragma_list() ORDER BY name;",
    "collation_list": "SELECT name FROM pragma_collation_list();",
}

pp = pprint.PrettyPrinter(indent=4)
for item, query in meta_list_sql.items():
    pp.pprint(item + " " * (25 - len(item)))
    metas = cur.execute(query).fetchall()
    pp.pprint([metas[i][0] for i in range(len(metas))])

cur.close()
con.close()
