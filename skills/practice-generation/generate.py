import json
import argparse
import random

def generate_practice(topic, difficulty, count):
    templates = {
        "Math": [
            "Calculate the derivative of f(x) = {coeff}x^{power}",
            "Solve for x: {coeff}x + {const} = {result}"
        ],
        "Physics": [
            "A mass of {coeff}kg accelerates at {power}m/s^2. What is the force?",
            "Calculate the kinetic energy of a {coeff}kg object moving at {power}m/s."
        ]
    }
    
    domain = "Math" if "derivative" in topic.lower() or "algebra" in topic.lower() else "Physics"
    chosen_templates = templates.get(domain, ["Explain the core principles of {topic} in {difficulty} detail."])
    
    problems = []
    for i in range(count):
        coeff = random.randint(2, 10 * difficulty)
        power = random.randint(2, 5 * difficulty)
        const = random.randint(1, 20)
        result = coeff * random.randint(1, 10) + const
        
        template = random.choice(chosen_templates)
        question = template.format(coeff=coeff, power=power, const=const, result=result, topic=topic, difficulty=difficulty)
        
        problems.append({
            "id": f"prob_{i+1}",
            "question": question,
            "type": "calculation" if "Calculate" in question or "Solve" in question else "conceptual",
            "difficulty_level": difficulty
        })
        
    return {
        "topic": topic,
        "requested_difficulty": difficulty,
        "problem_count": count,
        "problems": problems
    }

def main():
    parser = argparse.ArgumentParser(description="Generate practice problems.")
    parser.add_argument("--topic", required=True, help="Topic for problems")
    parser.add_argument("--difficulty", type=int, default=1, choices=[1, 2, 3, 4, 5], help="Difficulty level 1-5")
    parser.add_argument("--count", type=int, default=3, help="Number of problems to generate")
    
    args = parser.parse_args()
    result = generate_practice(args.topic, args.difficulty, args.count)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
