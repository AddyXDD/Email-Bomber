# ⚡ EMAIL-BOMBER

### A Python-based SMTP email sender with an interactive terminal experience.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SMTP-Gmail%20STARTTLS-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-Terminal-111111?style=for-the-badge&logo=windows-terminal&logoColor=white" />
</p>

---

## `01` — Overview

**Email-Bomber** is a lightweight Python application built around Gmail SMTP. It combines email configuration, SMTP authentication, message previews, and an interactive command-line interface.

Designed with simplicity and a terminal-first experience in mind.

## `02` — Features

| Feature | Description |
|---|---|
| ⚡ Interactive CLI | Menu-driven terminal interface |
| 🎨 Styled Interface | Custom ASCII banner and colored output |
| 📡 SMTP Integration | Gmail SMTP with STARTTLS |
| 🔐 Authentication | Gmail App Password support |
| ✉️ Message Builder | Custom subject and message body |
| 👁️ Preview | Review message details before sending |
| 🛠️ Error Handling | SMTP and connection error reporting |

## `03` — Preview

```text
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║

             SMTP TESTING TOOLKIT
                  VERSION 2.0
```

## `04` — Installation

**Clone the repository**

```bash
git clone https://github.com/AddyXDD/Email-Bomber.git
cd Email-Bomber
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

## `05` — Launch

```bash
python email-spammer.py
```

### Available options

| Option | Action |
|:---:|---|
| `1` | Configure SMTP |
| `2` | Test SMTP connection |
| `3` | Preview and send test email |
| `4` | Exit |

## `06` — Configuration

| Setting | Value |
|---|---|
| SMTP Host | `smtp.gmail.com` |
| SMTP Port | `587` |
| Encryption | STARTTLS |
| Authentication | Gmail App Password |

Use a Gmail App Password rather than your regular Google account password.

## `07` — Tech Stack

- **Python** — Core application
- **smtplib** — SMTP communication
- **EmailMessage** — Email construction
- **Colorama** — Terminal styling
- **getpass** — Secure credential input (when configured)

## `08` — Repository Structure

```text
Email-Bomber/
│
├── email-spammer.py
├── requirements.txt
└── README.md
```

## `09` — Security & Responsible Use

- Keep credentials and App Passwords private.
- Never commit secrets to GitHub.
- Only contact recipients who have agreed to receive your messages.
- Respect Gmail sending restrictions and anti-abuse policies.

---

<p align="center">
  <strong>BUILT WITH PYTHON.</strong>
  <br/>
  <sub>Developed by <a href="https://github.com/AddyXDD">AddyXDD</a></sub>
</p>
