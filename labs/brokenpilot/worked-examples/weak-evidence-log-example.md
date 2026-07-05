# Weak Example  -  BrokenPilot Evidence Log

This is an example of a weak evidence log entry.

## Finding

The agent can update tickets it should not update.

## Evidence

I tried to close a ticket and it worked.

## Risk

This is bad because users can do things they should not do.

## Fix

Add authorization.

## Why this is weak

This evidence log is not useful because it does not include:

- The exact endpoint or tool.
- The user identity.
- The user's tenant.
- The target ticket.
- The target ticket's tenant.
- The request payload.
- The observed response.
- The expected secure behavior.
- The root cause.
- The violated security property.
- The tested mitigation.

An engineer cannot reproduce it, and a risk owner cannot understand impact.

## Better version

A stronger version would say:

```text
Alice from tenant alpha closed TCK-2001 from tenant beta through update_ticket while ENABLE_TOOL_AUTHZ=false. The tool returned result=updated and authorization_decision=not_checked. With ENABLE_TOOL_AUTHZ=true, the same request returned HTTP 403 tool_authorization_denied.
```
