# LegalEdge AI

LegalEdge AI is an AI-powered legal practice management platform designed to help lawyers and clients manage cases, documents, payments, and communication from a single system. The platform provides secure role-based access, automated document generation, and real-time case updates.

---

## Features

### Authentication & Authorization

* JWT-based authentication
* Role-based access control (Lawyer / Client)
* Secure user registration and login
* Per-user data isolation

### Case Management

* Create and manage legal cases
* Track case status and deadlines
* Assign clients to cases
* Maintain case history

### Client Management

* Manage client profiles
* Store case-related information
* View case progress and updates

### Document Management

* Upload legal documents
* Generate PDF and DOCX files automatically
* Organize case documents securely

### Communication

* WhatsApp notifications using Twilio
* Automated case updates
* In-app notifications

### Payments

* Stripe payment integration
* Track invoices and transactions
* Secure payment processing

### AI Features

* AI-powered legal assistant
* Document analysis and summarization
* Smart recommendations
* Automated content generation

---

## Tech Stack

### Backend

* Django
* Django REST Framework
* Python

### Database

* SQLite / PostgreSQL

### Authentication

* JWT Authentication

### APIs & Integrations

* Twilio API
* Stripe API

### Document Processing

* PDF Generation
* DOCX Generation

### Deployment & Tools

* Git
* GitHub
* Postman

---

## Project Structure

```text
legaledge-ai/

├── accounts/
├── clients/
├── cases/
├── documents/
├── billing/
├── communication/
├── ai_engine/
├── analytics/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Workflow

1. Users register as either a lawyer or a client.
2. Lawyers create and manage cases.
3. Clients can view their assigned cases.
4. Documents are uploaded and stored securely.
5. AI assists with document processing and recommendations.
6. Notifications are sent automatically.
7. Payments are processed through Stripe.

---

## API Endpoints

| Method | Endpoint                | Description                 |
| ------ | ----------------------- | --------------------------- |
| POST   | `/api/auth/register`    | Register a new user         |
| POST   | `/api/auth/login`       | Login and receive JWT token |
| GET    | `/api/cases`            | Retrieve all cases          |
| POST   | `/api/cases`            | Create a new case           |
| GET    | `/api/clients`          | Retrieve clients            |
| POST   | `/api/documents/upload` | Upload legal documents      |
| POST   | `/api/payments/create`  | Create payment session      |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ankitaparasher04/legaledge-ai.git

cd legaledge-ai
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
SECRET_KEY=your_secret_key

DATABASE_URL=your_database_url

TWILIO_ACCOUNT_SID=your_twilio_sid

TWILIO_AUTH_TOKEN=your_twilio_token

STRIPE_SECRET_KEY=your_stripe_key
```

---

### 5. Apply migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## Future Roadmap

### Platform Features

* Lawyer dashboard
* Advanced search and filtering
* Appointment scheduling
* Case analytics

### AI Features

* Legal document summarization
* AI-powered legal research
* Smart case recommendations
* Chat-based legal assistant

### Infrastructure

* Docker support
* CI/CD pipeline
* Cloud deployment
* Monitoring and logging

---

## Contributing

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Ankita Parasher**

* GitHub: https://github.com/ankitaparasher04
* LinkedIn: Add your LinkedIn profile here.
