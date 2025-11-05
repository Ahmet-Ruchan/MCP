"""
MCP Generator - Streamlit Web Interface
A simple and reliable web interface for generating MCP servers.
"""

import streamlit as st
import json
import zipfile
import io
import os
import sys
from typing import Dict, List, Any

# Add parent directory to path to import server module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from server import MCPGenerator

# Page configuration
st.set_page_config(
    page_title="MCP Generator",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .step-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .success-box {
        padding: 1rem;
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        background: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        color: #0c5460;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'config' not in st.session_state:
    st.session_state.config = {}
if 'tools' not in st.session_state:
    st.session_state.tools = []
if 'resources' not in st.session_state:
    st.session_state.resources = []
if 'prompts' not in st.session_state:
    st.session_state.prompts = []

def reset_wizard():
    """Reset wizard to initial state"""
    st.session_state.step = 1
    st.session_state.config = {}
    st.session_state.tools = []
    st.session_state.resources = []
    st.session_state.prompts = []

def next_step():
    """Move to next step"""
    st.session_state.step += 1

def prev_step():
    """Move to previous step"""
    st.session_state.step -= 1

def create_zip(server_code: str, server_name: str) -> bytes:
    """Create a zip file containing the generated server"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Add server.py
        zip_file.writestr(f'{server_name}/server.py', server_code)

        # Add requirements.txt
        requirements = "mcp>=1.0.0\n"
        zip_file.writestr(f'{server_name}/requirements.txt', requirements)

        # Add README.md
        readme = f"""# {server_name}

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python server.py
```

## Configuration

Add to your Claude Desktop config:

```json
{{
  "mcpServers": {{
    "{server_name}": {{
      "command": "python",
      "args": ["/absolute/path/to/{server_name}/server.py"]
    }}
  }}
}}
```
"""
        zip_file.writestr(f'{server_name}/README.md', readme)

    zip_buffer.seek(0)
    return zip_buffer.getvalue()

# Header
st.markdown("""
<div class="main-header">
    <h1>🔧 MCP Generator</h1>
    <p>Create custom MCP servers with a simple wizard</p>
</div>
""", unsafe_allow_html=True)

# Progress indicator
progress = st.session_state.step / 4
st.progress(progress)
st.write(f"**Step {st.session_state.step} of 4**")
st.markdown("---")

# Step 1: Basic Information
if st.session_state.step == 1:
    st.header("📝 Step 1: Basic Information")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            server_name = st.text_input(
                "Server Name",
                value=st.session_state.config.get('name', ''),
                placeholder="my-awesome-server",
                help="Name for your MCP server (lowercase, hyphens allowed)"
            )

        with col2:
            server_type = st.selectbox(
                "Server Type",
                options=["tool", "resource", "full"],
                index=["tool", "resource", "full"].index(st.session_state.config.get('type', 'tool')),
                help="Choose the type of MCP server to generate"
            )

        description = st.text_area(
            "Description",
            value=st.session_state.config.get('description', ''),
            placeholder="Describe what your server does...",
            height=100
        )

    st.markdown("---")

    # Type descriptions
    st.markdown("### 🔍 Server Type Information")

    type_info = {
        "tool": {
            "icon": "🛠️",
            "title": "Tool Server",
            "desc": "Provides executable functions/tools that Claude can call"
        },
        "resource": {
            "icon": "📚",
            "title": "Resource Server",
            "desc": "Provides data/content that Claude can read"
        },
        "full": {
            "icon": "🎯",
            "title": "Full Server",
            "desc": "Includes tools, resources, and prompts"
        }
    }

    info = type_info[server_type]
    st.info(f"{info['icon']} **{info['title']}**: {info['desc']}")

    if st.button("Next →", type="primary", use_container_width=True):
        if server_name and description:
            st.session_state.config = {
                'name': server_name,
                'type': server_type,
                'description': description
            }
            next_step()
            st.rerun()
        else:
            st.error("Please fill in all required fields!")

# Step 2: Configuration
elif st.session_state.step == 2:
    st.header("⚙️ Step 2: Configuration")

    server_type = st.session_state.config['type']

    # Tools configuration
    if server_type in ['tool', 'full']:
        st.subheader("🛠️ Tools")
        st.write("Add the tools your server will provide:")

        # Display existing tools
        for idx, tool in enumerate(st.session_state.tools):
            with st.expander(f"Tool: {tool['name']}", expanded=False):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**Description:** {tool['description']}")
                    st.write(f"**Parameters:** {', '.join(tool['parameters'].keys()) if tool['parameters'] else 'None'}")
                with col2:
                    if st.button("🗑️", key=f"del_tool_{idx}"):
                        st.session_state.tools.pop(idx)
                        st.rerun()

        # Add new tool
        with st.form("add_tool_form"):
            st.write("**Add New Tool**")
            col1, col2 = st.columns(2)
            with col1:
                tool_name = st.text_input("Tool Name", placeholder="calculate")
            with col2:
                tool_desc = st.text_input("Description", placeholder="Performs calculations")

            # Parameters
            st.write("**Parameters** (one per line, format: `name:type:description`)")
            params_text = st.text_area(
                "Parameters",
                placeholder="num1:number:First number\nnum2:number:Second number",
                height=100,
                label_visibility="collapsed"
            )

            if st.form_submit_button("Add Tool"):
                if tool_name and tool_desc:
                    # Parse parameters
                    params = {}
                    if params_text.strip():
                        for line in params_text.strip().split('\n'):
                            if ':' in line:
                                parts = line.split(':')
                                if len(parts) >= 2:
                                    param_name = parts[0].strip()
                                    param_type = parts[1].strip()
                                    param_desc = parts[2].strip() if len(parts) > 2 else ""
                                    params[param_name] = {
                                        'type': param_type,
                                        'description': param_desc
                                    }

                    st.session_state.tools.append({
                        'name': tool_name,
                        'description': tool_desc,
                        'parameters': params
                    })
                    st.rerun()

    # Resources configuration
    if server_type in ['resource', 'full']:
        st.subheader("📚 Resources")
        st.write("Add the resources your server will provide:")

        # Display existing resources
        for idx, resource in enumerate(st.session_state.resources):
            with st.expander(f"Resource: {resource['uri']}", expanded=False):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**Name:** {resource['name']}")
                    st.write(f"**Description:** {resource['description']}")
                    st.write(f"**MIME Type:** {resource['mimeType']}")
                with col2:
                    if st.button("🗑️", key=f"del_resource_{idx}"):
                        st.session_state.resources.pop(idx)
                        st.rerun()

        # Add new resource
        with st.form("add_resource_form"):
            st.write("**Add New Resource**")
            col1, col2 = st.columns(2)
            with col1:
                resource_uri = st.text_input("URI", placeholder="data://mydata")
                resource_name = st.text_input("Name", placeholder="My Data")
            with col2:
                resource_desc = st.text_input("Description", placeholder="Contains important data")
                resource_mime = st.text_input("MIME Type", value="text/plain")

            if st.form_submit_button("Add Resource"):
                if resource_uri and resource_name and resource_desc:
                    st.session_state.resources.append({
                        'uri': resource_uri,
                        'name': resource_name,
                        'description': resource_desc,
                        'mimeType': resource_mime
                    })
                    st.rerun()

    # Prompts configuration
    if server_type == 'full':
        st.subheader("💬 Prompts")
        st.write("Add the prompts your server will provide:")

        # Display existing prompts
        for idx, prompt in enumerate(st.session_state.prompts):
            with st.expander(f"Prompt: {prompt['name']}", expanded=False):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**Description:** {prompt['description']}")
                with col2:
                    if st.button("🗑️", key=f"del_prompt_{idx}"):
                        st.session_state.prompts.pop(idx)
                        st.rerun()

        # Add new prompt
        with st.form("add_prompt_form"):
            st.write("**Add New Prompt**")
            prompt_name = st.text_input("Prompt Name", placeholder="analyze")
            prompt_desc = st.text_input("Description", placeholder="Analyzes data")

            if st.form_submit_button("Add Prompt"):
                if prompt_name and prompt_desc:
                    st.session_state.prompts.append({
                        'name': prompt_name,
                        'description': prompt_desc
                    })
                    st.rerun()

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", use_container_width=True):
            prev_step()
            st.rerun()
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            # Validate based on server type
            valid = True
            if server_type == 'tool' and not st.session_state.tools:
                st.error("Please add at least one tool!")
                valid = False
            elif server_type == 'resource' and not st.session_state.resources:
                st.error("Please add at least one resource!")
                valid = False
            elif server_type == 'full' and (not st.session_state.tools or not st.session_state.resources):
                st.error("Please add at least one tool and one resource!")
                valid = False

            if valid:
                next_step()
                st.rerun()

# Step 3: Review
elif st.session_state.step == 3:
    st.header("👀 Step 3: Review Configuration")

    st.subheader("📋 Basic Information")
    st.write(f"**Name:** {st.session_state.config['name']}")
    st.write(f"**Type:** {st.session_state.config['type']}")
    st.write(f"**Description:** {st.session_state.config['description']}")

    if st.session_state.tools:
        st.subheader("🛠️ Tools")
        for tool in st.session_state.tools:
            with st.expander(f"{tool['name']}", expanded=False):
                st.write(f"**Description:** {tool['description']}")
                if tool['parameters']:
                    st.write("**Parameters:**")
                    for param_name, param_info in tool['parameters'].items():
                        st.write(f"  - `{param_name}` ({param_info['type']}): {param_info['description']}")

    if st.session_state.resources:
        st.subheader("📚 Resources")
        for resource in st.session_state.resources:
            with st.expander(f"{resource['uri']}", expanded=False):
                st.write(f"**Name:** {resource['name']}")
                st.write(f"**Description:** {resource['description']}")
                st.write(f"**MIME Type:** {resource['mimeType']}")

    if st.session_state.prompts:
        st.subheader("💬 Prompts")
        for prompt in st.session_state.prompts:
            with st.expander(f"{prompt['name']}", expanded=False):
                st.write(f"**Description:** {prompt['description']}")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back", use_container_width=True):
            prev_step()
            st.rerun()
    with col2:
        if st.button("Generate Server 🚀", type="primary", use_container_width=True):
            next_step()
            st.rerun()

# Step 4: Generate
elif st.session_state.step == 4:
    st.header("🎉 Step 4: Generate & Download")

    with st.spinner("Generating your MCP server..."):
        try:
            # Prepare configuration
            config = {
                'name': st.session_state.config['name'],
                'description': st.session_state.config['description'],
                'type': st.session_state.config['type']
            }

            if st.session_state.tools:
                config['tools'] = st.session_state.tools
            if st.session_state.resources:
                config['resources'] = st.session_state.resources
            if st.session_state.prompts:
                config['prompts'] = st.session_state.prompts

            # Generate server
            generator = MCPGenerator()
            server_code = generator.generate_from_config(config)

            # Create zip file
            zip_data = create_zip(server_code, st.session_state.config['name'])

            # Success message
            st.success("✅ Server generated successfully!")

            # Preview
            with st.expander("📄 Preview Generated Code", expanded=False):
                st.code(server_code, language="python")

            # Download button
            st.download_button(
                label="⬇️ Download Server (ZIP)",
                data=zip_data,
                file_name=f"{st.session_state.config['name']}.zip",
                mime="application/zip",
                use_container_width=True
            )

            # Installation instructions
            st.markdown("### 📦 Installation Instructions")
            st.info(f"""
1. Extract the downloaded ZIP file
2. Navigate to the `{st.session_state.config['name']}` directory
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `python server.py`
5. Configure Claude Desktop (see README.md in the ZIP)
            """)

            st.markdown("---")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back to Review", use_container_width=True):
                    prev_step()
                    st.rerun()
            with col2:
                if st.button("🔄 Create Another Server", use_container_width=True):
                    reset_wizard()
                    st.rerun()

        except Exception as e:
            st.error(f"❌ Error generating server: {str(e)}")
            if st.button("← Back"):
                prev_step()
                st.rerun()

# Sidebar
with st.sidebar:
    st.header("ℹ️ About MCP Generator")
    st.write("""
    This tool helps you create custom Model Context Protocol (MCP) servers without writing code.

    **Features:**
    - 🛠️ Tool Servers
    - 📚 Resource Servers
    - 🎯 Full-Featured Servers
    - 🎨 Step-by-step wizard
    - 📦 Ready-to-use ZIP output
    """)

    st.markdown("---")
    st.write("**Current Configuration:**")
    if st.session_state.config:
        st.write(f"Name: `{st.session_state.config.get('name', 'N/A')}`")
        st.write(f"Type: `{st.session_state.config.get('type', 'N/A')}`")
    else:
        st.write("Not configured yet")

    st.markdown("---")
    if st.button("🔄 Reset Wizard", use_container_width=True):
        reset_wizard()
        st.rerun()
