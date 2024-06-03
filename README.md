# Stock Data Ingestion and Visualization Project 📈

## Table of Contents 📚
- [Introduction](#introduction-)
- [Architecture](#architecture-)
- [Overview](#overview-)
- [Schema](#schema%EF%B8%8F)
- [Dashboard](#dashboard-)
- [Author](#author-%EF%B8%8F)
- [Acknowledgements](#acknowledgements-)

## Introduction 🌐
This Data Engineering project aims to **ingest, transform, and visualize** the data of 3 popular ETFs, SPY, DIA, and QQQ via a fully functional data pipeline. The data includes various metrics such as price, trading volume, intraday volatility, and percentage changes relative to 52-week highs and lows. The project primarily utilizes a variety of AWS products and Grafana for data visualization. The goal is to provide insightful visualizations using Grafana to help investors and analysts make informed decisions.

## Architecture 📐
![architecture_diagram](https://github.com/Tongaonkar/stock-data-aws-project/assets/97370881/4d6b6cfd-2a5b-445b-a9a2-8aa7ab7e7d72)
_Image Credit: David Freitag_

The diagram above represents the data pipeline from start to finish.

## Overview 📋
![Screenshot 2024-06-02 173859](https://github.com/Tongaonkar/Stock-Data-Ingestion-and-Visualization/assets/97370881/0f6d7da8-6786-427c-873c-d2e1bb0f4029)
_StockData.org API_

The first step in the program is an **External API** request from [StockData.org](https://www.stockdata.org/). This is done with a **Lambda** function that is automated with **Eventbridge** scheduling.


![Screenshot 2024-06-02 175237](https://github.com/Tongaonkar/Stock-Data-Ingestion-and-Visualization/assets/97370881/28f865d0-063b-4f02-aafc-681297294dfd)
_Contents of S3 Bucket after Firehose Ingestion_

Next, the data is ingested by a **Kinesis Firehose**, and delivered into an **S3 Bucket**. From there, a **Glue Crawler** crawls through the landed data, identifying table schemas and partitions, as well as creating a table in Athena automatically.


![Screenshot 2024-05-31 170727](https://github.com/Tongaonkar/Stock-Data-Ingestion-and-Visualization/assets/97370881/62b3be25-411d-497e-9c23-e4c2deb3b98e)
_Project Workflow_

After the data is crawled, a series of **Glue Jobs** are executed, and data is transformed via SQL statements in Python wrappers. Notably, all job runs are logged and errors are stored in **CloudWatch** logs. The Crawler and Jobs are orchestrated through **Glue Workflows**, and the jobs will only run on the contingency of success from the previous job.


![Screenshot 2024-06-02 151602](https://github.com/Tongaonkar/Stock-Data-Ingestion-and-Visualization/assets/97370881/747ecbf5-da98-457f-ab44-0166987d0588)
_Query of stock_data_parquet_tbl_prod_

A successful iteration of a Glue Workflow produces a "prod" table that is queryable through **Athena**. Athena is connected as a data source in **Grafana**, where data visualizations are created with SQL, and the completed dashboard is accessible.

## Schema🗄️
- `ticker`: Stock ticker symbol (e.g., SPY, QQQ, DIA)
- `price`: Current price
- `day_price_high`: Highest price of the day
- `day_price_low`: Lowest price of the day
- `day_price_open`: Opening price of the day
- `day_price_median`: Median price of the day
- `day_price_range`: Range of prices throughout the day
- `intraday_volatility`: Measure of price fluctuation within the day
- `price_change_percentage`: Daily percentage change in price
- `Percentage_below_52_week_high`: Percentage below the 52-week high price
- `Percentage_above_52_week_low`: Percentage above the 52-week low price
- `volume`: Trading volume
- `row_ts`: Timestamp of the data row

## Dashboard 📊
![image](https://github.com/Tongaonkar/stock-data-aws-project/assets/97370881/444e834f-4cff-4cbc-8f7b-b4ea6a489290)
_Complete Grafana Dashboard, 6/2/2024_

The completed Grafana Dashboard displays visualizations of volume, intraday volatility, price change percentage, percentage below 52-week high, percentage above 52-week low, and the day price range.
  
## Author ✍️

- [@Tongaonkar](https://www.github.com/Tongaonkar)

## Acknowledgements 👏

 - [Build Your First Serverless Data Engineering Project Course](https://maven.com/david-freitag/first-serverless-de-project)
 - [StockData.org API](https://www.stockdata.org/)
 - [Grafana Dashboards](https://grafana.com/)
