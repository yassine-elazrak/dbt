import dateutil
import pandas


def try_dateutil_parse(x):
    try:
        return dateutil.parser.parse(x)
    except:
        return


def model(dbt, session):
    dbt.config(
        materialized = "table",
        packages = ["numpy", "pandas"]

    )
    df = dbt.ref("source_data").to_df()

    df['parsed_transaction_time'] = df['transaction_time']
    # .apply(try_dateutil_parse)

    return df
