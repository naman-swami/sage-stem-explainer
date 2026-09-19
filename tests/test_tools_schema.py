import os
import pytest
import glob

@pytest.mark.schema
def test_tool_schemas(project_root, load_yaml):
    tools_dir = os.path.join(project_root, 'tools')
    if not os.path.exists(tools_dir):
        pytest.skip("No tools directory found.")
        
    tool_files = glob.glob(os.path.join(tools_dir, '**', '*.yaml'), recursive=True)
    
    for tool_file in tool_files:
        data = load_yaml(tool_file)
        
        # Check basic fields
        assert 'name' in data, f"Tool {tool_file} missing name"
        assert 'description' in data, f"Tool {tool_file} missing description"
        assert 'input_schema' in data, f"Tool {tool_file} missing input_schema"
        assert 'output_schema' in data, f"Tool {tool_file} missing output_schema"
        
        # Check input schema structure
        input_schema = data['input_schema']
        assert input_schema.get('type') == 'object', f"Tool {tool_file} input_schema type must be object"
        assert 'properties' in input_schema, f"Tool {tool_file} input_schema missing properties"
        
        # Check required fields are in properties
        if 'required' in input_schema:
            for req in input_schema['required']:
                assert req in input_schema['properties'], f"Tool {tool_file} required field '{req}' not in properties"
