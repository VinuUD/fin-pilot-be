


# FinPilot Backend

FinPilot is a backend API built with FastAPI to support strategy simulation, saving, and management for the FinPilot frontend application. It handles validation, persistence, and data operations related to investment strategies.

## Getting Started

To set up and run the backend locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-org/fin-pilot-be.git
cd fin-pilot-be
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.