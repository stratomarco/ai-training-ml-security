# BrokenPilot Insecure Output Handling Lab

## Purpose

This lab makes Module 05 insecure output handling observable. The model is allowed to produce text. The failure happens when a downstream component embeds that text into an HTML context without context-appropriate encoding.

The payload is benign and deterministic:

```html
<b>OUTPUT_SINK_TRIGGERED</b>
```

It is not a working script. It is a visible marker that proves model-derived text reached an HTML sink raw.

## Vulnerable run

Run BrokenPilot with default controls and send this request to `/render`:

```json
{
  "user_id": "alice",
  "message": "render output sink html formatting widget beta",
  "top_k": 4
}
```

Expected observation:

```text
output_handling_decision: raw
<b>OUTPUT_SINK_TRIGGERED</b>
```

## Controlled run

Enable output encoding:

```powershell
$env:ENABLE_OUTPUT_ENCODING="true"
```

```bash
export ENABLE_OUTPUT_ENCODING=true
```

Run the same request again. Expected observation:

```text
output_handling_decision: encoded
&lt;b&gt;OUTPUT_SINK_TRIGGERED&lt;/b&gt;
```

## Real control

The control is not asking the model to avoid dangerous output. The control is context-appropriate output handling at the sink: HTML encoding for HTML, parameterization for SQL, argument allowlists for tools, and shell avoidance or strict argument construction for command contexts.
