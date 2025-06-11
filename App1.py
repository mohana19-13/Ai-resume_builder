mkdir ai_resume_builder
cd ai_resume_builder
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install Flask Flask-SQLAlchemy Flask-Login WeasyPrint openai  # or google-generativeai

