import os
import json
import sys
import subprocess
import tempfile
from typing import Any, Dict, List, Optional

CURRICULUM_DIR = os.path.join(os.path.dirname(__file__), "curriculum")
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

# ─────────────────────────────────────────────────
#  PROGRESS TRACKING
# ─────────────────────────────────────────────────

def load_progress() -> Dict[str, List[str]]:
    """Load completed topic IDs from progress.json."""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {}


def save_progress(progress: Dict[str, List[str]]):
    """Save completed topic IDs to progress.json."""
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2)
    except IOError:
        pass


def mark_complete(module_id: str, topic_id: str):
    """Mark a topic as completed."""
    progress = load_progress()
    completed = progress.get(module_id, [])
    if topic_id not in completed:
        completed.append(topic_id)
    progress[module_id] = completed
    save_progress(progress)


def is_complete(module_id: str, topic_id: str) -> bool:
    """Check if a topic is marked as completed."""
    progress = load_progress()
    return topic_id in progress.get(module_id, [])


def get_module_progress(module_id: str, topics: List[Dict]) -> tuple:
    """Returns (completed_count, total_count)."""
    progress = load_progress()
    completed = progress.get(module_id, [])
    total = len([t for t in topics if isinstance(t, dict)])
    done = sum(1 for t in topics if isinstance(t, dict) and t.get("id") in completed)
    return done, total


# ─────────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────────

