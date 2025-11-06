// MCP Generator - AI-Powered Web Interface
// State management
let tools = [];
let resources = [];
let prompts = [];
let generatedFilename = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateServerType();
    updateCounts();
});

// Server type information
const serverTypeInfo = {
    tool: {
        icon: '🛠️',
        title: 'Tool Server',
        desc: 'Provides executable functions that Claude can call to perform actions'
    },
    resource: {
        icon: '📚',
        title: 'Resource Server',
        desc: 'Provides data and content that Claude can read and use'
    },
    full: {
        icon: '🎯',
        title: 'Full-Featured Server',
        desc: 'Combines tools, resources, and prompts for complete functionality'
    }
};

// Update server type UI
function updateServerType() {
    const serverType = document.getElementById('serverType').value;
    const info = serverTypeInfo[serverType];

    // Update info box
    document.getElementById('typeInfo').innerHTML = `
        <p class="text-sm text-gray-700">${info.icon} <strong>${info.title}:</strong> ${info.desc}</p>
    `;

    // Show/hide sections
    const toolSection = document.getElementById('toolSection');
    const resourceSection = document.getElementById('resourceSection');
    const promptSection = document.getElementById('promptSection');

    if (serverType === 'tool') {
        toolSection.classList.remove('hidden');
        resourceSection.classList.add('hidden');
        promptSection.classList.add('hidden');
    } else if (serverType === 'resource') {
        toolSection.classList.add('hidden');
        resourceSection.classList.remove('hidden');
        promptSection.classList.add('hidden');
    } else if (serverType === 'full') {
        toolSection.classList.remove('hidden');
        resourceSection.classList.remove('hidden');
        promptSection.classList.remove('hidden');
    }
}

// Add Tool
function addTool() {
    const name = document.getElementById('toolName').value.trim();
    const desc = document.getElementById('toolDesc').value.trim();
    const paramsText = document.getElementById('toolParams').value.trim();

    if (!name || !desc) {
        showError('Please fill in tool name and description');
        return;
    }

    // Parse parameters
    const parameters = [];
    if (paramsText) {
        paramsText.split('\n').forEach(line => {
            if (line.trim() && line.includes(':')) {
                const parts = line.split(':');
                if (parts.length >= 2) {
                    parameters.push({
                        name: parts[0].trim(),
                        type: parts[1].trim(),
                        description: parts[2] ? parts[2].trim() : '',
                        required: true
                    });
                }
            }
        });
    }

    tools.push({ name, description: desc, parameters });

    // Clear inputs
    document.getElementById('toolName').value = '';
    document.getElementById('toolDesc').value = '';
    document.getElementById('toolParams').value = '';

    renderComponents();
    updateCounts();
    showSuccess(`✅ Added tool: ${name}`);
}

// Add Resource
function addResource() {
    const uri = document.getElementById('resourceUri').value.trim();
    const name = document.getElementById('resourceName').value.trim();
    const desc = document.getElementById('resourceDesc').value.trim();
    const mimeType = document.getElementById('resourceMime').value;

    if (!uri || !name) {
        showError('Please fill in resource URI and name');
        return;
    }

    resources.push({ uri, name, description: desc, mimeType });

    // Clear inputs
    document.getElementById('resourceUri').value = '';
    document.getElementById('resourceName').value = '';
    document.getElementById('resourceDesc').value = '';

    renderComponents();
    updateCounts();
    showSuccess(`✅ Added resource: ${name}`);
}

// Add Prompt
function addPrompt() {
    const name = document.getElementById('promptName').value.trim();
    const desc = document.getElementById('promptDesc').value.trim();

    if (!name || !desc) {
        showError('Please fill in prompt name and description');
        return;
    }

    prompts.push({ name, description: desc });

    // Clear inputs
    document.getElementById('promptName').value = '';
    document.getElementById('promptDesc').value = '';

    renderComponents();
    updateCounts();
    showSuccess(`✅ Added prompt: ${name}`);
}

