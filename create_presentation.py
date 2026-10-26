from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


BASE_DIR = Path(__file__).resolve().parent
CHART_DIR = BASE_DIR / "outputs" / "visualizations"
OUTPUT_FILE = BASE_DIR / "online_retail_presentation_final.pptx"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

NAVY = RGBColor(17, 31, 51)
PANEL = RGBColor(28, 47, 69)
TEAL = RGBColor(48, 191, 173)
GOLD = RGBColor(246, 190, 77)
WHITE = RGBColor(246, 248, 251)
MUTED = RGBColor(184, 197, 211)
RULE = RGBColor(71, 91, 110)


def add_text(
    slide,
    x,
    y,
    width,
    height,
    text,
    size=18,
    color=WHITE,
    bold=False,
    align=PP_ALIGN.LEFT,
    valign=MSO_ANCHOR.TOP,
    margin=0.05,
):
    shape = slide.shapes.add_textbox(
        Inches(x), Inches(y), Inches(width), Inches(height)
    )
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(margin)
    frame.margin_right = Inches(margin)
    frame.margin_top = Inches(margin)
    frame.margin_bottom = Inches(margin)
    frame.vertical_anchor = valign

    paragraph = frame.paragraphs[0]
    paragraph.alignment = align
    run = paragraph.add_run()
    run.text = text
    run.font.name = "Aptos"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    return shape


