from datetime import datetime, timezone
from pathlib import Path

DOWNLOAD_RESULTS = False  # @param {type:"boolean"}

def json_scalar(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"Valeur non sérialisable : {type(value).__name__}")

result_path = Path("resultats") / f"tp_{RESULT['tp']:02d}.json"
result_path.parent.mkdir(exist_ok=True)
experiment = {
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "seed": SEED,
    "environment": ENVIRONMENT,
    "results": RESULT,
}
result_path.write_text(
    json.dumps(experiment, indent=2, ensure_ascii=False, default=json_scalar) + "\n",
    encoding="utf-8",
)
print("Résultats enregistrés :", result_path)

if DOWNLOAD_RESULTS:
    try:
        from google.colab import files
    except ImportError:
        print("Hors Colab, récupérer le fichier dans le dossier resultats/.")
    else:
        files.download(str(result_path))
