# src/pdf_report.py
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AI-Augmented Data Analysis Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def create_pdf_report(report_txt_path, images_paths, output_path="outputs/final_report.pdf"):
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Primera página: texto del reporte
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    with open(report_txt_path, "r", encoding="utf-8") as f:
        for line in f:
            pdf.multi_cell(0, 8, line)

    # Agregar gráficos
    for img_path in images_paths:
        if os.path.exists(img_path):
            pdf.add_page()
            pdf.image(img_path, x=15, y=25, w=180)
    
    # Guardar PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path