def load_modules() -> List[Dict[str, Any]]:
    """Scans the curriculum directory for lesson_info.json files."""
    modules = []
    if not os.path.exists(CURRICULUM_DIR):
        print(f"Error: Curriculum directory not found at {CURRICULUM_DIR}")
        return []

    for item in sorted(os.listdir(CURRICULUM_DIR)):
        module_path = os.path.join(CURRICULUM_DIR, item)
        if os.path.isdir(module_path):
            info_file = os.path.join(module_path, "lesson_info.json")
            if os.path.exists(info_file):
                try:
                    with open(info_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        data["path"] = module_path
                        data["id"] = item
                        modules.append(data)
                except json.JSONDecodeError:
                    print(f"Warning: Could not parse {info_file}")
    return modules


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("╔══════════════════════════════════════════╗")
    print("║       🤖  AI PYTHON LEARNING AGENT       ║")
    print("╚══════════════════════════════════════════╝")
    print()


def print_separator(char="─", width=44):
    print(char * width)


def print_box(text: str):
    lines = text.split("\n")
    width = max(len(line) for line in lines) + 4
    print("┌" + "─" * (width - 2) + "┐")
    for line in lines:
        print(f"│  {line:<{width - 4}}  │")
    print("└" + "─" * (width - 2) + "┘")


# ─────────────────────────────────────────────────
#  QUIZ ENGINE
# ─────────────────────────────────────────────────

def run_quiz(quiz_step: Dict[str, Any]) -> bool:
    """
    Runs a multiple-choice question. Returns True if answered correctly.
    Quiz step format:
      {
        "type": "quiz",
        "title": "Quick Check",
        "question": "What does ReLU(x) return for x=-3?",
        "options": ["3", "-3", "0", "1"],
        "answer": 2   # 0-indexed correct option
      }
    """
    question = quiz_step.get("question", "")
    options = quiz_step.get("options", [])
    correct_idx = quiz_step.get("answer", 0)

    print()
    print("  🧠  QUICK CHECK")
    print_separator("─", 44)
    print(f"  {question}")
    print()
    for i, opt in enumerate(options):
        print(f"    {i + 1}) {opt}")
    print()

    while True:
        try:
            ans = input("  Your answer (number): ").strip()
            if not ans.isdigit():
                print("  Please enter a number.")
                continue
            chosen = int(ans) - 1
            if 0 <= chosen < len(options):
                break
            print(f"  Please enter a number between 1 and {len(options)}.")
        except (ValueError, EOFError):
            continue

    if chosen == correct_idx:
        print()
        print("  ✅  Correct! Great work.")
        print()
        input("  Press Enter to continue...")
        return True
    else:
        print()
        print(f"  ❌  Not quite. The correct answer was: {options[correct_idx]}")
        print()
        input("  Press Enter to continue...")
        return False


# ─────────────────────────────────────────────────
#  SCRATCHPAD
# ─────────────────────────────────────────────────

def open_scratchpad():
    """Create a temp Python file and open it for the user to edit and run."""
    scratch_dir = os.path.join(os.path.dirname(__file__), "scratch")
    os.makedirs(scratch_dir, exist_ok=True)

    scratch_file = os.path.join(scratch_dir, "scratchpad.py")
    if not os.path.exists(scratch_file):
        with open(scratch_file, "w", encoding="utf-8") as f:
            f.write("# ✏️  Python Scratchpad — write and test your code here!\n\n")
            f.write("# Example:\n")
            f.write("# name = 'AI'\n")
            f.write("# print(f'Hello, {name}!')\n\n")

    clear_screen()
    print_header()
    print("  📝  SCRATCHPAD MODE")
    print_separator()
    print()
    print(f"  Scratch file: {scratch_file}")
    print()
    print("  Options:")
    print("   R) Run the scratchpad file")
    print("   O) Open file location in Explorer")
    print("   B) Back to menu")
    print()
    choice = input("  Select: ").strip().lower()

    if choice == 'r':
        print()
        print_separator()
        print("  ▶  Running scratchpad...\n")
        subprocess.run([sys.executable, scratch_file], check=False)
        print()
        input("  Press Enter to continue...")
    elif choice == 'o':
        os.startfile(scratch_dir)
        print("  📂  Opened scratch folder.")
        input("  Press Enter to continue...")


# ─────────────────────────────────────────────────
#  TUTORIAL RUNNER
# ─────────────────────────────────────────────────

def run_tutorial(module_path: str, topic: Dict[str, Any], module_id: str):
    """Runs the step-by-step tutorial for a topic."""
    tutorial_steps = topic.get("tutorial", [])
    topic_file = topic.get("file")
    topic_id = topic.get("id", "")
    total = len(tutorial_steps)
    quiz_passed = False

    clear_screen()
    print_header()
    print(f"  📖  TOPIC: {topic.get('title')}")
    print_separator()
    print()

    for i, step in enumerate(tutorial_steps):
        step_type = step.get("type")
        title = step.get("title", "")
        content = step.get("content", "")

        # Breadcrumb
        breadcrumb = f"  [{i + 1}/{total}]  {title}"
        print(breadcrumb)
        print_separator("─", len(breadcrumb.rstrip()))
        print()

        if step_type == "text":
            # Indent each content line for readability
            for line in content.split("\n"):
                print(f"  {line}")
            print()
            input("  Press Enter to continue...")
            print()

        elif step_type == "code":
            print("  Code Example:")
            print()
            print("  ┌─ python " + "─" * 30)
            for line in content.split("\n"):
                print(f"  │  {line}")
            print("  └" + "─" * 38)
            print()

            if step.get("run") and topic_file:
                action = input("  Press Enter to RUN this code (or 's' to skip): ").strip().lower()
                if action != 's':
                    file_path = os.path.join(module_path, topic_file)
                    if os.path.exists(file_path):
                        print()
                        print_separator("─", 44)
                        print(f"  ▶  Output of {topic_file}:")
                        print_separator("─", 44)
                        subprocess.run([sys.executable, file_path], check=False)
                        print_separator("─", 44)
                    else:
                        print(f"  Error: File {topic_file} not found.")
            else:
                input("  Press Enter to continue...")
            print()

        elif step_type == "quiz":
            result = run_quiz(step)
            if result:
                quiz_passed = True
            print()

    print_separator()
    print()
    if quiz_passed or not any(s.get("type") == "quiz" for s in tutorial_steps):
        print("  🎉  Tutorial Complete!")
        mark_complete(module_id, topic_id)
        print("  ✅  Topic marked as COMPLETE in your progress.")
    else:
        print("  📚  Tutorial Complete — keep practicing to pass the quiz!")
    print()
    input("  Press Enter to return to menu...")


# ─────────────────────────────────────────────────
#  MODULE MENU
# ─────────────────────────────────────────────────

def show_module_menu(module: Dict[str, Any]):
    module_id = module.get("id", "")
    while True:
        clear_screen()
        print_header()
        topics = module.get("topics", [])
        done, total = get_module_progress(module_id, topics)

        print(f"  📦  Module: {module.get('title', 'Unknown')}")
        print(f"  📝  {module.get('description', '')}")
        print(f"  🏆  Progress: {done}/{total} topics complete")
        print()
        print_separator()
        print("  Topics:")
        print()

        for idx, topic in enumerate(topics):
            if isinstance(topic, dict):
                tid = topic.get("id", "")
                check = "✓" if is_complete(module_id, tid) else " "
                print(f"    [{check}] {idx + 1}. {topic.get('title')}")
            else:
                print(f"    [ ] {idx + 1}. {topic}")

        print()
        print_separator()
        print("  Actions:")
        print("    E) Run Examples")
        print("    T) Run Tests")
        print("    S) Open Scratchpad")
        print("    B) Back to Main Menu")
        print()

        choice = input("  Select a topic (number) or action: ").strip().lower()

        if choice == 'b':
            break
        elif choice == 'e':
            examples_path = os.path.join(module["path"], "examples.py")
            if os.path.exists(examples_path):
                clear_screen()
                print_header()
                print_separator()
                print(f"  ▶  Running examples for {module.get('title')}...\n")
                print_separator()
                subprocess.run([sys.executable, examples_path], check=False)
                print_separator()
            else:
                print(f"\n  Error: examples.py not found.")
            input("\n  Press Enter to continue...")
        elif choice == 't':
            clear_screen()
            print_header()
            tests_path = os.path.join(module["path"], "tests.py")
            print_separator()
            print(f"  ▶  Running tests for {module.get('title')}...\n")
            print_separator()
            subprocess.run([sys.executable, tests_path], check=False)
            print_separator()
            input("\n  Press Enter to continue...")
        elif choice == 's':
            open_scratchpad()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(topics):
                    selected_topic = topics[idx]
                    if isinstance(selected_topic, dict) and "tutorial" in selected_topic:
                        run_tutorial(module["path"], selected_topic, module_id)
                    else:
                        print("\n  This topic does not have a tutorial yet.")
                        input("  Press Enter to continue...")
                else:
                    input("  Invalid selection. Press Enter...")
            except ValueError:
                input("  Invalid input. Press Enter...")


# ─────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────

def main():
    while True:
        clear_screen()
        print_header()
        modules = load_modules()

        if not modules:
            print("  No modules found. Please check the curriculum directory.")
            return

        print("  📚  Available Modules:")
        print()
        for idx, module in enumerate(modules):
            topics = module.get("topics", [])
            done, total = get_module_progress(module.get("id", ""), topics)
            difficulty = module.get("difficulty", "")
            bar_filled = int((done / total) * 10) if total else 0
            bar = "█" * bar_filled + "░" * (10 - bar_filled)
            print(f"    {idx + 1}. {module.get('title')}")
            print(f"       [{bar}] {done}/{total}  |  {difficulty}")
            print()

        print_separator()
        print("  H) Help & Tips   Q) Quit")
        print()
        choice = input("  Select a module (number) or action: ").strip().lower()

        if choice == 'q':
            print()
            print("  👋  Goodbye! Keep learning!")
            print()
            break
        elif choice == 'h':
            clear_screen()
            print_header()
            print_box(
                "HOW TO USE THIS PROGRAM\n"
                "\n"
                "1. Select a module by number.\n"
                "2. Select a topic to start a tutorial.\n"
                "3. Follow the steps and answer quiz questions.\n"
                "4. Press 'E' to see example programs.\n"
                "5. Press 'T' to run the test suite.\n"
                "6. Press 'S' to open a scratchpad to practice.\n"
                "\n"
                "Your progress is saved automatically!"
            )
            print()
            input("  Press Enter to continue...")
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(modules):
                    show_module_menu(modules[idx])
                else:
                    input("  Invalid selection. Press Enter...")
            except ValueError:
                input("  Invalid input. Press Enter...")


if __name__ == "__main__":
    main()
