from pathlib import Path

PROJECT_ROOT  = Path(__file__).resolve().parent.parent
 # __file__ store holds the location of the file src/config.py  
 # Path converts it into a object
 # resolve() converts it into a full abosolutte path 
 # .parent points to the parernt of the currnet folder and again .parent points to the root of the repo 
 
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw" / "HUST bearing dataset"
INTERIM_DIR = DATA_DIR / "interim"
SIGNALS_DIR = INTERIM_DIR / "signals"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
MODELS_DIR = PROJECT_ROOT / "models"

SAMPLE_RATE_HZ = 51_200

WINDOW_SECONDS = 1.0
WINDOW_OVERLAP = 0.5
WINDOW_SIZE = int(SAMPLE_RATE_HZ * WINDOW_SECONDS)
WINDOW_STEP = int(WINDOW_SIZE * (1 - WINDOW_OVERLAP))