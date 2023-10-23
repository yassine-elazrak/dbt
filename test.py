import duckdb

with duckdb.connect('/Users/yassine-elazrak/goinfre/dbt/jaffle_shop/duckdb_test/test.duckdb') as con:
    # con.sql('CREATE TABLE test(i INTEGER)')
    # con.sql('INSERT INTO test VALUES (42)')
    print(con.sql("SELECT name FROM sqlite_master WHERE type='table'").show())
    print(con.table('product_codes').show())
    print(con.table('transactions').show())
    print(con.table('transformed_product_codes').show())
    # list all tables 
    # the context manager closes the connection automaticallytransformed_product_codes