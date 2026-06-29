# BrokenPilot Prototype Safety Notes

BrokenPilot is intentionally vulnerable and must be treated as a local-only training target.

## Rules

1. Run locally only.
2. Do not expose to the internet.
3. Do not connect to real internal tools.
4. Do not use real customer, employee, or production data.
5. Do not store real API keys in the prototype.
6. Do not run with privileged Docker settings unless absolutely necessary.
7. Keep logs fake and local.
8. Reset lab data after use.

## Network exposure

Bind to localhost by default:

```text
127.0.0.1:8080
```

Avoid:

```text
0.0.0.0:8080
```

unless the instructor intentionally runs in an isolated classroom network.

## Data safety

All data should be synthetic.

Never include:

- Real names
- Real incidents
- Real service names
- Real credentials
- Real tokens
- Real internal documents
- Real customer records

## Provider safety

The first prototype should use mock LLM mode to avoid external provider exposure.

If optional real LLM mode is later added, docs must clearly explain:

- What data is sent to the provider
- How to avoid sending sensitive data
- How to configure local-only mode
- How to remove API keys after testing

## Instructor note

The point of the prototype is to teach defensive security. It should not become an uncontrolled offensive playground.
