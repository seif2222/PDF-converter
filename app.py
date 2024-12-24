from flask import Flask, request, jsonify, render_template
import os
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert_pdf():
    try:
        # Get uploaded file and target path
        file = request.files['file']
        destination_path = request.form['path']
        output_format = request.form.get('format', 'txt')  # Default format is 'txt'

        # Ensure the destination directory exists
        os.makedirs(destination_path, exist_ok=True)

        # Save the uploaded PDF file temporarily
        temp_pdf_path = os.path.join(destination_path, file.filename)
        file.save(temp_pdf_path)

        # Extract the filename without extension
        base_filename = os.path.splitext(file.filename)[0]

        # Convert PDF to the desired format
        if output_format.lower() == 'txt':
            output_file = os.path.join(destination_path, f"{base_filename}.txt")
            pdf_to_txt(temp_pdf_path, output_file)
        elif output_format.lower() == 'doc':
            output_file = os.path.join(destination_path, f"{base_filename}.docx")
            pdf_to_doc(temp_pdf_path, output_file)
        else:
            return jsonify({"message": "Unsupported format. Please use 'txt' or 'doc'."}), 400

        # Remove the temporary PDF file
        os.remove(temp_pdf_path)

        return jsonify({"message": f"File successfully converted to {output_format} and saved at {output_file}"})
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

def pdf_to_txt(pdf_path, output_path):
    """Convert a PDF file to a text file."""
    reader = PdfReader(pdf_path)
    with open(output_path, 'w', encoding='utf-8') as txt_file:
        for page in reader.pages:
            txt_file.write(page.extract_text() + "\n")

def pdf_to_doc(pdf_path, output_path):
    """Convert a PDF file to a Word document."""
    reader = PdfReader(pdf_path)
    doc = Document()
    for page in reader.pages:
        doc.add_paragraph(page.extract_text())
    doc.save(output_path)

if __name__ == '__main__':
    app.run(debug=True)
