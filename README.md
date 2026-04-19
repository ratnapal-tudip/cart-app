# Cart App

## Pre-requisite :

- Python >= 3.8
- git

## Installation:

**Step 1**: Clone the repository

```bash
git clone https://github.com/ratnapal-tudip/cart-app.git
```

```
cd cart-app
```

**Step 2**:  Create Virtual Environment

```bash
# Ubuntu
python3 -m venv .venv
source .venv/bin/activate
```


**Step 3**:  Install dependencies

```bash
pip install -r requirements.txt
```

## Running the app:


```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Visit http://localhost:8000 to see the app.