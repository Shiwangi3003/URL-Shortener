# URL Shortener

A simple Python-based web app to shorten long URLs into short, shareable links.

## Features
- Shortens long URLs
- Redirects short URLs to their original links
- Easy to set up and run locally or deploy online

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Shiwangi3003/URL-Shortener.git
   ```
2. Navigate to the folder:
   ```bash
   cd URL-Shortener
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the app:
```bash
python main.py
```

Then open your browser and go to:
```
http://localhost:8000/
```
Enter a long URL and get a shortened one instantly.

---

## Available Routes

| Route | Method | Description |
|--------|--------|-------------|
| `/shorturl?req=<long_url>` | GET | Creates and returns a short URL for the given link |
| `/<short_code>` | GET | Redirects to the original long URL |

### Example Usage
- **Shorten a URL:**
  ```
  https://url-shortener-2q3m.onrender.com/shorturl?req=https://www.example.com
  ```
  → Response:
  ```
  Short URL: https://url-shortener-2q3m.onrender.com/abc123
  ```

- **Redirect using short link:**
  ```
  https://url-shortener-2q3m.onrender.com/abc123
  ```
  → Redirects to https://www.example.com

---

## Author
**Shiwangi**  
[GitHub Profile](https://github.com/Shiwangi3003)
