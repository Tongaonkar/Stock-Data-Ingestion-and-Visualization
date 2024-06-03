import boto3

client = boto3.client('athena')

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = """
    CREATE TABLE stock_data_parquet_tbl
    WITH (
        external_location = 's3://stock-data-parquet-bucket/',
        format = 'PARQUET',
        write_compression = 'SNAPPY',
        partitioned_by = ARRAY['row_ts']
    )
    AS
    SELECT DISTINCT
        ticker,
        price,
        day_high AS day_price_high,
        day_low AS day_price_low,
        day_open AS day_price_open,
        ROUND((day_high + day_low) / 2, 2) AS day_price_median,
        ROUND((day_high - day_low), 2) AS day_price_range,
        ROUND((day_high - day_low) / day_open * 100, 2) AS intraday_volatility,
        ROUND(((price - previous_close_price) / previous_close_price) * 100, 2) AS price_change_percentage,
        ROUND((1 - (price / "52_week_high")) * 100, 2) AS "Percentage_below_52_week_high",
        ROUND(((price / "52_week_low") - 1) * 100, 2) AS "Percentage_above_52_week_low",
        volume,
        row_ts
    FROM "de_project_database"."stock_data_bucket_may_2024";
    """,
    QueryExecutionContext={
        'Database': 'de_project_database'
    },
    ResultConfiguration={
        'OutputLocation': 's3://stock-query-results-location-de-project'
    }
)
