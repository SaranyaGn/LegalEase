import os
import io
from docx import Document
from docx.shared import Inches
from fpdf import FPDF

# Custom PDF class handling header/footer layout
class LegalPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def format_docx(text: str, doc_type: str = "Legal Document", logo_path: str = None) -> bytes:
    """Generates a styled .docx file from plain text."""
    doc = Document()

    # Optional Logo Header for Word Document
    if logo_path and os.path.exists(logo_path):
        try:
            doc.add_picture(logo_path, width=Inches(1.5))
        except Exception:
            pass

    doc.add_heading(doc_type.upper(), level=1)
    
    for paragraph in text.split("\n"):
        if paragraph.strip():
            doc.add_paragraph(paragraph.strip())
            
    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    return file_stream.getvalue()


def format_pdf(text: str, doc_type: str = "Legal Document", logo_path: str = None) -> bytes:
    """Generates a clean PDF document with safe margins and multi-cell wrapping."""
    pdf = LegalPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set explicit margins (15mm)
    pdf.set_margins(15, 15, 15)

    # Optional Logo Header
    if logo_path and os.path.exists(logo_path):
        try:
            pdf.image(logo_path, x=15, y=10, w=30)
            pdf.ln(20)
        except Exception:
            pass

    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, doc_type.upper(), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)

    # Calculate usable width dynamically (Page Width minus Margins)
    effective_width = pdf.w - pdf.l_margin - pdf.r_margin

    # Body Text
    pdf.set_font("Helvetica", size=10)
    
    for line in text.split("\n"):
        pdf.set_x(pdf.l_margin)
        line_str = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(w=effective_width, h=6, text=line_str, new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())


def format_html_preview(text: str) -> str:
    """Formats document text for HTML preview display."""
    formatted_body = "<br>".join(text.split("\n"))
    return f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; line-height: 1.6; color: #333;">
        {formatted_body}
    </div>
    """