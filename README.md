# SimpleMP

SimpleMP is a well tested, Python-first media processing API that provides a clean, reliable interface over FFmpeg through PyAV — without exposing users to the complexities of codec quirks or invalid configurations.

It focuses on deterministic behavior, strict validation, and sensible defaults to ensure media transcoding is predictable, repeatable, and easy to integrate in production.

## Why simplemp?

FFmpeg is powerful, but:

* The API surface is complex 
* PyAV exposes low-level internals directly
* Codec support is inconsistent across builds
* Invalid inputs can cause silent failures
* Filter graphs can segfault or misbehave
* Validation is basically up to the user

SimpleMP fixes this by providing a well-defined, safe, high-level API that handles:

* Input introspection
* Codec capability validation
* Sample format negotiation
* Channel layout enforcement
* Sample rate clamping
* Container compatibility checks
* Error handling and reporting
* So developers can focus on using it, not debugging it.

## Core Features
### Simple, high-level API

```
from simplemp import process_media

    process_media(
        input="input.mp4",
        output="output.mkv",
        codec="opus",
        bitrate=256000,
        sample_rate=48000,
        sample_fmt="flt",
        
    )
```

No direct FFmpeg arguments.
No command strings.
Safe, predictable, declarative config.


## Deterministic Validation Layer

SimpleMP includes a reliable validation system that rejects invalid or unsafe configurations before encoding begins.

Validation includes:

codec ↔ container compatibility

codec ↔ sample format compatibility

codec ↔ channel count support

codec ↔ sample rate range

bitrate sanity checks

output path and directory checks

Over 30 validation tests are executed against supported formats.

Industrial reliable correctness, in Python.


## Codec Support (Audio)

Lossy:
AAC
MP3
Opus
Vorbis
Speex
WMA v1/v2

Lossless:
FLAC
ALAC
PCM (8–32 bit, be/le)
A-Law
µ-Law

## File Formats

Multi-container support:
.mp3
.m4a
.opus
.ogg
.oga
.flac
.wav
.3gp
.aif / .aifc / .aiff
.wma
.aac
.adts

## Test Suite & Quality Assurance

SimpleMP is tested like a industry grade project:

250+ test matrix entries in total
Tests for all valid codec/sample-fmt combinations
Tests for invalid combinations
Tests for failure mode correctness
Static analysis (mypy)
Unit tests + integration tests