import pandas as pd
from src.paths import IMAGINE_LABELS_CSV

def load_imagine_train_labels() -> pd.DataFrame:
    df = pd.read_csv(IMAGINE_LABELS_CSV)
    df["subject"] = df["subject"].astype(str)
    df["trial_idx"] = df["trial_idx"].astype(int)
    return df

def make_imagine_id(subject: str, trial_idx: int) -> str:
    return f"{subject}_{trial_idx}"