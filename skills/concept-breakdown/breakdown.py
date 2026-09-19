import json
import argparse
import sys

def breakdown_concept(concept, depth=2):
    """Breaks down a STEM concept into smaller atomic parts."""
    # Mock knowledge base for demonstration purposes
    database = {
        "Photosynthesis": {
            "definition": "Process by which plants convert light energy into chemical energy.",
            "components": [
                {"name": "Light-dependent reactions", "complexity": "High"},
                {"name": "Calvin cycle", "complexity": "High"},
                {"name": "Chlorophyll", "complexity": "Medium"}
            ]
        },
        "Derivative": {
            "definition": "Rate of change of a function with respect to a variable.",
            "components": [
                {"name": "Limits", "complexity": "Medium"},
                {"name": "Power Rule", "complexity": "Low"},
                {"name": "Chain Rule", "complexity": "High"}
            ]
        }
    }
    
    data = database.get(concept, {
        "definition": f"General concept of {concept}.",
        "components": [{"name": f"Core principle of {concept}", "complexity": "Medium"}]
    })
    
    result = {
        "concept": concept,
        "breakdown_depth": depth,
        "definition": data["definition"],
        "sub_components": data["components"],
        "recommended_learning_order": [c["name"] for c in sorted(data["components"], key=lambda x: {"Low": 1, "Medium": 2, "High": 3}[x["complexity"]])]
    }
    return result

def main():
    parser = argparse.ArgumentParser(description="Break down a STEM concept.")
    parser.add_argument("--concept", required=True, help="The concept to break down")
    parser.add_argument("--depth", type=int, default=2, help="Depth of breakdown")
    
    args = parser.parse_args()
    
    result = breakdown_concept(args.concept, args.depth)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
