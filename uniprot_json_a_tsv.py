"""
Programa: uniprot_json_a_tsv.py
Autor: Samuel Restrepo Buritica
Descripción:
    Este programa convierte un archivo de datos biológicos descargado de UniProt
    en formato JSON comprimido (.json.gz) a un archivo TSV (valores separados
    por tabulaciones).

    Columnas exportadas en el archivo TSV:
        - Accession: número de acceso de la proteína en UniProt
        - Gene_name: nombre principal del gen asociado
        - Organism: nombre científico del organismo de origen
        - Function: descripción de la función de la proteína (si está anotada)
        - Subcellular_location: ubicación subcelular (si está anotada)
        - Length: longitud de la secuencia proteica

Requisitos:
    - Python 3.x
    - Librerías estándar: gzip, json

Uso:
    python uniprot_json_a_tsv.py
"""

import gzip
import json

# ============================
# Archivos de entrada/salida
# ============================
archivo_entrada = "uniprotkb_tom40_2025_09_26.json.gz"   # Archivo JSON comprimido descargado de UniProt
archivo_salida = "proteinas.tsv"     # Archivo TSV que generará el programa

# ============================
# Leer JSON comprimido
# ============================
with gzip.open(archivo_entrada, "rt", encoding="utf-8") as f:
    data = json.load(f)

# Las entradas en tu JSON están bajo la clave "results"
entries = data.get("results", [])

# ============================
# Escribir archivo de salida TSV
# ============================
with open(archivo_salida, "w", encoding="utf-8") as out:
    # Titulos de las columnas
    out.write("Accession\tGene_name\tOrganism\tFunction\tSubcellular_location\tLength\n")

    # Iterar sobre cada proteína en el JSON
    for entry in entries:
        # Número de acceso
        accession = entry.get("primaryAccession", "NA")

        # Nombre del gen (el primero disponible)

        gene = "NA"
        if "genes" in entry and entry["genes"]:
            if "geneName" in entry["genes"][0]:
                gene = entry["genes"][0]["geneName"].get("value", "NA")

        # Organismo (nombre científico)
        organism = entry.get("organism", {}).get("scientificName", "NA")

        # Función (commentType == FUNCTION)
        function = "NA"
        if "comments" in entry:
            for c in entry["comments"]:
                if c.get("commentType") == "FUNCTION":
                    if "texts" in c and c["texts"]:
                        function = c["texts"][0].get("value", "NA")
                        break


        # Ubicación subcelular (commentType == SUBCELLULAR LOCATION)
        subcell = "NA"
        if "comments" in entry:
            for c in entry["comments"]:
                if c.get("commentType") == "SUBCELLULAR LOCATION":
                    if "subcellularLocations" in c and c["subcellularLocations"]:
                        subcell = c["subcellularLocations"][0]["location"].get("value", "NA")
                        break

        # Longitud de la proteína (número de aminoácidos)
        length = entry.get("sequence", {}).get("length", "NA")

        # ============================
        # Escribir fila en el TSV
        # ============================
        # Limpiar valores para evitar tabs o saltos de línea en el texto
        safe = lambda s: str(s).replace("\t", " ").replace("\n", " ")
        out.write(
            f"{safe(accession)}\t{safe(gene)}\t{safe(organism)}\t"
            f"{safe(function)}\t{safe(subcell)}\t{safe(length)}\n"
        )

print("Conversión finalizada:", archivo_salida)
