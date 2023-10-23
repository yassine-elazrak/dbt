def model(dbt, session):
    dbt.config(
        materialized = "table",
        packages = ["numpy", "pandas"]

    )

    product_df = dbt.ref("product_codes")
    print(product_df)
    df = product_df.to_pandas()

    df["product_new"] = df["product_code"]

    return df