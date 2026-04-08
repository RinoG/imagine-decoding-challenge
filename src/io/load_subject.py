from pathlib import Path
import mne
import pandas as pd

from src.labels import load_imagine_train_labels

def load_epochs(subject_dir: Path, subject: str):
    localizer_path = subject_dir / f"{subject}_localizer-epo.fif"
    imagine_path = subject_dir / f"{subject}_imagine-epo.fif"

    localizer = mne.read_epochs(localizer_path, preload=True, verbose="ERROR")
    imagine = mne.read_epochs(imagine_path, preload=True, verbose="ERROR")
    return localizer, imagine

def subject_summary(subject_dir: Path, subject: str) -> dict:
    localizer, imagine = load_epochs(subject_dir, subject)

    return {
        "subject": subject,
        "localizer_n_epochs": len(localizer),
        "imagine_n_epochs": len(imagine),
        "localizer_shape": localizer.get_data().shape,
        "imagine_shape": imagine.get_data().shape,
        "sfreq": localizer.info["sfreq"],
        "n_channels": len(localizer.ch_names),
        "tmin_localizer": localizer.tmin,
        "tmax_localizer": localizer.tmax,
        "tmin_imagine": imagine.tmin,
        "tmax_imagine": imagine.tmax,
    }

def attach_imagine_labels(subject: str, imagine_epochs) -> pd.DataFrame:
    labels_df = load_imagine_train_labels()
    sub_df = labels_df[labels_df["subject"] == subject].copy()
    sub_df = sub_df.sort_values("trial_idx").reset_index(drop=True)

    if len(sub_df) != len(imagine_epochs):
        raise ValueError(
            f"Label count mismatch for {subject}: "
            f"{len(sub_df)} labels vs {len(imagine_epochs)} imagine epochs"
        )

    return sub_df