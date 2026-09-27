# Cellule autonome : les bibliothèques déjà présentes dans Colab sont conservées.
import importlib.util
import json
import os
import platform
import subprocess
import sys

DEPENDENCIES = {
    "numpy": "numpy==2.2.6",
    "sklearn": "scikit-learn==1.7.2",
    "torch": "torch==2.8.0",
    "matplotlib": "matplotlib==3.10.6",
}
missing = [pin for module, pin in DEPENDENCIES.items()
           if importlib.util.find_spec(module) is None]
if missing:
    print("Installation des bibliothèques absentes :", ", ".join(missing))
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *missing])

import matplotlib
import numpy as np
import sklearn
import torch

ENVIRONMENT = {
    "runtime": "google-colab" if "google.colab" in sys.modules or "COLAB_RELEASE_TAG" in os.environ else "python-local-ou-ci",
    "python": platform.python_version(),
    "numpy": np.__version__,
    "scikit_learn": sklearn.__version__,
    "torch": torch.__version__,
    "matplotlib": matplotlib.__version__,
    "device": "cpu",
    "cuda_available": torch.cuda.is_available(),
}
print(json.dumps(ENVIRONMENT, indent=2, ensure_ascii=False))
print("Les cinq TP utilisent le CPU, même si un GPU est disponible.")
