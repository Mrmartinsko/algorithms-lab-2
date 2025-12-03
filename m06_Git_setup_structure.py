"""
Vytvoří základní adresářovou strukturu pro projekt, např. algorithms-lab
včetně prázdných souborů podle zadání.
Stačí spustit jednou z kořenového adresáře, kde chceš nový projekt.
Vlastnosti:
    - Nevytváří žádné konflikty s existujícími soubory.
    - Prázdné soubory budou obsahovat případně jen komentář.
"""

import os
from pathlib import Path

# modifikuj název kořenového adresáře projektu a dále pak adresáře a soubory níže
# -----------------------------
BASE = "algorithms-lab-2"
# -----------------------------


def make_structure(base_dir: str = BASE) -> None:
    """
    Vytvoří adresáře a základní soubory pro projekt algorithms-lab.

    Args:
        base_dir: Název kořenového adresáře projektu.
    """
    # Definice potřebných adresářů a souborů
    # ======================================================
    dirs = [
        f"{base_dir}/src",
        f"{base_dir}/tests",
        f"{base_dir}/.github/workflows"
    ]
    files = {
        f"{base_dir}/src/__init__.py": "# Init",
        f"{base_dir}/src/algorithms.py": "",
        f"{base_dir}/tests/__init__.py": "# Init",
        f"{base_dir}/tests/test_algorithms.py": "",
        f"{base_dir}/.github/workflows/ci.yml": "",
        f"{base_dir}/requirements.txt": "",
        f"{base_dir}/.gitignore": "",
        f"{base_dir}/README.md": "# algorithms-lab\n"
    }
    # ======================================================
    
    # Vytvoření adresářů
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

    # Vytvoření souborů se základem
    for path, content in files.items():
        file_path = Path(path)
        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Vytvořen soubor: {file_path}")
        else:
            print(f"Soubor {file_path} již existuje.")

if __name__ == "__main__":
    make_structure()  # Defaultně vytváří ve složce algorithms-lab
