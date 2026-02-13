🚀 AI-Driven E-Learning Platform
A dynamic, full-stack Learning Management System (LMS) that leverages the Google Gemini LLM to generate real-time, interactive educational assessments. Built with Django and MongoDB, this platform features an asynchronous frontend and a privacy-first video delivery system.

💡 Overview
This project aims to bridge the gap between static video courses and active learning. By integrating a secure AI pipeline, the platform allows users to input any topic and instantly receive a structured, interactive quiz to test their knowledge alongside their video coursework.

✨ Key Features
Real-Time AI Quiz Generation: Integrates the Google Gemini 2.5 Flash API to dynamically generate course-specific quizzes.

Deterministic AI Responses: Enforces application/json MIME types at the API level to guarantee structured, easily parsable data without AI hallucination or markdown formatting errors.

Asynchronous Interactive UI: Utilizes Vanilla JavaScript and the Fetch API to provide a seamless, SPA-like experience (Single Page Application) for quiz generation and gameplay without page reloads.

Privacy-First Video Player: Employs the YouTube IFrame API via the youtube-nocookie domain to serve educational content without compromising user tracking data.

Flexible Data Architecture: Uses Django's JSONField integrated with MongoDB to handle complex, nested course modules and unpredictable AI-generated schemas without requiring rigid database migrations.

Secure Session Management: Features custom user authentication with secure password hashing and strict route protection (@login_required, @never_cache).

🛠️ Tech Stack
Backend: Python, Django, Django REST Framework (DRF)

Database: MongoDB (Integrated via custom compatibility bridge)

Frontend: HTML5, CSS3, Vanilla JavaScript (ES6+), Server-Side Rendering (SSR)

AI/External APIs: Google Generative AI (Gemini 2.5 Flash)

🏗️ Architectural Highlights
Client-Side State Management: Implements local JavaScript caching (quizStore) to hold generated AI data in browser memory, drastically reducing server load and ensuring zero-latency quiz initialization.

Server-Side Rendering (SSR) Injection: Decouples backend database queries from frontend logic by injecting serialized JSON state directly into the DOM during the initial page load, eliminating the need for secondary API fetching.

Graceful Error Handling: Employs strict guard clauses and HTTP status code management (400, 500) to ensure the application fails gracefully during external API timeouts or bad data payloads.

🗺️ Roadmap / Future Enhancements
[ ] Transition to native PyMongo/MongoEngine for long-term database stability.

[ ] Implement asynchronous Django views (async def) or a Celery task queue to handle concurrent AI API requests at scale.

[ ] Add granular video progress tracking utilizing the YouTube Player API.

[ ] Implement token-based authentication (JWT) for secure API endpoints.
