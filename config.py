import os

SEED = 42
IMG_FLAT = 64
IMG_CNN = 224

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "dataset", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "dataset","processed")
FEATURES_DIR = os.path.join(BASE_DIR, "features")
MODELS_DIR = os.path.join(BASE_DIR, "models")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
MANIFEST_DIR = os.path.join(BASE_DIR, "manifest.csv")
