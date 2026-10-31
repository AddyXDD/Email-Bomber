#Simple Email-Bomber

<p align="center">
  A minimal Python SMTP automation experiment.
  <br>
  Exploring email protocols, SMTP authentication and Python automation.
</p>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python)
![Protocol](https://img.shields.io/badge/Protocol-SMTP-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Legacy-yellow?style=flat-square)

---

## About

Email-Bomber is a small Python project demonstrating SMTP-based email communication using Python's built-in `smtplib` library.

The original script demonstrates:
- SMTP server connections
- STARTTLS encryption
- SMTP authentication
- Sender and recipient configuration
- Message delivery through Python

This repository is an experimental learning project, not a production-ready email service.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| smtplib | SMTP communication |
| SMTP | Email transfer protocol |
| STARTTLS | Connection encryption |

## Installation

Clone the repository:

```bash
git clone https://github.com/AddyXDD/Email-Bomber.git
```

Navigate into the project:

```bash
cd Email-Bomber
```

No third-party Python packages are required by the original script.

## Configuration

The original script contains SMTP configuration placeholders:

```python
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587
```

SMTP authentication should use secure, provider-approved credentials.

Never hardcode passwords or upload credentials to a public repository.

## Important Security Notice

The original source contains an automated high-volume email loop.

**Do not execute it as published.**

Unrestricted repeated email delivery can:
- Violate email provider policies
- Trigger spam detection
- Cause account restrictions
- Disrupt recipients' inboxes

For legitimate experimentation, use a local mail-testing environment or a controlled, single-message test with an account you own.

## Disclaimer

This project is provided for educational purposes.

The author does not endorse spam, harassment, phishing, or unauthorized email distribution.

Users are responsible for ensuring that any testing is authorized and complies with applicable laws and service-provider policies.

## Author

**AddyXDD**

GitHub: [@AddyXDD](https://github.com/AddyXDD)

---

<p align="center">
  Made with Python 🐍
  <br>
  <sub>Learn • Experiment • Build</sub>
</p>
