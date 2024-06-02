# Stock Data Ingestion and Visualization

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Overview](#overview)
- [Schema](#schema)
- [Author](#author)
- [Acknowledgements](#Acknowledgements)

## Introduction
This Data Engineering project aims to **ingest, transform, and visualize** the data of 3 popular ETFs, SPY, DIA, and QQQ via a fully functional data pipeline. The data includes various metrics such as price, trading volume, intraday volatility, and percentage changes relative to 52-week highs and lows. The project primarily utilizes a variety of AWS products and Grafana for data visualization. The goal is to provide insightful visualizations using Grafana to help investors and analysts make informed decisions.

## Architecture
![architecture_diagram](https://github.com/Tongaonkar/stock-data-aws-project/assets/97370881/4d6b6cfd-2a5b-445b-a9a2-8aa7ab7e7d72)
_Image Credit: David Freitag_

The image above represents the data pipeline from start to finish.

## Overview
The first step in the program is an **External API** request from [stockdata.org](https://www.stockdata.org/). This is done with a **Lambda** function that is automated with scheduling via **Eventbridge**. Next, the data is ingested by a **Kinesis Firehose**, and delivered into an **S3 Bucket**. From there, a **Glue Crawler** crawls through the landed data, identifying table schemas and partitions, as well as creating a table in Athena automatically. After the data is crawled, a series of **Glue Jobs** are executed, and data is transformed via SQL statements in Python wrappers. Notably, all job runs are logged and errors are stored in **CloudWatch** logs. The Crawler and Jobs are orchestrated through **Glue Workflows**, and the jobs will only run on the contingency of success from the previous job. A successful iteration of a Glue Workflow yields a "prod" table that is accessible through **Athena**. Athena is connected as a data source in **Grafana**, where data visualizations are created with SQL, and the completed dashboard is accessible.

## Schema
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

  
## Author

- [@Tongaonkar](https://www.github.com/Tongaonkar)

## Acknowledgements

 - [Build Your First Serverless Data Engineering Project Course](https://maven.com/david-freitag/first-serverless-de-project)
 - [StockData.org API](https://www.stockdata.org/)
 - [Grafana Dashboards](https://grafana.com/)
