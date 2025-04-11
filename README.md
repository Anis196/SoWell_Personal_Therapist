# SoWell - Your Friendly Anonymous Therapist

Welcome to **SoWell**, a web-based application that serves as your personal, anonymous virtual therapist. This project integrates real-time face and emotion detection using a webcam with a conversational AI powered by Google Generative AI. The interface features a dynamic cityscape animation built with HTML, CSS, and Flask.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description
SoWell uses computer vision libraries (OpenCV and MTCNN) and deep learning (DeepFace) to detect and analyze facial expressions in real-time. The detected emotion influences the AI therapist's tone, built using LangChain with Google's Gemini model. The user interface, styled with Bootstrap and custom CSS, includes a cityscape background with animated elements and a chat interface.

## Features
- **Real-Time Emotion Detection**: Analyzes facial expressions via webcam and classifies emotions (happy, sad, angry, fear, disgust, neutral, surprise).
- **Emotion-Adaptive AI**: Adjusts the therapist's tone based on detected emotions for a personalized experience.
- **Dynamic Cityscape**: Animated background with trees, towers, clouds, and street elements.
- **Responsive Design**: Full-width layout adaptable to different screen sizes.
- **Chat Interface**: Interactive chat with the AI therapist using Flask and jQuery.
- **Anonymous Support**: Provides a safe, anonymous environment for users.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sowell-therapist.git

(Replace your-username and sowell-therapist with your GitHub username and repository name.)

Navigate to the project directory:
bash

Collapse

Wrap

Copy
cd sowell-therapist
Install dependencies:
bash

Collapse

Wrap

Copy
pip install -r requirements.txt
Set up your Google API key:
Create a .env file in the project root.
Add your key: GOOGLE_API_KEY=your_api_key_here.
Add .env to .gitignore to keep it secure.
Run the application:
bash

Collapse

Wrap

Copy
python together.py
Open http://127.0.0.1:5000/ in your browser.
Usage
Allow webcam access for real-time emotion detection.
Use the chat interface (left side) to interact with SoWell. Type a message and click "Send".
The right side shows the live video feed with emotion labels and a greeting.
Customize static/css/style.css or together.html for design changes.
Extend with JavaScript or modify together.py for new features.
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a branch: git checkout -b feature-branch.
Commit changes: git commit -m "Add new feature".
Push to the branch: git push origin feature-branch.
Open a pull request with a clear description.
Please adhere to the existing code style and add comments where needed.

License
This project is licensed under the . See the  file for details.

Contact
For questions or issues, open an issue or contact the maintainer:

Email: your-email@example.com (replace with your email)
GitHub: your-username
Author: Anis Shaikh
Last updated: April 11, 2025

text

Collapse

Wrap

Copy

### Instructions
1. **Copy the Text**: Copy the entire block above.
2. **Paste into README.md**: Create or open the `README.md` file in your GitHub repository's root directory and paste the content.
3. **Customize**:
   - Replace `your-username` and `sowell-therapist` with your actual GitHub username and repository name.
   - Update the email and GitHub link with your contact information (e.g., `[your-email@example.com](mailto:your-email@example.com)`).
   - If you have a `LICENSE` file, ensure it exists; otherwise, remove the license link or create one.
4. **Commit and Push**:
   - Stage the file: `git add README.md`
   - Commit: `git commit -m "Add updated README for SoWell project"`
   - Push: `git push origin main` (or your branch name)

### Notes
- **Markdown Features**: This version uses GitHub-flavored Markdown with proper headings (`#`, `##`), code blocks (```), links, and emphasis (**bold**, *italic*).
- **Missing `style.css`**: The `static/css/style.css` file is referenced but not provided. If you share it, I can include specific styling details or suggest enhancements.
- **Security Reminder**: Ensure `.env` is in `.gitignore` to protect your Google API key.
- **Enhancements**: You can add a "Screenshots" section with images or a "Demo" link later by editing the README.
- Let me know if you want to adjust any section or add more details (e.g., troubleshooting, deployment)!
