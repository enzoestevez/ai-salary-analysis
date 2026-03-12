from src.ai_agent import ask_ai_about_dataset
import os

def generate_text_report(df, ai_context=None, user_question="generate full report"):
    """
    Genera un reporte de texto con análisis descriptivo y con IA.
    """
    lines = []

    # Insights clásicos
    avg_salary = df["salary_in_usd"].mean()
    lines.append(f"Average salary across all roles: ${avg_salary:,.2f}")

    # Más análisis
    exp_avg = df.groupby("experience_level")["salary_in_usd"].mean()
    for level, sal in exp_avg.items():
        lines.append(f"Average salary for {level} level: ${sal:,.2f}")

    # Usamos IA para generar insights más analíticos
    if ai_context:
        ai_insights = ask_ai_about_dataset(ai_context, user_question)
        lines.append("\nAI Insights:")
        lines.append(ai_insights)

    # Guardar reporte
    os.makedirs("outputs", exist_ok=True)
    report_path = "outputs/report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    return report_path