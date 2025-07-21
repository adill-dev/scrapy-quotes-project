
# 📚 Scrapy Quotes Crawler

This project is a simple **web scraper** built using [Scrapy](https://scrapy.org/) that extracts quotes and author information from [quotes.toscrape.com](https://quotes.toscrape.com/).

## 🚀 Features

- Crawls quotes from the main and paginated pages
- Follows author profile links
- Scrapes the following author details:
  - Full name
  - Date of birth
  - Short biography
- Supports exporting scraped data to JSON, CSV, or XML

## 📁 Project Structure

```
scrapy_quotes/
├── scrapy_quotes/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── author_spider.py
├── scrapy.cfg
```

## 🕷 Spider Details

### `author_spider.py`

- **Spider Name**: `author`
- **Start URL**: `https://quotes.toscrape.com/`
- **Extracts** author links and paginated quote pages using CSS selectors
- For each author, it scrapes:
  - `name` – full name of the author
  - `dob` – date of birth
  - `bio` – short biography

### 🧪 Example Extracted Data

```json
{
  "name": "Albert Einstein",
  "dob": "March 14, 1879",
  "bio": "Lorem ipsum author biography..."
}
```

## 🧪 How to Run the Spider

### Install Scrapy (if not already installed):

```bash
pip install scrapy
```

### Navigate to your project directory:

```bash
cd scrapy_quotes
```

### Run the spider and export data:

```bash
scrapy crawl author -o authors.json
```

Supported formats: `.json`, `.csv`, `.xml`, etc.

## 🧱 Requirements

- Python 3.7 or higher
- Scrapy (tested on Scrapy 2.13.3)

### Install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, just install Scrapy directly using:

```bash
pip install scrapy
```
