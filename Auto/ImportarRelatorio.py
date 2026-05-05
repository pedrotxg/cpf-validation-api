import time
import pandas as pd
import pyodbc
import os

import sys
sys.path.insert(0,"")

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.Claro.services import remover_todos_socios


ARQUIVO = os.getenv('PATH_IMPORT')
CHUNK_SIZE = 100000

def importar_arquivo():
    inicio_total = time.perf_counter()

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={os.getenv('DB_HOST')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "TrustServerCertificate=yes;"
    )

    cursor = conn.cursor()
    cursor.fast_executemany = True

    sql = f"""
INSERT INTO {os.getenv("TB_CLIENTE")}
(
    data_insercao,
    data_ultimo_update,
    col1,
    col2,
    cpf
)
VALUES
(
    GETDATE(),
    GETDATE(),
    ?,
    ?,
    ?
)
    """

    total_importado = 0

    leitor = pd.read_csv(
        ARQUIVO,
        sep=";",
        header=None,
        names=["col1", "col2", "cpf"],
        dtype=str,
        chunksize=CHUNK_SIZE,
        encoding="utf-8"
    )

    for numero_lote, df in enumerate(leitor, start=1):
        inicio_lote = time.perf_counter()

        df = df.fillna("")

        dados = [
            (
                str(row.col1).strip(),
                str(row.col2).strip(),
                str(row.cpf).strip(),
            )
            for row in df.itertuples(index=False)
        ]

        cursor.executemany(sql, dados)
        conn.commit()

        total_importado += len(dados)

        print(
            f"Lote {numero_lote} | "
            f"Linhas: {len(dados)} | "
            f"Total: {total_importado:,} | "
            f"Tempo lote: {time.perf_counter() - inicio_lote:.2f}s"
        )

    cursor.close()
    conn.close()

    print(f"\nImportação concluída.")
    print(f"Total inserido: {total_importado:,}")
    print(f"Tempo total: {time.perf_counter() - inicio_total:.2f}s")


if __name__ == "__main__":
    importar_arquivo()
    