// Remove components
function removeTool(index) {
    tools.splice(index, 1);
    renderComponents();
    updateCounts();
}

function removeResource(index) {
    resources.splice(index, 1);
    renderComponents();
    updateCounts();
}

function removePrompt(index) {
    prompts.splice(index, 1);
    renderComponents();
    updateCounts();
}

// Render components
function renderComponents() {
    // Render tools
    const toolsList = document.getElementById('toolsList');
    toolsList.innerHTML = tools.map((tool, index) => `
        <div class="component-card bg-white border-2 border-purple-200 rounded-lg p-3 hover:shadow-md">
            <div class="flex justify-between items-start">
                <div class="flex-1">
                    <p class="font-semibold text-purple-700">${tool.name}</p>
                    <p class="text-sm text-gray-600">${tool.description}</p>
                    <p class="text-xs text-gray-500 mt-1">Params: ${tool.parameters.length}</p>
                </div>
                <button onclick="removeTool(${index})" class="text-red-600 hover:text-red-800 font-bold ml-2">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');

    // Render resources
    const resourcesList = document.getElementById('resourcesList');
    resourcesList.innerHTML = resources.map((resource, index) => `
        <div class="component-card bg-white border-2 border-green-200 rounded-lg p-3 hover:shadow-md">
            <div class="flex justify-between items-start">
                <div class="flex-1">
                    <p class="font-semibold text-green-700">${resource.name}</p>
                    <p class="text-sm text-gray-600">${resource.uri}</p>
                    <p class="text-xs text-gray-500 mt-1">${resource.mimeType}</p>
                </div>
                <button onclick="removeResource(${index})" class="text-red-600 hover:text-red-800 font-bold ml-2">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');

    // Render prompts
    const promptsList = document.getElementById('promptsList');
    promptsList.innerHTML = prompts.map((prompt, index) => `
        <div class="component-card bg-white border-2 border-orange-200 rounded-lg p-3 hover:shadow-md">
            <div class="flex justify-between items-start">
                <div class="flex-1">
                    <p class="font-semibold text-orange-700">${prompt.name}</p>
                    <p class="text-sm text-gray-600">${prompt.description}</p>
                </div>
                <button onclick="removePrompt(${index})" class="text-red-600 hover:text-red-800 font-bold ml-2">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');
}

// Update counts
function updateCounts() {
    document.getElementById('toolCount').textContent = tools.length;
    document.getElementById('resourceCount').textContent = resources.length;
    document.getElementById('promptCount').textContent = prompts.length;
}

// Generate with Claude AI
async function generateWithClaude() {
    const apiKey = document.getElementById('apiKey').value.trim();
    const serverName = document.getElementById('serverName').value.trim();
    const serverType = document.getElementById('serverType').value;
    const description = document.getElementById('description').value.trim();

    // Validation
    if (!apiKey) {
        showError('❌ Please enter your Claude API key!');
        return;
    }

    if (!serverName || !description) {
        showError('❌ Please fill in server name and description!');
        return;
    }

    // Validate components based on server type
    if (serverType === 'tool' && tools.length === 0) {
        showError('❌ Please add at least one tool!');
        return;
    }

    if (serverType === 'resource' && resources.length === 0) {
        showError('❌ Please add at least one resource!');
        return;
    }

    if (serverType === 'full' && (tools.length === 0 || resources.length === 0)) {
        showError('❌ Full server needs at least one tool and one resource!');
        return;
    }

    // Show loading
    showLoading('🤖 Claude is generating your MCP server...');

    try {
        const response = await fetch('/api/generate-with-claude', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                api_key: apiKey,
                name: serverName,
                description: description,
                server_type: serverType,
                config: {
                    tools: tools,
                    resources: resources,
                    prompts: prompts
                }
            })
        });

        const data = await response.json();

        if (data.success) {
            generatedFilename = data.filename;

            // Show success
            showSuccess(data.message);

            // Display code
            document.getElementById('generatedCode').textContent = data.code;
            document.getElementById('configJson').textContent = data.config_json;

            // Show preview section
            document.getElementById('codePreview').classList.remove('hidden');

            // Enable download button
            document.getElementById('downloadBtn').disabled = false;

            // Scroll to preview
            document.getElementById('codePreview').scrollIntoView({ behavior: 'smooth' });
        } else {
            showError(data.message || '❌ Failed to generate server');
        }
    } catch (error) {
        showError(`❌ Error: ${error.message}`);
    }
}

// Download ZIP
async function downloadZip() {
    if (!generatedFilename) {
        showError('❌ No file to download');
        return;
    }

    window.location.href = `/api/download/${generatedFilename}`;
    showSuccess('✅ Download started!');
}

// Reset all
function resetAll() {
    if (confirm('Are you sure you want to reset everything?')) {
        tools = [];
        resources = [];
        prompts = [];
        generatedFilename = null;

        // Clear inputs
        document.getElementById('serverName').value = '';
        document.getElementById('description').value = '';
        document.getElementById('serverType').value = 'tool';

        // Hide preview
        document.getElementById('codePreview').classList.add('hidden');
        document.getElementById('downloadBtn').disabled = true;

        // Update UI
        renderComponents();
        updateCounts();
        updateServerType();
        hideStatus();

        showSuccess('✅ Reset complete!');
    }
}

// Tab switching
function showTab(tab) {
    const codeTab = document.getElementById('codeTab');
    const instructionsTab = document.getElementById('instructionsTab');
    const codeContent = document.getElementById('codeContent');
    const instructionsContent = document.getElementById('instructionsContent');

    if (tab === 'code') {
        codeTab.classList.add('tab-active');
        codeTab.classList.remove('bg-gray-200', 'hover:bg-gray-300');
        instructionsTab.classList.remove('tab-active');
        instructionsTab.classList.add('bg-gray-200', 'hover:bg-gray-300');

        codeContent.classList.remove('hidden');
        instructionsContent.classList.add('hidden');
    } else {
        instructionsTab.classList.add('tab-active');
        instructionsTab.classList.remove('bg-gray-200', 'hover:bg-gray-300');
        codeTab.classList.remove('tab-active');
        codeTab.classList.add('bg-gray-200', 'hover:bg-gray-300');

        codeContent.classList.add('hidden');
        instructionsContent.classList.remove('hidden');
    }
}

// Status messages
function showSuccess(message) {
    showStatus(message, 'success');
}

function showError(message) {
    showStatus(message, 'error');
}

function showLoading(message) {
    const statusDiv = document.getElementById('statusMessage');
    statusDiv.className = 'bg-blue-50 border-l-4 border-blue-500 p-4 rounded-lg';
    statusDiv.innerHTML = `
        <div class="flex items-center">
            <svg class="spinner w-5 h-5 mr-3 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <p class="font-semibold text-blue-800">${message}</p>
        </div>
    `;
    statusDiv.classList.remove('hidden');
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('statusMessage');

    if (type === 'success') {
        statusDiv.className = 'bg-green-50 border-l-4 border-green-500 p-4 rounded-lg';
        statusDiv.innerHTML = `<p class="font-semibold text-green-800">${message}</p>`;
    } else if (type === 'error') {
        statusDiv.className = 'bg-red-50 border-l-4 border-red-500 p-4 rounded-lg';
        statusDiv.innerHTML = `<p class="font-semibold text-red-800">${message}</p>`;
    }

    statusDiv.classList.remove('hidden');

    // Auto hide after 5 seconds
    setTimeout(() => {
        statusDiv.classList.add('hidden');
    }, 5000);
}

function hideStatus() {
    document.getElementById('statusMessage').classList.add('hidden');
}
