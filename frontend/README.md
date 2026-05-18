# Clinical Orchestrator Frontend

This is the Streamlit frontend for the Agentic Clinical Orchestrator.

## Prerequisites

- Python 3.11+
- A running backend (usually on `http://localhost:8000`)

## Installation

1. Create a virtual environment (if not already done):
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your backend URL if necessary:
   ```env
   BACKEND_URL=http://localhost:8000
   ```

## Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```
