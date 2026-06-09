# tracker.py
# The Tracker class manages roadmap navigation, progress
# tracking, and persistent save/load via JSON.
# Author: KyberPhantasma

import json
import os
import textwrap
from data import PHASES, FIRST_ACTIONS, PRINCIPLES

SAVE_FILE = "progress.json"
WIDTH = 62


# ── Formatting Helpers ─────────────────────────────────────────────

def rule(char="─", width=WIDTH):
    return char * width

def wrap(text, indent=2):
    prefix = " " * indent
    return textwrap.fill(
        text,
        width=WIDTH - indent,
        initial_indent=prefix,
        subsequent_indent=prefix,
    )

def progress_bar(done, total, width=30):
    if total == 0:
        return "[" + "░" * width + "] 0%"
    filled = int((done / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    pct = int((done / total) * 100)
    return f"[{bar}] {pct}%  ({done}/{total})"


# ── Tracker Class ──────────────────────────────────────────────────

class Tracker:
    """
    Manages roadmap navigation and deliverable progress.

    Features:
    - Load and display any phase with full detail
    - Mark deliverables complete/incomplete
    - Persist progress to a local JSON file
    - Show overall and per-phase progress
    - View weekly breakdowns and resources
    """

    def __init__(self):
        self.phases = PHASES
        self.progress = self._load_progress()

    # ── Persistence ────────────────────────────────────────────────

    def _load_progress(self):
        """
        Load saved progress from progress.json.
        If the file does not exist, initialise empty progress.
        """
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        # Initialise: every deliverable starts as False (incomplete)
        return {
            phase["id"]: [False] * len(phase["deliverables"])
            for phase in self.phases
        }

    def save_progress(self):
        """Write current progress to progress.json."""
        try:
            with open(SAVE_FILE, "w") as f:
                json.dump(self.progress, f, indent=2)
            return True
        except IOError:
            return False

    # ── Phase Lookups ──────────────────────────────────────────────

    def get_phase(self, identifier):
        """
        Find a phase by number string ('0'-'4') or id ('p0'-'p4').
        Returns the phase dict or None.
        """
        identifier = str(identifier).strip().lower()
        for phase in self.phases:
            if phase["number"] == identifier.zfill(2):
                return phase
            if phase["id"] == identifier:
                return phase
            if identifier == phase["number"].lstrip("0") or identifier == "0" and phase["number"] == "00":
                return phase
        return None

    def all_phase_ids(self):
        return [p["id"] for p in self.phases]

    # ── Progress Calculations ──────────────────────────────────────

    def phase_progress(self, phase):
        """Return (done, total) for a phase's deliverables."""
        checks = self.progress.get(phase["id"], [])
        done = sum(1 for c in checks if c)
        return done, len(phase["deliverables"])

    def overall_progress(self):
        """Return (done, total) across all phases."""
        total_done = 0
        total_all = 0
        for phase in self.phases:
            done, total = self.phase_progress(phase)
            total_done += done
            total_all += total
        return total_done, total_all

    def toggle_deliverable(self, phase, index):
        """
        Toggle a deliverable at the given index for a phase.
        Returns the new state (True = complete).
        """
        checks = self.progress.get(phase["id"], [])
        if 0 <= index < len(checks):
            checks[index] = not checks[index]
            self.progress[phase["id"]] = checks
            self.save_progress()
            return checks[index]
        return None

    # ── Formatters ─────────────────────────────────────────────────

    def format_overview(self):
        """Format the full roadmap overview with all phases."""
        total_done, total_all = self.overall_progress()
        lines = [
            rule("═"),
            "  PURPLE TEAM & AGENTIC AI ROADMAP",
            "  KyberPhantasma — Beginner to Pro",
            rule("═"),
            "",
            f"  OVERALL PROGRESS  {progress_bar(total_done, total_all)}",
            "",
            rule(),
            "  PHASES",
            rule(),
        ]
        for phase in self.phases:
            done, total = self.phase_progress(phase)
            bar = progress_bar(done, total, width=20)
            lines.append(
                f"  Phase {phase['number']}  {phase['title']:<28}  {bar}"
            )
        lines += [
            rule(),
            "  Type 'phase <number>' to open a phase. (e.g. phase 0)",
            rule(),
        ]
        return "\n".join(lines)

    def format_phase(self, phase):
        """Format a phase with sections and weekly breakdown."""
        done, total = self.phase_progress(phase)
        lines = [
            "",
            rule("═"),
            f"  PHASE {phase['number']}  —  {phase['title'].upper()}",
            f"  {phase['duration']}",
            rule("═"),
            "",
            wrap(phase["summary"]),
            "",
            rule(),
        ]

        # Sections
        for section in phase["sections"]:
            lines.append(f"\n  ► {section['title'].upper()}")
            lines.append("")

            if section["type"] == "text":
                lines.append(wrap(section["content"], indent=4))

            elif section["type"] == "list":
                for item in section["items"]:
                    lines.append(f"    · {item}")

            elif section["type"] == "code":
                lines.append("    ┌─ terminal ──────────────────────────")
                for line in section["content"].split("\n"):
                    lines.append(f"    │  {line}")
                lines.append("    └────────────────────────────────────")

            lines.append("")

        # Weekly breakdown
        if phase["weekly_breakdown"]:
            lines += [rule(), "  WEEKLY BREAKDOWN", rule()]
            for row in phase["weekly_breakdown"]:
                lines.append(f"\n  [{row['period']}]  {row['focus']}")
                lines.append(wrap(row["action"], indent=4))

        # Background threads
        if phase["background_threads"]:
            lines += ["", rule(), "  BACKGROUND THREADS (run in parallel)", rule()]
            for thread in phase["background_threads"]:
                lines.append(f"\n  ◦ {thread}")

        lines += ["", rule()]
        return "\n".join(lines)

    def format_deliverables(self, phase):
        """Format the deliverables checklist for a phase."""
        checks = self.progress.get(phase["id"], [])
        done, total = self.phase_progress(phase)
        lines = [
            "",
            rule("═"),
            f"  PHASE {phase['number']} DELIVERABLES — {phase['title'].upper()}",
            rule("═"),
            f"  Progress: {progress_bar(done, total)}",
            rule(),
        ]
        for i, deliverable in enumerate(phase["deliverables"]):
            status = "✓" if (i < len(checks) and checks[i]) else "○"
            num = str(i + 1).zfill(2)
            lines.append(f"\n  [{status}] {num}  {deliverable}")

        lines += [
            "",
            rule(),
            "  Type 'check <phase> <number>' to mark a deliverable done.",
            "  Example: check 1 3   (Phase 1, deliverable 3)",
            rule(),
        ]
        return "\n".join(lines)

    def format_resources(self, phase):
        """Format the resource list for a phase."""
        lines = [
            "",
            rule("═"),
            f"  PHASE {phase['number']} RESOURCES — {phase['title'].upper()}",
            rule("═"),
        ]
        if not phase["resources"]:
            lines.append("\n  No specific resources listed for this phase.")
        else:
            for resource in phase["resources"]:
                lines.append(f"  › {resource}")
        lines += ["", rule()]
        return "\n".join(lines)

    def format_first_actions(self):
        """Format the First Actions block."""
        lines = [
            rule("═"),
            "  YOUR FIRST ACTIONS",
            rule("═"),
        ]
        for action in FIRST_ACTIONS:
            lines.append("")
            lines.append(wrap(action, indent=2))
        lines += ["", rule("═"), "  PRINCIPLES", rule("═")]
        for p in PRINCIPLES:
            lines.append(f"\n  ✦  {p}")
        lines += ["", rule()]
        return "\n".join(lines)

    def format_all_deliverables(self):
        """Format a combined checklist across all phases."""
        total_done, total_all = self.overall_progress()
        lines = [
            rule("═"),
            "  MASTER DELIVERABLES CHECKLIST",
            f"  {progress_bar(total_done, total_all)}",
            rule("═"),
        ]
        for phase in self.phases:
            done, total = self.phase_progress(phase)
            checks = self.progress.get(phase["id"], [])
            lines.append(f"\n  PHASE {phase['number']} — {phase['title'].upper()}")
            lines.append(f"  {progress_bar(done, total, width=20)}")
            for i, deliverable in enumerate(phase["deliverables"]):
                status = "✓" if (i < len(checks) and checks[i]) else "○"
                lines.append(f"    [{status}] {deliverable}")
        lines += ["", rule()]
        return "\n".join(lines)
