from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 45)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.set_font_size(30)
    pdf.set_text_color(250, 250, 250)
    pdf.text(x=30, y=130, txt=f"{name} took CS50")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
