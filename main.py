# main.py
import pandas as pd
from src.data_loader import load_dataset, get_dataset_overview
from src.visualizations import (
    plot_salary_by_experience,
    plot_salary_by_company_size,
    plot_remote_salary
)
from src.ai_context_builder import build_dataset_context
from src.report_generator import generate_text_report
from src.pdf_report import create_pdf_report
import os

def main():
    # -------------------------
    # 1️⃣ Cargar dataset
    # -------------------------
    df = load_dataset("data/remote_salaries.csv")

    # Overview básico
    overview = get_dataset_overview(df)
    print("Dataset Overview:")
    print(f"rows: {overview['rows']}")
    print(f"columns: {overview['columns']}")
    print(f"column_names: {overview['column_names']}")
    print(f"missing_values: {overview['missing_values']}\n")

    # -------------------------
    # 2️⃣ Generar gráficos
    # -------------------------
    plot_salary_by_experience(df.groupby("experience_level")["salary_in_usd"].mean())
    plot_salary_by_company_size(df.groupby("company_size")["salary_in_usd"].mean())
    plot_remote_salary(df.groupby("remote_ratio")["salary_in_usd"].mean())
    print("Visualizations saved in outputs/")

    # -------------------------
    # 3️⃣ Preparar contexto para IA
    # -------------------------
    context = build_dataset_context(df)

    # -------------------------
    # 4️⃣ Generar reporte analítico con IA
    # -------------------------
    report_file = generate_text_report(df, ai_context=context, user_question="generate full report")
    print(f"Text report generated: {report_file}")

    # -------------------------
    # 5️⃣ Generar PDF profesional con gráficos + reporte
    # -------------------------
    images = [
        "outputs/salary_by_experience.png",
        "outputs/salary_by_company_size.png",
        "outputs/remote_salary.png"
    ]
    pdf_file = create_pdf_report(report_file, images)
    print(f"PDF report generated: {pdf_file}")

if __name__ == "__main__":
    main()