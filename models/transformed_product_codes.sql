SELECT
    product_code,
    product_name,
    CONCAT(product_code, ' - ', product_name) AS concatenated_column
FROM {{ ref('product_codes') }}
