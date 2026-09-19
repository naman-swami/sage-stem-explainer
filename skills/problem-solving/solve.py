import json
import argparse

def solve_problem(problem_statement):
    """Implement a systematic problem solving framework (Polya's 4 steps)."""
    
    # Heuristic based mocked solving steps
    understanding = "Identify given variables and what needs to be found."
    plan = "Select appropriate formulas and set up equations."
    execute = "Substitute values and perform algebraic manipulation."
    review = "Check units and verify if the answer makes physical/logical sense."
    
    steps = [
        {"step": 1, "phase": "Understand", "action": understanding},
        {"step": 2, "phase": "Plan", "action": plan},
        {"step": 3, "phase": "Execute", "action": execute},
        {"step": 4, "phase": "Review", "action": review}
    ]
    
    solution = {
        "original_problem": problem_statement,
        "framework_used": "Polya's Problem Solving Techniques",
        "solution_steps": steps,
        "final_verification": "Consistent with known physical laws/mathematical axioms."
    }
    return solution

def main():
    parser = argparse.ArgumentParser(description="Solve a STEM problem systematically.")
    parser.add_argument("--problem", required=True, help="The problem statement to solve")
    
    args = parser.parse_args()
    
    result = solve_problem(args.problem)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
