import os

def generate_text_report(df):
    """
    Generate a simple textual report with insights from the dataset
    """

    lines = []

    # Salary overview
    avg_salary = df["salary_in_usd"].mean()
    lines.append(f"Average salary across all roles: ${avg_salary:,.2f}")

    # Salary by experience level
    exp_avg = df.groupby("experience_level")["salary_in_usd"].mean()
    for level, sal in exp_avg.items():
        lines.append(f"Average salary for {level} level: ${sal:,.2f}")

    # Salary by company size
    size_avg = df.groupby("company_size")["salary_in_usd"].mean()
    for size, sal in size_avg.items():
        lines.append(f"Average salary for company size {size}: ${sal:,.2f}")

    # Remote work
    remote_avg = df.groupby("remote_ratio")["salary_in_usd"].mean()
    for ratio, sal in remote_avg.items():
        lines.append(f"Average salary for remote ratio {ratio}%: ${sal:,.2f}")

    # Top paying jobs
    top_jobs = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(5)
    lines.append("Top 5 highest paying jobs:")
    for job, sal in top_jobs.items():
        lines.append(f"- {job}: ${sal:,.2f}")

    # Save to file
    os.makedirs("outputs", exist_ok=True)
    report_path = "outputs/report.txt"
    with open(report_path, "w") as f:
        for line in lines:
            f.write(line + "\n")

    return report_path