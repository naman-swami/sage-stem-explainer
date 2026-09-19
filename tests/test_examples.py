import os
import pytest
import glob

@pytest.mark.structure
def test_examples_format(project_root):
    examples_dir = os.path.join(project_root, 'examples')
    if not os.path.exists(examples_dir):
        pytest.skip("No examples directory found.")
        
    example_files = glob.glob(os.path.join(examples_dir, '**', '*.md'), recursive=True)
    
    for example_file in example_files:
        with open(example_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            
            # Verify Example format requirements
            has_goal = 'question' in content or 'goal' in content
            has_steps = 'step' in content
            has_check = 'check' in content or 'takeaway' in content
            
            assert has_goal, f"Example {example_file} missing Question/Goal"
            assert has_steps, f"Example {example_file} missing Step headings"
            assert has_check, f"Example {example_file} missing Check/Takeaway section"
