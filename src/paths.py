from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

TRAIN_DIR = RAW_DIR / "train"
TEST_DIR = RAW_DIR / "test"
IMAGINE_LABELS_CSV = RAW_DIR / "labels_imagine-train.csv"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"