def add_rect(slide, x, y, width, height, color, rounded=False):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(
        shape_type, Inches(x), Inches(y), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    if rounded:
        shape.adjustments[0] = 0.12
    return shape


def set_background(slide, color=NAVY):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def add_header(slide, section, title, slide_number):
    add_text(slide, 0.58, 0.27, 6.0, 0.28, section.upper(), 10, TEAL, True)
    add_text(slide, 0.58, 0.62, 12.0, 0.58, title, 27, WHITE, True)
    add_rect(slide, 0.58, 1.29, 12.15, 0.025, PANEL)
    add_text(
        slide, 12.15, 7.08, 0.6, 0.2, f"{slide_number:02d} / 07",
        9, MUTED, align=PP_ALIGN.RIGHT,
    )


def add_notes(slide, duration, narration):
    notes = slide.notes_slide.notes_text_frame
    notes.text = f"Timing: {duration}\n\n{narration}"


def add_card(slide, x, y, width, height, label, heading, body, accent=TEAL):
    add_rect(slide, x, y, width, height, PANEL, rounded=True)
    add_rect(slide, x, y, 0.07, height, accent, rounded=True)
    add_text(slide, x + 0.24, y + 0.19, width - 0.45, 0.24, label.upper(),
             10, accent, True)
    add_text(slide, x + 0.24, y + 0.52, width - 0.45, 0.43, heading,
             18, WHITE, True)
    add_text(slide, x + 0.24, y + 1.02, width - 0.45, height - 1.12,
             body, 13, MUTED)


def add_chart(slide, filename, x, y, width, height):
    path = CHART_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Required chart image was not found: {path}")
    with Image.open(path) as image:
        image_width, image_height = image.size

    scale = min(width / image_width, height / image_height)
    picture_width = image_width * scale
    picture_height = image_height * scale
    picture_x = x + (width - picture_width) / 2
    picture_y = y + (height - picture_height) / 2
    return slide.shapes.add_picture(
        str(path),
        Inches(picture_x),
        Inches(picture_y),
        width=Inches(picture_width),
        height=Inches(picture_height),
    )


# Slide 1 — Project introduction
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_rect(slide, 0.72, 0.76, 0.10, 5.95, TEAL, rounded=True)
add_text(slide, 1.12, 1.05, 7.5, 0.35, "DATA ANALYSIS  •  ONLINE RETAIL",
         12, TEAL, True)
add_text(slide, 1.08, 1.75, 9.3, 1.45, "Online Retail\nAnalysis",
         38, WHITE, True)
add_text(
    slide, 1.12, 3.55, 10.4, 0.72,
    "What patterns can historical online retail transactions reveal about "
    "product demand and sales performance?",
    21, MUTED,
)
add_rect(slide, 1.12, 4.65, 5.7, 1.05, PANEL, rounded=True)
add_text(slide, 1.35, 4.82, 4.7, 0.30, "TOOLS", 10, TEAL, True)
add_text(slide, 1.35, 5.18, 5.1, 0.32,
         "Python  •  pandas  •  Matplotlib  •  Seaborn", 14, WHITE)
add_text(slide, 1.12, 6.32, 5.9, 0.28, "Presented by: [Your Name]", 13, MUTED)
add_text(slide, 12.15, 7.08, 0.6, 0.2, "01 / 07", 9, MUTED,
         align=PP_ALIGN.RIGHT)
add_notes(
    slide,
    "30 seconds",
    "Hello, my project is an exploratory analysis of historical transactions "
    "from a UK online retailer. I used Python and pandas for data cleaning and "
    "analysis, and Matplotlib and Seaborn for visualizations. The main business "
    "question is: what patterns can these transactions reveal about product "
    "demand and sales performance? I will cover the dataset and cleaning "
    "choices, sales and product trends, recommendations, and limitations. "
    "Replace the name placeholder on this slide before presenting.",
)

# Slide 2 — Dataset, cleaning, and distribution checks
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_header(slide, "01  |  Dataset & method", "Dataset and cleaning decisions", 2)

add_rect(slide, 0.58, 1.55, 5.65, 4.98, PANEL, rounded=True)
add_text(slide, 0.90, 1.82, 4.95, 0.28, "DATASET SNAPSHOT", 11, TEAL, True)
add_text(slide, 0.90, 2.20, 2.3, 0.42, "541,909", 24, WHITE, True)
add_text(slide, 0.90, 2.63, 2.35, 0.34, "original rows", 11, MUTED)
add_text(slide, 3.35, 2.20, 2.35, 0.42, "8 columns", 22, WHITE, True)
add_text(slide, 3.35, 2.63, 2.35, 0.34, "transaction fields", 11, MUTED)
add_text(slide, 0.90, 3.07, 2.3, 0.42, "5,268", 22, GOLD, True)
add_text(slide, 0.90, 3.48, 2.35, 0.34, "duplicates removed", 11, MUTED)
add_text(slide, 3.35, 3.07, 2.35, 0.42, "536,639", 22, GOLD, True)
add_text(slide, 3.35, 3.48, 2.35, 0.34, "rows after cleaning", 11, MUTED)
add_rect(slide, 0.90, 3.92, 4.98, 0.025, RULE)
add_text(slide, 0.90, 4.12, 4.95, 0.30, "CLEANING DECISIONS", 10, TEAL, True)
add_text(
    slide, 0.92, 4.50, 4.92, 1.78,
    "• Filled 1,454 missing descriptions with “Unknown”; kept missing IDs.\n"
    "• Converted InvoiceDate to datetime and removed duplicate rows.\n"
    "• Retained negative quantities; removed 2 negative-price rows.\n"
    "• Kept zero-price transactions for investigation.",
    12, WHITE,
)
add_rect(slide, 6.47, 1.55, 6.28, 2.43, WHITE, rounded=True)
add_text(slide, 6.72, 1.63, 5.8, 0.25,
         "QUANTITY & UNIT PRICE DISTRIBUTIONS", 10, NAVY, True)
add_chart(slide, "quantity_unitprice_distribution.png", 6.62, 1.88, 5.98, 2.00)
add_rect(slide, 6.47, 4.13, 6.28, 2.40, WHITE, rounded=True)
add_text(slide, 6.72, 4.20, 5.8, 0.25, "CORRELATION HEATMAP", 10, NAVY, True)
add_chart(slide, "correlation_heatmap.png", 7.76, 4.47, 3.70, 1.98)
add_notes(
    slide,
    "45 seconds",
    "The original dataset contained 541,909 rows and eight columns, spanning "
    "December 2010 to December 2011. I removed 5,268 duplicate rows, leaving "
    "536,639. I filled 1,454 missing descriptions with “Unknown” and retained "
    "missing customer IDs because those records still support analyses that "
    "do not require customer identification. I converted invoice dates to "
    "datetime. Negative quantities were retained because they may represent "
    "returns or credit notes. I removed two rows with negative unit prices and "
    "kept zero-price rows for investigation. The distribution chart shows "
    "skewed price values, and the heatmap shows linear relationships that "
    "should be interpreted with outliers and negative transactions in mind.",
)

# Slide 3 — Revenue and order trends
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_header(slide, "02  |  Sales trends", "Monthly revenue and order activity", 3)
add_rect(slide, 0.58, 1.55, 8.2, 4.98, WHITE, rounded=True)
add_chart(slide, "monthly_revenue_trend.png", 0.72, 1.72, 7.92, 4.62)
add_rect(slide, 9.02, 1.55, 3.73, 4.98, PANEL, rounded=True)
add_text(slide, 9.35, 1.86, 3.05, 0.28, "KEY PATTERN", 10, TEAL, True)
add_text(slide, 9.32, 2.24, 3.05, 0.77,
         "Strong rise into\nNovember 2011", 21, WHITE, True)
add_text(slide, 9.35, 3.23, 3.0, 0.72, "£1.46M", 28, GOLD, True)
add_text(slide, 9.35, 3.72, 3.0, 0.44,
         "highest monthly net recorded revenue", 12, MUTED)
add_rect(slide, 9.35, 4.20, 3.05, 0.025, RULE)
add_text(slide, 9.35, 4.38, 3.0, 0.37,
         "December is incomplete", 15, WHITE, True)
add_text(
    slide, 9.35, 4.77, 3.02, 0.34,
    "Data ends Dec 9. Monthly sums include negative transactions, which "
    "reduce net recorded revenue.",
    10, MUTED,
)
add_text(slide, 9.35, 5.16, 3.0, 0.22, "MONTHLY UNIQUE INVOICES", 9, TEAL, True)
add_chart(slide, "monthly_order_volume.png", 9.18, 5.38, 3.40, 1.12)
add_text(
    slide, 0.68, 6.70, 11.9, 0.24,
    "November peaked at £1.46M net revenue and 3,462 invoices; December's "
    "1,015 invoices cover only Dec 1–9.",
    12, TEAL, True,
)
add_notes(
    slide,
    "60 seconds",
    "This chart sums Quantity multiplied by UnitPrice for every invoice line, "
    "so it shows net recorded revenue rather than positive sales alone. "
    "Negative-quantity transactions reduce the total and may represent returns "
    "or credit notes; their exact reason should not be assumed without "
    "checking. Revenue increased toward autumn and reached its highest level "
    "in November 2011, at about £1.46 million. November also had the highest "
    "invoice volume, at 3,462. December's totals are lower, but the dataset "
    "ends on December 9, and records only 1,015 invoices for that partial "
    "month. For fair comparisons, compare equivalent date ranges or exclude "
    "incomplete December from full-month comparisons.",
)

# Slide 4 — Product demand and order-volume visualizations
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_header(slide, "03  |  Product insights", "Product demand and order volume", 4)
add_rect(slide, 0.58, 1.55, 8.2, 4.98, WHITE, rounded=True)
add_chart(slide, "top_10_products.png", 0.78, 1.72, 7.82, 4.62)
add_rect(slide, 9.02, 1.55, 3.73, 4.98, PANEL, rounded=True)
add_text(slide, 9.35, 1.86, 3.05, 0.28, "TOP PRODUCT BY NET QUANTITY", 10, TEAL, True)
add_text(slide, 9.32, 2.26, 3.0, 1.03,
         "WORLD WAR 2\nGLIDERS ASSTD\nDESIGNS", 18, WHITE, True)
add_text(slide, 9.35, 3.52, 3.0, 0.55, "53,751", 28, GOLD, True)
add_text(slide, 9.35, 4.06, 3.0, 0.34, "net units recorded", 12, MUTED)
add_rect(slide, 9.35, 4.55, 3.05, 0.025, RULE)
add_text(
    slide, 9.35, 4.80, 3.0, 1.25,
    "Novelty, gift, and household products feature prominently. The ranking "
    "measures net units—not revenue or order count.",
    12, MUTED,
)
add_text(
    slide, 0.68, 6.70, 11.9, 0.24,
    "Monthly unique invoices increased to 3,462 in November; compare product "
    "net quantities with returns in mind.",
    12, TEAL, True,
)
add_notes(
    slide,
    "60 seconds",
    "The bar chart ranks the ten products with the highest net quantity. "
    "WORLD WAR 2 GLIDERS ASSTD DESIGNS leads with 53,751 net units. The top "
    "products also include novelty, gift, and household items. This can guide "
    "further product-level demand review and inventory planning. It measures "
    "net units rather than revenue, profit, or order count, and negative "
    "quantities reduce the ranking totals. The monthly order-volume analysis "
    "also shows that unique invoices rose to 3,462 in November, the high point "
    "in the period. Both metrics are historical and should be validated "
    "against additional years before using them as seasonal forecasts.",
)

# Slide 5 — Recommendations
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_header(slide, "04  |  Actions", "Three recommendations", 5)
add_card(
    slide, 0.68, 1.82, 3.86, 3.75, "01  •  Plan inventory",
    "Use the November peak",
    "Review November's revenue and invoice-volume peak alongside product "
    "demand. Validate with more years before assuming the pattern repeats "
    "seasonally.",
    TEAL,
)
add_card(
    slide, 4.74, 1.82, 3.86, 3.75, "02  •  Compare fairly",
    "Adjust for partial December",
    "December covers only the first nine days. Compare like-for-like dates or "
    "omit it from full-month comparisons.",
    GOLD,
)
add_card(
    slide, 8.80, 1.82, 3.86, 3.75, "03  •  Investigate",
    "Understand adjustments",
    "Review negative-quantity and zero-price records. Where possible, report "
    "positive sales, negative transactions, and net recorded revenue "
    "separately.",
    TEAL,
)
add_text(
    slide, 0.72, 6.20, 11.85, 0.38,
    "Use historical patterns as evidence for questions to investigate—not "
    "guarantees of future demand.",
    14, MUTED, True,
)
add_notes(
    slide,
    "60 seconds",
    "I recommend three next steps. First, use November's high revenue and "
    "invoice volume, alongside the top-products chart, to guide inventory "
    "questions—but validate this against additional years because the dataset "
    "covers only a little over one year. Second, make December comparisons "
    "fair by comparing the first nine days with equivalent periods, or "
    "excluding December from complete-month comparisons. Third, investigate "
    "negative-quantity and zero-priced transactions to understand whether "
    "they reflect returns, cancellations, credit notes, samples, or "
    "adjustments. Where possible, report positive recorded sales, negative "
    "transactions, and net recorded revenue separately.",
)

# Slide 6 — Limitations and conclusion
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_header(slide, "05  |  Wrap-up", "Limitations and conclusion", 6)
add_rect(slide, 0.58, 1.62, 7.15, 4.90, PANEL, rounded=True)
add_text(slide, 0.92, 1.94, 6.4, 0.34, "LIMITATIONS", 11, TEAL, True)

limitations = [
    ("Historical window", "Just over one year; not enough to establish recurring seasonality."),
    ("Partial final month", "Data ends Dec 9, 2011; December is not a full month."),
    ("Transaction context", "Negative transactions and zero prices need investigation."),
    ("No causality", "The analysis identifies patterns, not why sales changed."),
]
for index, (heading, body) in enumerate(limitations):
    y = 2.50 + index * 0.86
    add_rect(slide, 0.96, y + 0.06, 0.11, 0.11,
             GOLD if index == 1 else TEAL, rounded=True)
    add_text(slide, 1.22, y, 1.78, 0.27, heading, 13, WHITE, True)
    add_text(slide, 3.05, y, 4.20, 0.50, body, 12, MUTED)

add_rect(slide, 8.02, 1.62, 4.73, 4.90, TEAL, rounded=True)
add_text(slide, 8.40, 1.98, 3.95, 0.32, "TAKEAWAY", 11, NAVY, True)
add_text(
    slide, 8.38, 2.48, 3.98, 1.42,
    "Demand rose toward November, and leading products offer a starting "
    "point for inventory review.",
    20, NAVY, True,
)
add_rect(slide, 8.40, 4.24, 3.94, 0.025, RGBColor(32, 140, 132))
add_text(
    slide, 8.40, 4.56, 3.92, 1.22,
    "Treat results as historical evidence, account for net transactions, "
    "and investigate before acting.",
    14, NAVY,
)
add_notes(
    slide,
    "45 seconds",
    "To conclude, this analysis describes historical activity from December "
    "2010 through December 9, 2011. It shows a rise in net recorded revenue "
    "toward a November peak and identifies leading products by net quantity. "
    "The period is short, December is incomplete, negative transactions and "
    "zero prices need context, and the analysis cannot establish causes of "
    "sales changes. These findings can identify areas for further "
    "investigation, but they should not be treated as a forecast or proof of "
    "a recurring seasonal pattern. Transition to the final slide for questions.",
)

# Slide 7 — Closing
slide = prs.slides.add_slide(BLANK)
set_background(slide)
add_rect(slide, 0.72, 0.76, 0.10, 5.95, TEAL, rounded=True)
add_text(slide, 1.16, 1.50, 6.0, 0.34, "ONLINE RETAIL ANALYSIS", 12, TEAL, True)
add_text(slide, 1.12, 2.40, 8.8, 1.05, "Thank you", 44, WHITE, True)
add_rect(slide, 1.16, 3.72, 2.10, 0.045, GOLD)
add_text(slide, 1.12, 4.18, 8.8, 0.85, "Any questions?", 30, MUTED, True)
add_text(slide, 12.15, 7.08, 0.6, 0.2, "07 / 07", 9, MUTED,
         align=PP_ALIGN.RIGHT)
add_notes(slide, "Closing", "Thank the audience and invite questions.")

prs.save(OUTPUT_FILE)
print(f"Presentation created: {OUTPUT_FILE}")
print(f"Slides created: {len(prs.slides)}")
