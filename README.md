# Stock Data Analysis and Visualization

![Project Banner](path/to/banner/image) <!-- Optional -->

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Columns](#data-columns)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Grafana Dashboards](#grafana-dashboards)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is designed to analyze and visualize stock data for SPY, QQQ, and DIA. The data includes various metrics such as price, trading volume, intraday volatility, and percentage changes relative to 52-week highs and lows. The goal is to provide insightful visualizations using Grafana to help investors and analysts make informed decisions.

## Features
- Fetches and processes stock data from a specified API.
- Stores processed data in AWS S3.
- Uses AWS Glue and Athena for ETL (Extract, Transform, Load) operations.
- Visualizes data with Grafana dashboards.

## Technologies Used
- **Programming Language**: Python
- **Data Storage**: AWS S3
- **Data Processing**: AWS Glue, AWS Athena
- **Visualization**: Grafana
- **Others**: AWS Lambda, AWS Kinesis Firehose

## Data Columns
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

## Setup and Installation

### Prerequisites
- Python 3.x
- AWS CLI configured with appropriate permissions
- Grafana installed and configured

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/stock-data-analysis.git
   cd stock-data-analysis
