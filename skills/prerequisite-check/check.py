import json
import argparse
import sys

def build_prerequisite_graph():
    return {
        "Calculus": ["Algebra", "Trigonometry"],
        "Algebra": ["Basic Arithmetic"],
        "Physics": ["Calculus", "Algebra"],
        "Machine Learning": ["Linear Algebra", "Calculus", "Probability"],
        "Linear Algebra": ["Algebra"]
    }

def check_prerequisites(target, known):
    graph = build_prerequisite_graph()
    visited = set()
    missing = []
    
    def dfs(node):
        if node in known:
            return
        if node not in visited:
            visited.add(node)
            if node in graph:
                for prereq in graph[node]:
                    dfs(prereq)
            missing.append(node)
            
    dfs(target)
    
    # Remove the target itself from missing if it got added
    if target in missing:
        missing.remove(target)
        
    return {
        "target_concept": target,
        "known_concepts": known,
        "missing_prerequisites": list(dict.fromkeys(missing)),
        "ready_to_learn": len(missing) == 0
    }

def main():
    parser = argparse.ArgumentParser(description="Check prerequisites for a STEM concept.")
    parser.add_argument("--target", required=True, help="Target concept to learn")
    parser.add_argument("--known", nargs="*", default=[], help="Concepts already known by the learner")
    
    args = parser.parse_args()
    
    result = check_prerequisites(args.target, args.known)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
