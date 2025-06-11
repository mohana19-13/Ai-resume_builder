# Ai-resume_builder
# AI-Powered Resume Builder

![Project Status](https://img.shields.io/badge/status-in%20development-orange) ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python Version](https://img.shields.io/badge/python-3.9%2B-blue) ![Framework](https://img.shields.io/badge/backend-Flask-green)
![AI Model](https://img.shields.io/badge/ai_model-[Your_LLM_Here]-purple) ## Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the Application](#running-the-application)
* [API Endpoints](#api-endpoints)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgments](#acknowledgments)

## About The Project

The AI-Powered Resume Builder is an innovative web application designed to simplify and enhance the resume creation process. Leveraging the power of Large Language Models (LLMs), it assists users in generating compelling and professional resume content, optimizing it for impact, and exporting it directly to a PDF format. This project aims to empower job seekers by providing an intelligent tool that goes beyond traditional template-based builders, offering real-time AI suggestions and content refinement.

**Key Goals:**
* To streamline resume creation by automating content generation.
* To help users craft impactful and keyword-rich descriptions.
* To provide a user-friendly interface for managing multiple resume versions.
* To offer secure user authentication and data storage.

## Features

* **User Authentication:** Secure user registration, login, and session management.
* **Resume Management:** Create, retrieve, update, and delete multiple resume profiles.
* **AI-Assisted Content Generation:**
    * Generate professional resume summaries/objectives.
    * Expand and refine experience bullet points with action verbs and quantifiable results.
    * Suggest relevant skills based on roles and industries.
    * (Optional: Add specific features like keyword optimization for job descriptions if implemented)
* **PDF Export:** Download your generated resume as a professionally formatted PDF.
* **Structured Data Input:** Organize resume information (personal details, experience, education, skills, projects) in a clear, structured format.
* **[Add any other planned or implemented features, e.g., drag-and-drop sections, multiple templates, rich text editing]**

## Technologies Used

* **Backend:**
    * [Python 3.9+](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/) (Web Framework)
    * [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) (ORM for database interaction)
    * [Flask-Login](https://flask-login.readthedocs.io/) (User session management)
    * [WeasyPrint](https://weasyprint.org/) (HTML to PDF converter)
    * `werkzeug.security` (for password hashing)
    * `json` (for handling resume content)
    * `io`, `os` (standard library for file operations)
* **AI/LLM Integration:**
    * `[OpenAI API / google-generativeai library]` (for integrating with [GPT-3.5/4 / Gemini-Pro] for content generation).
* **Database:**
    * [SQLite](https://www.sqlite.org/index.html) (for development - `site.db`)
    * (Optional: [PostgreSQL](https://www.postgresql.org/) or [MySQL](https://www.mysql.com/) for production)
* **Frontend (Conceptual / Future Implementation):**
    * HTML5, CSS3, JavaScript
    * [React](https://react.dev/) / [Vue.js](https://vuejs.org/) / [Angular](https://angular.io/) (Recommended for interactive UI)
    * [Figma](https://www.figma.com/) (for UI/UX design, if applicable)

## Getting Started

Follow these steps to set up the project locally for development and testing.

### Prerequisites

* Python 3.9+ installed on your system.
* `pip` (Python package installer).
* A valid API key for your chosen LLM (e.g., OpenAI API Key or Google Gemini API Key).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[your-username]/AI-Powered-Resume-Builder.git
    cd AI-Powered-Resume-Builder
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # If you don't have requirements.txt yet, run:
    # pip install Flask Flask-SQLAlchemy Flask-Login WeasyPrint openai # or google-generativeai
    ```
    * **Note:** After installing, it's good practice to create `requirements.txt`:
        ```bash
        pip freeze > requirements.txt
        ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory of your project.
    * **For OpenAI:**
        ```env
        OPENAI_API_KEY='your_openai_api_key_here'
        ```
    * **For Google Gemini:**
        ```env
        GOOGLE_GEMINI_API_KEY='your_gemini_api_key_here'
        ```
    * You might also want to set your Flask secret key here:
        ```env
        FLASK_SECRET_KEY='your_super_secret_key_here'
        ```
    * *Remember to never commit your `.env` file to Git! Ensure `.env` is in your `.gitignore`.*

### Running the Application

1.  **Initialize the database:**
    The first time you run the application, or if you modify your models, you need to create the database tables.
    ```bash
    # Make sure your virtual environment is active
    python -c "from app import app, db; with app.app_context(): db.create_all()"
    ```
    This command will create the `site.db` file in your project directory.

2.  **Start the Flask development server:**
    ```bash
    # Make sure your virtual environment is active
    flask run
    # Or for a more common development setup:
    # export FLASK_APP=app.py # On Windows: set FLASK_APP=app.py
    # flask run
    ```
    The application will typically run on `http://127.0.0.1:5000/`.

## API Endpoints

The backend exposes the following RESTful API endpoints:

| Method | Endpoint                          | Description                                         | Authentication Required |
| :----- | :-------------------------------- | :-------------------------------------------------- | :---------------------- |
| `POST` | `/register`                       | Register a new user.                                | No                      |
| `POST` | `/login`                          | Log in a user.                                      | No                      |
| `GET`  | `/logout`                         | Log out the current user.                           | Yes                     |
| `POST` | `/resume`                         | Create a new resume for the logged-in user.         | Yes                     |
| `GET`  | `/resume/<int:resume_id>`         | Get a specific resume by ID.                        | Yes                     |
| `PUT`  | `/resume/<int:resume_id>`         | Update an existing resume.                          | Yes                     |
| `DELETE` | `/resume/<int:resume_id>`       | Delete a resume.                                    | Yes                     |
| `POST` | `/ai/generate`                    | Request AI to generate content (summary, bullets, skills). | Yes                     |
| `GET`  | `/resume/<int:resume_id>/pdf`     | Export a resume as a PDF file.                      | Yes                     |

## Usage

**(This section assumes you have a basic frontend or are testing with tools like Postman/Insomnia/curl.)**

1.  **Register a User:** Send a `POST` request to `/register` with `username`, `email`, and `password`.
    ```json
    {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpassword123"
    }
    ```
2.  **Login:** Send a `POST` request to `/login` with `username` and `password`. This will set a session cookie.
    ```json
    {
        "username": "testuser",
        "password": "strongpassword123"
    }
    ```
3.  **Create/Save a Resume:** After logging in, send a `POST` request to `/resume` with your structured resume data.
    ```json
    {
        "title": "My First Resume",
        "content": {
            "personal_info": {
                "name": "Jane Doe",
                "email": "jane.doe@example.com",
                "phone": "123-456-7890",
                "linkedin": "[linkedin.com/in/janedoe](https://linkedin.com/in/janedoe)"
            },
            "summary": "Placeholder summary to be replaced by AI.",
            "experience": [
                {
                    "title": "Software Developer",
                    "company": "Innovate Corp",
                    "start_date": "Jan 2023",
                    "end_date": "Present",
                    "responsibilities": [
                        "Initial draft of responsibilities..."
                    ]
                }
            ],
            "skills": {
                "Programming Languages": ["Python", "JavaScript"]
            }
        }
    }
    ```
4.  **AI-Generate Content (e.g., Summary):** Send a `POST` request to `/ai/generate`.
    ```json
    {
        "type": "summary",
        "input": "I am a software developer with 3 years experience in Python and Flask, built web applications and led small teams."
    }
    ```
    The response will contain the AI-generated text. You can then update your resume with this content.
5.  **Export to PDF:** Once your resume content is finalized and saved (e.g., resume ID `1`), navigate your browser to `http://127.0.0.1:5000/resume/1/pdf` (after logging in via the frontend/Postman if using cookies) or configure your frontend to make a GET request to this endpoint.



