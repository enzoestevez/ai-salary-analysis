# AI Salary Analysis – Data Science & AI Project

This project demonstrates a **complete data analysis pipeline enhanced with Artificial Intelligence**.
It analyzes salary data from data science roles and automatically generates **insights, visualizations, and a professional PDF report**.

The goal is to simulate how a **Data Analyst or Data Scientist** could combine **Python, data analysis, visualization, and AI** to generate automated reports from datasets.

---

## Project Features

* Automated dataset analysis
* Salary insights using **AI (OpenAI API)**
* Professional **data visualizations**
* Automatic **PDF report generation**
* Modular Python architecture

---

## Project Structure

```
ai-salary-analysis/
│
├── data/                     # Dataset
│
├── outputs/                  # Generated charts and reports
│
├── src/
│   ├── data_loader.py        # Load dataset and overview
│   ├── visualizations.py     # Data visualizations
│   ├── ai_context_builder.py # Dataset context for AI
│   ├── ai_agent.py           # OpenAI API integration
│   ├── report_generator.py   # Generate text report
│   └── pdf_report.py         # Generate final PDF report
│
├── main.py                   # Main pipeline
│
└── README.md
```

---

## Dataset

The dataset contains salary information for **Data Science related roles**, including:

* Work year
* Experience level
* Employment type
* Job title
* Salary
* Salary in USD
* Remote work ratio
* Company size
* Company location

The dataset allows analysis such as:

* Salary by experience level
* Salary by company size
* Remote vs onsite salary trends
* Salary distribution

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* OpenAI API
* FPDF (PDF generation)

---

## Installation

Clone the repository:

```
git clone https://github.com/enzoestevez/ai-salary-analysis.git
cd ai-salary-analysis
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install pandas matplotlib openai fpdf2
```

---

## Running the Project

Execute the main pipeline:

```
python main.py
```

The program will automatically:

1. Load the dataset
2. Generate visualizations
3. Generate AI insights
4. Create a text report
5. Generate a **final PDF report**

All outputs are saved inside the **outputs/** folder.

---

## Generated Outputs

Charts:

* salary_by_experience.png
* salary_by_company_size.png
* remote_salary.png

Reports:

* report.txt
* final_report.pdf

---

## Example Analysis Questions

The AI component can generate insights such as:

* How experience level affects salaries
* Differences between company sizes
* Remote vs onsite salary trends
* High paying job roles

---

## Future Improvements

Possible improvements for this project:

* Interactive dashboards using **Plotly**
* Web interface with **Streamlit**
* Automatic dataset upload
* More advanced AI analysis
* Deployment as a web application

---

## Author

**Enzo Estévez**

Data Science Student – UNLu

Portfolio
https://enzoestevez.com

GitHub
https://github.com/enzoestevez

LinkedIn
https://www.linkedin.com/in/enzoestevez/

---

## License

This project is for **educational and portfolio purposes**.
