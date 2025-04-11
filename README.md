# SoWell - Your Friendly Anonymous Therapist

Welcome to **SoWell**, a web-based application that serves as your personal, anonymous virtual therapist. This project integrates real-time face and emotion detection using a webcam with a conversational AI powered by Google Generative AI. The interface features a dynamic cityscape animation built with HTML, CSS, and Flask.

## Screenshots
![App Preview](static/css/screenshot.png)


---

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Description

SoWell uses computer vision libraries (OpenCV and MTCNN) and deep learning (DeepFace) to detect and analyze facial expressions in real-time. The detected emotion influences the AI therapist's tone, built using LangChain with Google's Gemini model. The user interface, styled with Bootstrap and custom CSS, includes a cityscape background with animated elements and a chat interface.

---

## Features

- 🎭 **Real-Time Emotion Detection**: Analyzes facial expressions via webcam and classifies emotions (happy, sad, angry, fear, disgust, neutral, surprise).
- 💬 **Emotion-Adaptive AI**: Adjusts the therapist's tone based on detected emotions for a personalized experience.
- 🌆 **Dynamic Cityscape**: Animated background with trees, towers, clouds, and street elements.
- 📱 **Responsive Design**: Full-width layout adaptable to different screen sizes.
- 💻 **Chat Interface**: Interactive chat with the AI therapist using Flask and jQuery.
- 🕶️ **Anonymous Support**: Provides a safe, anonymous environment for users.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/sowell-therapist.git
