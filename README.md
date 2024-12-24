# PDF Converter Project

## Overview
The PDF Converter project is a web-based application that allows users to upload PDF files and convert them into different formats, such as TXT or DOC. The project is designed with a modern dark-themed UI and provides a user-friendly experience. The application was built using Flask (Python) for backend functionality and HTML, CSS, and JavaScript for the frontend.

## Features
- **File Upload and Conversion**:
  - Supports PDF file uploads.
  - Converts PDF files to TXT or DOC format.
  - Allows users to specify the destination path for the converted file.

- **Modern UI**:
  - Dark-themed interface with a sleek and responsive design.
  - Smooth animations for better user interaction.
  - Clear status messages and a loading spinner for feedback.

- **Cross-Platform Compatibility**:
  - Accessible on desktops, tablets, and mobile devices.

- **Branding**:
  - Footer includes credit: "Designed by Saif Abozaid."

## Technology Stack
- **Frontend**:
  - HTML5
  - CSS3 (with custom styles and animations)
  - JavaScript (for client-side interactivity)

- **Backend**:
  - Python (Flask framework)

- **Libraries**:
  - Flask for routing and API handling.

## Installation and Setup

### Requirements
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-converter.git
   cd pdf-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Folder Structure
```
project/
├── app.py                # Flask backend logic
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   ├── styles.css        # CSS styles
│   └── script.js         # JavaScript for interactivity
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Usage
1. Open the web application in your browser.
2. Upload a PDF file using the file input.
3. Specify the destination path for the converted file.
4. Select the desired output format (TXT or DOC).
5. Click the **Convert** button to process the file.
6. View the status message for confirmation or error details.

## Customization
- **Colors and Styles**: Modify the `static/styles.css` file to adjust the theme.
- **Animations**: Add or change animations in the CSS file.
- **Backend Logic**: Enhance `app.py` to include additional features or file formats.

## Future Enhancements
- Add support for more file formats (e.g., XLS, PPT).
- Integrate cloud storage options for file upload and download.
- Provide a preview of the converted files.

## Credits
Designed and developed by **Saif Abozaid**.

