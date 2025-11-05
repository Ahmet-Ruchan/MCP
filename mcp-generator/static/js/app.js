// Global state
let currentStep = 1;
let serverConfig = {
    name: '',
    description: '',
    server_type: '',
    config: {
        tools: [],
        resources: [],
        prompts: []
    }
};
let generatedFilename = '';

// Server type selection
function selectServerType(type) {
    serverConfig.server_type = type;
    document.getElementById('serverType').value = type;

    // Update visual selection
    document.querySelectorAll('.server-type-card').forEach(card => {
        card.classList.remove('border-purple-500', 'bg-purple-50');
        card.classList.add('border-gray-300');
    });

    event.target.closest('.server-type-card').classList.add('border-purple-500', 'bg-purple-50');
    event.target.closest('.server-type-card').classList.remove('border-gray-300');
}

// Step navigation
function nextStep(step) {
    // Validate current step
    if (!validateStep(currentStep)) {
        return;
    }

    // Save current step data
    saveStepData(currentStep);

    // Hide current step
    document.getElementById(`step${currentStep}`).classList.add('hidden');

    // Show next step
    document.getElementById(`step${step}`).classList.remove('hidden');
    document.getElementById(`step${step}`).classList.add('slide-in');

    // Update progress indicators
    document.getElementById(`step${currentStep}-indicator`).classList.remove('active');
    document.getElementById(`step${currentStep}-indicator`).classList.add('completed');
    document.getElementById(`step${step}-indicator`).classList.add('active');

    // Load step content
    if (step === 2) {
        loadConfigForm();
    } else if (step === 3) {
        loadReview();
    }

    currentStep = step;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function previousStep(step) {
    // Hide current step
    document.getElementById(`step${currentStep}`).classList.add('hidden');

    // Show previous step
    document.getElementById(`step${step}`).classList.remove('hidden');

    // Update progress indicators
    document.getElementById(`step${currentStep}-indicator`).classList.remove('active');
    document.getElementById(`step${step}-indicator`).classList.remove('completed');
    document.getElementById(`step${step}-indicator`).classList.add('active');

    currentStep = step;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Validation
function validateStep(step) {
    if (step === 1) {
        const name = document.getElementById('serverName').value.trim();
        const description = document.getElementById('serverDescription').value.trim();
        const type = document.getElementById('serverType').value;

        if (!name) {
            alert('⚠️ Please enter a server name');
            return false;
        }

        if (!/^[a-z0-9-]+$/.test(name)) {
            alert('⚠️ Server name must be lowercase with hyphens only (e.g., my-server)');
            return false;
        }

        if (!description) {
            alert('⚠️ Please enter a description');
            return false;
        }

        if (!type) {
            alert('⚠️ Please select a server type');
            return false;
        }

        return true;
    }

    if (step === 2) {
        const type = serverConfig.server_type;

        if (type === 'tool' || type === 'full') {
            if (serverConfig.config.tools.length === 0) {
                alert('⚠️ Please add at least one tool');
                return false;
            }
        }

        if (type === 'resource' || type === 'full') {
            if (serverConfig.config.resources.length === 0) {
                alert('⚠️ Please add at least one resource');
                return false;
            }
        }

        return true;
    }

    return true;
}

// Save step data
function saveStepData(step) {
    if (step === 1) {
        serverConfig.name = document.getElementById('serverName').value.trim();
        serverConfig.description = document.getElementById('serverDescription').value.trim();
        serverConfig.server_type = document.getElementById('serverType').value;
    }
}

// Load configuration form based on server type
function loadConfigForm() {
    const type = serverConfig.server_type;
    const container = document.getElementById('configContent');

    let html = '';

    if (type === 'tool' || type === 'full') {
        html += generateToolsSection();
    }

    if (type === 'resource' || type === 'full') {
        html += generateResourcesSection();
    }

    if (type === 'full') {
        html += generatePromptsSection();
    }

    container.innerHTML = html;
}

// Generate Tools Section
function generateToolsSection() {
    return `
        <div class="border-2 border-purple-200 rounded-lg p-6 bg-purple-50">
            <h3 class="text-xl font-bold mb-4 text-purple-800">
                <i class="fas fa-tools mr-2"></i>Tools Configuration
            </h3>
            <p class="text-sm text-gray-600 mb-4">Tools are functions that your MCP server can execute.</p>

            <div id="toolsList" class="space-y-4 mb-4">
                ${serverConfig.config.tools.map((tool, index) => renderTool(tool, index)).join('')}
            </div>

            <button onclick="addTool()" class="bg-purple-500 text-white px-4 py-2 rounded-lg hover:bg-purple-600 transition">
                <i class="fas fa-plus mr-2"></i>Add Tool
            </button>
        </div>
    `;
}

// Generate Resources Section
function generateResourcesSection() {
    return `
        <div class="border-2 border-green-200 rounded-lg p-6 bg-green-50 mt-6">
            <h3 class="text-xl font-bold mb-4 text-green-800">
                <i class="fas fa-database mr-2"></i>Resources Configuration
            </h3>
            <p class="text-sm text-gray-600 mb-4">Resources are data sources your MCP server can provide.</p>

            <div id="resourcesList" class="space-y-4 mb-4">
                ${serverConfig.config.resources.map((resource, index) => renderResource(resource, index)).join('')}
            </div>

            <button onclick="addResource()" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">
                <i class="fas fa-plus mr-2"></i>Add Resource
            </button>
        </div>
    `;
}

// Generate Prompts Section
function generatePromptsSection() {
    return `
        <div class="border-2 border-blue-200 rounded-lg p-6 bg-blue-50 mt-6">
            <h3 class="text-xl font-bold mb-4 text-blue-800">
                <i class="fas fa-comment-dots mr-2"></i>Prompts Configuration
            </h3>
            <p class="text-sm text-gray-600 mb-4">Prompts are pre-defined templates for AI interactions.</p>

            <div id="promptsList" class="space-y-4 mb-4">
                ${serverConfig.config.prompts.map((prompt, index) => renderPrompt(prompt, index)).join('')}
            </div>

            <button onclick="addPrompt()" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
                <i class="fas fa-plus mr-2"></i>Add Prompt
            </button>
        </div>
    `;
}

// Render Tool
function renderTool(tool, index) {
    return `
        <div class="bg-white p-4 rounded-lg shadow border-l-4 border-purple-500">
            <div class="flex justify-between items-start mb-3">
                <h4 class="font-bold text-lg">${tool.name || 'New Tool'}</h4>
                <button onclick="removeTool(${index})" class="text-red-500 hover:text-red-700">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <p class="text-sm text-gray-600 mb-2">${tool.description || 'No description'}</p>
            <p class="text-xs text-gray-500">${tool.parameters.length} parameter(s)</p>
        </div>
    `;
}

// Render Resource
function renderResource(resource, index) {
    return `
        <div class="bg-white p-4 rounded-lg shadow border-l-4 border-green-500">
            <div class="flex justify-between items-start mb-3">
                <h4 class="font-bold text-lg">${resource.name || 'New Resource'}</h4>
                <button onclick="removeResource(${index})" class="text-red-500 hover:text-red-700">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <p class="text-sm text-gray-600 mb-2">${resource.uri || 'No URI'}</p>
            <p class="text-xs text-gray-500">${resource.description || 'No description'}</p>
        </div>
    `;
}

// Render Prompt
function renderPrompt(prompt, index) {
    return `
        <div class="bg-white p-4 rounded-lg shadow border-l-4 border-blue-500">
            <div class="flex justify-between items-start mb-3">
                <h4 class="font-bold text-lg">${prompt.name || 'New Prompt'}</h4>
                <button onclick="removePrompt(${index})" class="text-red-500 hover:text-red-700">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <p class="text-sm text-gray-600">${prompt.description || 'No description'}</p>
        </div>
    `;
}

// Add Tool
function addTool() {
    const name = prompt('Enter tool name (e.g., calculate, search):');
    if (!name) return;

    const description = prompt('Enter tool description:');
    if (!description) return;

    const tool = {
        name: name,
        description: description,
        parameters: []
    };

    // Add parameters
    while (true) {
        const addParam = confirm('Add a parameter?');
        if (!addParam) break;

        const paramName = prompt('Parameter name:');
        if (!paramName) break;

        const paramType = prompt('Parameter type (string, number, boolean, object, array):', 'string');
        const paramDesc = prompt('Parameter description:');
        const paramRequired = confirm('Is this parameter required?');

        tool.parameters.push({
            name: paramName,
            type: paramType || 'string',
            description: paramDesc || '',
            required: paramRequired
        });
    }

    serverConfig.config.tools.push(tool);
    loadConfigForm();
}

// Remove Tool
function removeTool(index) {
    if (confirm('Are you sure you want to remove this tool?')) {
        serverConfig.config.tools.splice(index, 1);
        loadConfigForm();
    }
}

// Add Resource
function addResource() {
    const uri = prompt('Enter resource URI (e.g., data://users, file://docs):');
    if (!uri) return;

    const name = prompt('Enter resource name:');
    if (!name) return;

    const description = prompt('Enter resource description:');
    const type = prompt('Resource type (text or json):', 'json');

    serverConfig.config.resources.push({
        uri: uri,
        name: name,
        description: description || '',
        type: type || 'json'
    });

    loadConfigForm();
}

// Remove Resource
function removeResource(index) {
    if (confirm('Are you sure you want to remove this resource?')) {
        serverConfig.config.resources.splice(index, 1);
        loadConfigForm();
    }
}

// Add Prompt
function addPrompt() {
    const name = prompt('Enter prompt name:');
    if (!name) return;

    const description = prompt('Enter prompt description:');
    if (!description) return;

    serverConfig.config.prompts.push({
        name: name,
        description: description
    });

    loadConfigForm();
}

// Remove Prompt
function removePrompt(index) {
    if (confirm('Are you sure you want to remove this prompt?')) {
        serverConfig.config.prompts.splice(index, 1);
        loadConfigForm();
    }
}

// Load Review
function loadReview() {
    const container = document.getElementById('reviewContent');

    let html = `
        <h3 class="text-xl font-bold mb-4">📋 Configuration Summary</h3>

        <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700">Server Name:</p>
                <p class="text-lg">${serverConfig.name}</p>
            </div>

            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700">Description:</p>
                <p class="text-lg">${serverConfig.description}</p>
            </div>

            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700">Server Type:</p>
                <p class="text-lg capitalize">${serverConfig.server_type}</p>
            </div>
    `;

    if (serverConfig.config.tools.length > 0) {
        html += `
            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700 mb-2">Tools (${serverConfig.config.tools.length}):</p>
                <ul class="list-disc list-inside space-y-1">
                    ${serverConfig.config.tools.map(t => `<li>${t.name} - ${t.description}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    if (serverConfig.config.resources.length > 0) {
        html += `
            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700 mb-2">Resources (${serverConfig.config.resources.length}):</p>
                <ul class="list-disc list-inside space-y-1">
                    ${serverConfig.config.resources.map(r => `<li>${r.name} (${r.uri})</li>`).join('')}
                </ul>
            </div>
        `;
    }

    if (serverConfig.config.prompts.length > 0) {
        html += `
            <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-700 mb-2">Prompts (${serverConfig.config.prompts.length}):</p>
                <ul class="list-disc list-inside space-y-1">
                    ${serverConfig.config.prompts.map(p => `<li>${p.name} - ${p.description}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    html += `
        </div>

        <div class="mt-6 p-4 bg-blue-50 border-l-4 border-blue-500 rounded">
            <p class="text-sm text-blue-800">
                <i class="fas fa-info-circle mr-2"></i>
                Review your configuration carefully. You can go back to make changes or continue to generate your server.
            </p>
        </div>
    `;

    container.innerHTML = html;
}

// Generate Server
async function generateServer() {
    const btn = document.getElementById('generateBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Generating...';

    try {
        const response = await fetch('/api/generate-and-prepare', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(serverConfig)
        });

        const result = await response.json();

        if (result.success) {
            generatedFilename = result.filename;

            document.getElementById('generateContent').classList.add('hidden');
            document.getElementById('successContent').classList.remove('hidden');
            document.getElementById('successMessage').textContent = result.message;
            document.getElementById('backBtn').classList.add('hidden');
        } else {
            alert('❌ ' + result.message);
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-magic mr-2"></i>Generate Server';
        }
    } catch (error) {
        alert('❌ Error: ' + error.message);
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-magic mr-2"></i>Generate Server';
    }
}

// Download Server
function downloadServer() {
    window.location.href = `/api/download/${generatedFilename}`;
}

// Reset Wizard
function resetWizard() {
    // Reset state
    currentStep = 1;
    serverConfig = {
        name: '',
        description: '',
        server_type: '',
        config: {
            tools: [],
            resources: [],
            prompts: []
        }
    };
    generatedFilename = '';

    // Reset UI
    document.getElementById('serverName').value = '';
    document.getElementById('serverDescription').value = '';
    document.getElementById('serverType').value = '';

    document.querySelectorAll('.server-type-card').forEach(card => {
        card.classList.remove('border-purple-500', 'bg-purple-50');
        card.classList.add('border-gray-300');
    });

    // Hide all steps except first
    for (let i = 2; i <= 4; i++) {
        document.getElementById(`step${i}`).classList.add('hidden');
    }
    document.getElementById('step1').classList.remove('hidden');

    // Reset step indicators
    for (let i = 1; i <= 4; i++) {
        document.getElementById(`step${i}-indicator`).classList.remove('active', 'completed');
        document.getElementById(`step${i}-indicator`).classList.add('bg-gray-300');
    }
    document.getElementById('step1-indicator').classList.add('active');
    document.getElementById('step1-indicator').classList.remove('bg-gray-300');

    // Reset step 4 content
    document.getElementById('generateContent').classList.remove('hidden');
    document.getElementById('successContent').classList.add('hidden');
    document.getElementById('backBtn').classList.remove('hidden');
    document.getElementById('generateBtn').disabled = false;
    document.getElementById('generateBtn').innerHTML = '<i class="fas fa-magic mr-2"></i>Generate Server';

    window.scrollTo({ top: 0, behavior: 'smooth' });
}
