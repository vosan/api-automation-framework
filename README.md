# API Automation Framework

## Overview

This project is a lightweight API automation framework built in Python for validating REST API responses.

The framework was designed with scalability and maintainability in mind rather than as a single standalone test script. While the current implementation validates a single endpoint from the Trade Me Sandbox API, the structure supports easy expansion for additional endpoints, environments, and test suites.

The test validates the following acceptance criteria:

- `Name = "Carbon credits"`
- `CanRelist = true`
- The `Promotion` with `Name = "Gallery"` contains `"Good position in category"` in its description

---

# Tech Stack

- Python 3.12+
- pytest
- requests
- pydantic
- pytest-html

---

# Framework Structure

```text
api-automation-framework/
├── assertions/     # Reusable business validations
├── clients/        # API communication layer
├── config/         # Environment configuration
├── models/         # Typed response models
├── tests/          # Test cases
├── utils/          # Shared utilities and logging
├── reports/        # Generated test reports
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Design Approach

The framework follows a layered architecture with separation of concerns between:

| Layer | Responsibility |
|---|---|
| Client Layer | Handles HTTP communication |
| Model Layer | Maps API responses into typed objects |
| Assertion Layer | Contains reusable business validations |
| Test Layer | Orchestrates test execution |
| Config Layer | Centralizes environment configuration |

This structure keeps tests small, readable, and maintainable as the framework grows.

---

# Key Design Decisions

## Typed Response Models

Pydantic models are used for response deserialization and validation instead of raw dictionary parsing.

Benefits:
- type safety
- cleaner test code
- better maintainability
- automatic schema validation

---

## Reusable API Client

API communication is centralized in reusable client classes rather than implemented directly inside tests.

This allows:
- shared session management
- centralized timeout handling
- easier request logging
- scalable endpoint expansion

---

## Centralized Assertions

Business validations are separated from test execution logic.

This keeps tests focused on behavior while allowing assertions to remain reusable and easy to maintain.

---

## Logging

Request and response logging is centralized to simplify debugging and improve test observability.

---

# Setup

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run all tests:

```bash
pytest
```

---

# Environment Configuration

The framework supports overriding the API base URL through environment variables.

Example:

```bash
export BASE_URL=https://api.tmsandbox.co.nz
```

If no environment variable is provided, the default sandbox URL is used.

---

# Reporting

The framework supports HTML report generation using `pytest-html`.

Reports include:
- execution summary
- passed/failed tests
- assertion failures
- stack traces
- captured logs

Generated reports are stored in:

```text
reports/
```

---

# Scalability Considerations

Although the assessment requires validating a single endpoint, the framework structure was designed to scale cleanly for larger API test suites.

The current architecture supports:
- additional API clients
- multiple environments
- shared authentication handling
- reusable assertions
- request/response logging
- CI/CD integration

without requiring structural changes to the framework itself.