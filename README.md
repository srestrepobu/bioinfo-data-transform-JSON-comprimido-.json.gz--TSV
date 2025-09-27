# bioinfo-data-transform-JSON-comprimido-.json.gz--TSV
Este programa convierte un archivo de datos biológicos descargado de UniProt en formato JSON comprimido (.json.gz) a un archivo TSV.
Scripts en Python para transformar datos biológicos de **UniProt** en formato JSON a archivos TSV más fáciles de analizar.

## Archivos incluidos
- `uniprot_json_a_tsv.py` → Convierte UniProt JSON.gz en TSV con columnas Accession, Gene, Organism, Function, Subcellular location y Length.
- `uniprotkb_tom40_2025_09_26.json.gz` → Base de datos para hacer la prueba 

## Tutorial de uso

Este script convierte archivos de **UniProt** en formato **JSON comprimido (`.json.gz`)** a un archivo **TSV** más fácil de analizar.

### Requisitos

* Python 3.x
* Librerías estándar: `gzip`, `json`

### Pasos de uso

1. Descarga un archivo de UniProt en formato **JSON.gz**.
2. Edita el script y cambia esta línea con el nombre de tu archivo:

   ```python
   archivo_entrada = "uniprotkb_tom40_2025_09_26.json.gz"
   ```
3. Ejecuta el script en la terminal:

   ```bash
   python uniprot_json_a_tsv.py
   ```
4. Se generará un archivo `proteinas.tsv` con las columnas:

   * Accession
   * Gene_name
   * Organism
   * Function
   * Subcellular_location
   * Length

### Ejemplo de salida

```tsv
Accession   Gene_name   Organism            Function                                   Subcellular_location   Length
Q75Q40      Tomm40      Rattus norvegicus   Channel-forming protein essential...       Mitochondrion          361
```

