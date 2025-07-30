# Student Grade Analyzer with Python and Pandas

## 📖 Overview

This is a practical Python script designed to process a CSV file containing student grades. It automates the task of calculating final averages, determining each student's academic status ('Approved' or 'Reproved'), and exporting the processed data into a clean, structured JSON file.

This project serves as a foundational exercise in data manipulation and processing, utilizing the powerful Pandas library to handle data efficiently.

## ✨ Features

-   Reads student data from a `.csv` file.
-   Calculates the final average from multiple grade columns.
-   Determines the student's status based on a defined threshold (>= 7.0 for 'Approved').
-   Exports the results, including the calculated average and status, to a `.json` file.

## 🛠️ Technologies Used

-   **Python 3**
-   **Pandas:** For data manipulation and analysis.
-   **NumPy:** For efficient numerical operations (used by Pandas).

## ▶️ How to Run

1.  Ensure the input file `notas_alunos.csv` is present in the root directory of the project.
2.  Execute the main script from your terminal:
    ```bash
    python processador_notas.py
    ```
3.  After the script finishes, a new file named `notas_finais.json` will be created in the same directory, containing the processed data.

## 📂 Project Structure
