from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()

# Helper function to create title slides
def add_title_slide(prs, title_text, subtitle_text):
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = title_text
    subtitle.text = subtitle_text

# Helper function to create content slides
def add_content_slide(prs, title_text, bullets):
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    shapes = slide.shapes
    shapes.title.text = title_text
    
    tf = shapes.placeholders[1].text_frame
    tf.word_wrap = True
    
    for i, bullet in enumerate(bullets):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = bullet
        p.font.size = Pt(18)

# Slide 1: Title
add_title_slide(
    prs, 
    "LegalEase – AI-Powered Legal Document Generator", 
    "Automated Legal Drafting, Inline Editing, and Multi-Format Export\nFinal Project Documentation Presentation"
)

# Slide 2: Overview & Tech Stack
add_content_slide(
    prs, 
    "Project Overview & Tech Stack", 
    [
        "Project Mission: Streamline contract creation and legal document generation using Generative AI.",
        "Frontend: Streamlit (Dynamic UI, Live Preview, Multi-format file downloads).",
        "Backend: FastAPI (Asynchronous REST API, Request handling, Gemini Integration).",
        "LLM Engine: Google Gemini API (gemini-1.5-pro).",
        "Document Formatting: Python-docx (Word) & ReportLab (PDF)."
    ]
)

# Slide 3: System Architecture
add_content_slide(
    prs, 
    "System Architecture & Workflow", 
    [
        "1. User Input: Collects contract details via Streamlit UI (Document Type, Parties, Terms, Date).",
        "2. FastAPI Request: Transmits structured JSON payloads to backend endpoints.",
        "3. Gemini Processing: Prompts gemini-1.5-pro to construct legally structured agreements.",
        "4. Dynamic Preview: Renders formatted preview with inline editing capabilities.",
        "5. Multi-Format Export: Generates .txt, .docx, and .pdf documents with formatted layouts."
    ]
)

# Slide 4: Input Interface
add_content_slide(
    prs, 
    "UI Walkthrough: Input Interface", 
    [
        "Clean, dark-themed Streamlit user interface.",
        "Form Fields Supported:",
        "  • Document Type (e.g., Freelance Service Contract)",
        "  • Parties Involved (e.g., Jane Doe vs. TechNova Inc.)",
        "  • Terms & Conditions (Payment terms, NDA, IP clauses)",
        "  • Effective Date (e.g., October 1, 2026)",
        "[INSERT SCREENSHOT: Streamlit Input Form]"
    ]
)

# Slide 5: Preview & Inline Editing
add_content_slide(
    prs, 
    "UI Walkthrough: Preview & Editing", 
    [
        "Real-time Generation: Displays AI-generated legal text instantly.",
        "Click to Edit Feature: Built-in inline editor allowing real-time modifications before export.",
        "Live HTML/Markdown Preview: Updates formatting on the fly based on user edits.",
        "[INSERT SCREENSHOT: Inline Editor & Dynamic Preview]"
    ]
)

# Slide 6: Multi-Format Export
add_content_slide(
    prs, 
    "UI Walkthrough: Export Capabilities", 
    [
        "Plain Text (.txt): Unformatted raw text export for quick sharing.",
        "Word Document (.docx): Styled headers, company logos, bold section titles, and dynamic tables.",
        "PDF Document (.pdf): Clean, print-ready layout created via ReportLab.",
        "[INSERT SCREENSHOT: File Download Buttons & Sample Export Files]"
    ]
)

# Slide 7: E2E Verification
add_content_slide(
    prs, 
    "Verification & Testing Summary", 
    [
        "✓ API Connectivity: Backend successfully processed requests and received responses from Gemini.",
        "✓ State Management: Streamlit session state persisted inline edits accurately.",
        "✓ Export Integrity: Logos, tables, headers, and signatures rendered cleanly across .docx and .pdf.",
        "✓ Error Handling: Authentication and missing input errors handled gracefully."
    ]
)

# Slide 8: Conclusion
add_content_slide(
    prs, 
    "Conclusion & Future Roadmap", 
    [
        "Project Conclusion: LegalEase successfully bridges complex legal drafting and AI-driven automation.",
        "Future Enhancements:",
        "  • Contract Redlining & Analysis: AI-assisted risk and clause detection.",
        "  • Legal Database Integration: Linking with regional legal repositories.",
        "  • Multi-Language Support: Automated translation for international contracts."
    ]
)

# Save the PowerPoint Presentation
output_filename = "LegalEase_Documentation.pptx"
prs.save(output_filename)
print(f"✅ Success! PowerPoint presentation saved as '{output_filename}' in D:\\LegalEase\\")