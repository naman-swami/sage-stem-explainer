#!/usr/bin/env python3
"""Emit a deterministic concept-breakdown outline from a topic."""
import json
import sys


def main() -> None:
    topic = " ".join(sys.argv[1:]).strip() or "the requested STEM concept"
    outline = {
        "goal": f"Explain {topic} clearly and checkably",
        "steps": [
            "Clarify the learner's target and prerequisites",
            "Give the plain-language intuition",
            "Introduce notation and derive the result step by step",
            "Run a units, limiting-case, or example sanity check",
            "Summarize the takeaway and state remaining uncertainty",
        ],
    }
    print(json.dumps(outline, indent=2))


if __name__ == "__main__":
    main()
