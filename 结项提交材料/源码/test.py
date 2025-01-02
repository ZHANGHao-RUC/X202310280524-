from docx import Document
import re

# Load the document
doc_path = r"C:\Users\欧拉-Q\OneDrive\桌面\中国档案学会2024征文\专题（二）_张昊、阿亚古孜·叶尔切特_实然与应然：初探档案多维著录的转向逻辑.docx"
doc = Document(doc_path)

# Define the mapping
mapping = {
    "1": "1",
    "2": "2",
    "15": "3",
    "16": "4",
    "17": "5",
    "18": "6",
    "19": "7",
    "20": "8",
    "21": "9",
    "22": "10",
    "23": "11",
    "24": "12",
    "27": "13",
    "28": "14",
    "29": "15",
    "34": "16",
    "35": "17",
    "38": "18",
    "39": "19",
    "40": "20",
    "41": "21",
    "42": "22",
    "43": "23",
    "44": "24",
}

# Function to replace the references in text
def replace_references(text):
    for old, new in mapping.items():
        text = re.sub(r'\[{}\]'.format(old), f'[{new}]', text)
    return text

# Replace all references in the document while preserving the format
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        run.text = replace_references(run.text)

# Save the modified document
modified_doc_path = r"C:\Users\欧拉-Q\OneDrive\桌面\中国档案学会2024征文\专题（二）_张昊、阿亚古孜·叶尔切特_实然与应然：初探档案多维著录的转向逻辑_1.docx"
doc.save(modified_doc_path)