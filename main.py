# main.py
# Entry point for the Purple Team & Agentic AI Roadmap.
# Run this file to launch the interactive roadmap terminal.
# Author: KyberPhantasma
#
# Usage:
#   python main.py
#
# Requirements:
#   Python 3.6+
#   No external libraries — runs on Pydroid3
#   Progress saved automatically to progress.json

from tracker import Tracker

BANNER = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🧭 PURPLE TEAM & AGENTIC AI ROADMAP                    ║
║   KyberPhantasma — Beginner to Pro                       ║
║                                                          ║
║   Laptop-First · All Free Resources                      ║
║   Web2 Security · Web3 Auditing · AI Agents              ║
║                                                          ║
║   "The guide is complete. The rest is execution."        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""

HELP_TEXT = """
┌─────────────────────────────────────────────────────┐
│  ROADMAP COMMAND REFERENCE                          │
├─────────────────────────────────────────────────────┤
│  overview              — Show all phases + progress │
│  phase <n>             — Open a phase  (e.g. phase 1)│
│  deliverables <n>      — Phase checklist            │
│  check <phase> <item>  — Toggle deliverable done    │
│  resources <n>         — Phase resource list        │
│  all                   — Master checklist all phases│
│  start                 — Show your first actions    │
│  progress              — Overall progress summary   │
│  help                  — Show this menu             │
│  exit                  — Exit the roadmap           │
├─────────────────────────────────────────────────────┤
│  EXAMPLES:                                          │
│  phase 0                                            │
│  phase 3                                            │
│  deliverables 1                                     │
│  check 1 3   (mark Phase 1 deliverable 3 done)      │
│  resources 2                                        │
│  all                                                │
└─────────────────────────────────────────────────────┘
"""


def show_progress_summary(tracker):
    """Print a clean progress summary across all phases."""
    print()
    print("  ── PROGRESS SUMMARY ──────────────────────────────")
    for phase in tracker.phases:
        done, total = tracker.phase_progress(phase)
        bar_filled = int((done / total) * 20) if total else 0
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        pct = int((done / total) * 100) if total else 0
        print(f"  Phase {phase['number']}  [{bar}] {pct:>3}%  {phase['title']}")
    total_done, total_all = tracker.overall_progress()
    print("  ──────────────────────────────────────────────────")
    bar_filled = int((total_done / total_all) * 20) if total_all else 0
    bar = "█" * bar_filled + "░" * (20 - bar_filled)
    pct = int((total_done / total_all) * 100) if total_all else 0
    print(f"  TOTAL    [{bar}] {pct:>3}%  {total_done}/{total_all} deliverables\n")


def run():
    """Main interactive loop for the Roadmap terminal."""
    print(BANNER)

    tracker = Tracker()

    # Check if saved progress exists
    import os
    if os.path.exists("progress.json"):
        total_done, _ = tracker.overall_progress()
        if total_done > 0:
            print(f"  ✓ Progress loaded. {total_done} deliverables completed.\n")

    print("  Type 'overview' to see all phases or 'help' for commands.\n")

    while True:
        try:
            raw = input("ROADMAP › ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Roadmap closed. Stay consistent.\n")
            break

        if not raw:
            continue

        parts = raw.split()
        command = parts[0].lower()
        args = parts[1:]

        # ── Commands ──────────────────────────────────────────────

        if command == "exit":
            print("\n  Roadmap closed. Stay consistent.\n")
            break

        elif command == "help":
            print(HELP_TEXT)

        elif command == "overview":
            print(tracker.format_overview())

        elif command == "start":
            print(tracker.format_first_actions())

        elif command == "progress":
            show_progress_summary(tracker)

        elif command == "all":
            print(tracker.format_all_deliverables())

        elif command == "phase":
            if not args:
                print("  Usage: phase <number>  (e.g. phase 1)")
            else:
                phase = tracker.get_phase(args[0])
                if not phase:
                    print(f"  Phase '{args[0]}' not found. Phases are 0 through 4.")
                else:
                    print(tracker.format_phase(phase))

        elif command == "deliverables":
            if not args:
                print("  Usage: deliverables <phase number>  (e.g. deliverables 1)")
            else:
                phase = tracker.get_phase(args[0])
                if not phase:
                    print(f"  Phase '{args[0]}' not found.")
                else:
                    print(tracker.format_deliverables(phase))

        elif command == "resources":
            if not args:
                print("  Usage: resources <phase number>  (e.g. resources 2)")
            else:
                phase = tracker.get_phase(args[0])
                if not phase:
                    print(f"  Phase '{args[0]}' not found.")
                else:
                    print(tracker.format_resources(phase))

        elif command == "check":
            # check <phase_number> <deliverable_number>
            if len(args) < 2:
                print("  Usage: check <phase> <item>  (e.g. check 1 3)")
            else:
                phase = tracker.get_phase(args[0])
                if not phase:
                    print(f"  Phase '{args[0]}' not found.")
                elif not args[1].isdigit():
                    print(f"  Deliverable number must be a number (e.g. check 1 3)")
                else:
                    index = int(args[1]) - 1  # convert to 0-based
                    if index < 0 or index >= len(phase["deliverables"]):
                        print(
                            f"  Deliverable {args[1]} not found in Phase {phase['number']}. "
                            f"Valid range: 1-{len(phase['deliverables'])}"
                        )
                    else:
                        new_state = tracker.toggle_deliverable(phase, index)
                        deliverable = phase["deliverables"][index]
                        status = "✓ COMPLETE" if new_state else "○ INCOMPLETE"
                        print(f"\n  [{status}] {deliverable}")
                        print(f"  Progress saved to {__import__('os').path.abspath('progress.json')}\n")

        else:
            print(f"  Unknown command: '{command}'. Type 'help' for options.")


if __name__ == "__main__":
    run()
