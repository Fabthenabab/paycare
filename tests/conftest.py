import pytest
import pandas as pd
from io import StringIO
import os


@pytest.fixture
def sample_csv_file(tmp_path):
    """Crée un fichier CSV temporaire valide pour les tests."""
    file_path = tmp_path / "test_data.csv"
    df_test = pd.DataFrame({"col1": [1, 2, 3], "col2": ["A", "B", "C"]})
    df_test.to_csv(file_path, index=False)
    return file_path  # Retourne le chemin du fichier


@pytest.fixture
def empty_csv_file(tmp_path):
    """Crée un fichier CSV vide."""
    file_path = tmp_path / "empty.csv"
    file_path.touch()  # Crée un fichier vide
    return file_path

@pytest.fixture
def sample_data():
    """Crée un DataFrame exemple pour tester le prétraitement des données."""
    data = pd.DataFrame({
        'employee_id': [101, 102],
        'employee_name': ['Alice', 'Bob'],
        'salary': [5000, 6000]
    })
    return pd.DataFrame(data)