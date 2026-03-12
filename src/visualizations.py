import matplotlib.pyplot as plt
import os


def plot_salary_by_experience(df):

    data = df.groupby("experience_level")["salary_in_usd"].mean()

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    data.plot(kind="bar")

    plt.title("Average Salary by Experience Level")
    plt.xlabel("Experience Level")
    plt.ylabel("Average Salary (USD)")

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/salary_by_experience.png")
    plt.close()


def plot_salary_by_company_size(df):

    data = df.groupby("company_size")["salary_in_usd"].mean()

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    data.plot(kind="bar")

    plt.title("Average Salary by Company Size")
    plt.xlabel("Company Size")
    plt.ylabel("Average Salary (USD)")

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/salary_by_company_size.png")
    plt.close()


def plot_remote_salary(df):

    data = df.groupby("remote_ratio")["salary_in_usd"].mean()

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    data.plot(kind="bar")

    plt.title("Remote vs Onsite Salary")
    plt.xlabel("Remote Ratio")
    plt.ylabel("Average Salary (USD)")

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/remote_salary.png")
    plt.close()
    
def plot_top_jobs_salary(df):

    data = (
        df.groupby("job_title")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    data.plot(kind="bar")

    plt.title("Top 10 Highest Paying Data Jobs")
    plt.xlabel("Job Title")
    plt.ylabel("Average Salary (USD)")

    plt.xticks(rotation=45)

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/top_jobs_salary.png")
    plt.close()
    
def plot_salary_distribution(df):

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.hist(df["salary_in_usd"], bins=30)

    plt.title("Salary Distribution")
    plt.xlabel("Salary (USD)")
    plt.ylabel("Frequency")

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/salary_distribution.png")
    plt.close()

def plot_remote_distribution(df):

    data = df["remote_ratio"].value_counts()

    plt.figure(figsize=(10,6))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    data.plot(kind="bar")

    plt.title("Remote Work Distribution")
    plt.xlabel("Remote Ratio")
    plt.ylabel("Number of Jobs")

    os.makedirs("outputs", exist_ok=True)

    plt.savefig("outputs/remote_distribution.png")
    plt.close()