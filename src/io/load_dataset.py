from pathlib import Path
import pandas as pd

from src.paths import TRAIN_DIR, TEST_DIR
from src.io.load_subject import subject_summary

def list_subjects(split: str) -> list[str]:
    base_dir = TRAIN_DIR if split == "train" else TEST_DIR
    return sorted([p.name for p in base_dir.iterdir() if p.is_dir() and p.name.startswith("sub-")])

def build_subject_summary(split: str) -> pd.DataFrame:
    base_dir = TRAIN_DIR if split == "train" else TEST_DIR
    rows = []
    for subject in list_subjects(split):
        rows.append(subject_summary(base_dir / subject, subject))
    return pd.DataFrame(rows)