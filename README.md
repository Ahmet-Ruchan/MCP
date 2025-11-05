# 🚀 MCP Servers Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue)](https://modelcontextprotocol.io)
[![GitHub](https://img.shields.io/badge/GitHub-Integration-green)](https://github.com/Ahmet-Ruchan/MCP)

A curated collection of **Model Context Protocol (MCP)** servers for seamless integration with AI development tools like Cursor, enabling powerful context-aware coding experiences.

## 📖 Table of Contents

- [What is MCP?](#what-is-mcp)
- [Features](#features)
- [Available MCP Servers](#available-mcp-servers)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🤔 What is MCP?

**Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). It enables AI assistants to securely access external tools, APIs, and data sources in a controlled manner.

### Key Benefits:

- 🔌 **Universal Integration**: Connect AI models to any data source or tool
- 🔒 **Secure Access**: Fine-grained permission control for external resources
- ⚡ **Real-time Data**: Access up-to-date information from APIs and databases
- 🛠️ **Extensible**: Build custom servers for your specific needs
- 🌐 **Cross-platform**: Works with multiple AI development environments

## ✨ Features

- **GitHub Integration**: Full GitHub API access through MCP
- **Easy Configuration**: Simple JSON-based setup
- **Token Management**: Secure credential handling
- **Multi-server Support**: Run multiple MCP servers simultaneously
- **Real-time Updates**: Live data access from external sources
- **Error Handling**: Robust error reporting and debugging

## 🛠️ Available MCP Servers

This repository includes configurations and examples for the following MCP servers:

### 1. GitHub MCP Server

Connect your AI assistant directly to GitHub for repository management, issue tracking, and code collaboration.

**Capabilities:**
- 📦 Create, update, and manage repositories
- 🔍 Search code, issues, and users
- 📝 Create and manage issues and pull requests
- 🌿 Branch management and file operations
- 👥 Repository collaboration features
- 📊 Access repository statistics and insights

**Package:** `@modelcontextprotocol/server-github`

### Coming Soon:
- **Filesystem MCP Server** - Local file system access
- **Database MCP Server** - SQL database integration
- **API MCP Server** - Custom REST API connections
- **Cloud Storage MCP Server** - S3, GCS, Azure Blob integration

## 📦 Installation

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- An AI development tool that supports MCP (e.g., Cursor)
- GitHub Personal Access Token (for GitHub MCP server)

### Setup Steps

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Ahmet-Ruchan/MCP.git
   cd MCP
   ```

2. **Get your GitHub Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate new token with required scopes: `repo`, `read:user`, `user:email`
   - Copy the token for configuration

3. **Configure MCP in Cursor:**
   
   Edit or create `~/.cursor/mcp.json`:
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": [
           "-y",
           "@modelcontextprotocol/server-github"
         ],
         "env": {
           "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token_here"
         }
       }
     }
   }
   ```

4. **Clear npx cache (if needed):**
   ```bash
   rm -rf ~/.npm/_npx
   ```

5. **Restart Cursor**

## ⚙️ Configuration

### GitHub MCP Server Configuration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**Important Notes:**
- ⚠️ Never commit your actual token to version control
- ⚠️ Remove `<` and `>` brackets from token - use raw token value only
- ⚠️ Ensure token has appropriate permissions for intended operations

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GITHUB_PERSONAL_ACCESS_TOKEN` | GitHub PAT for API access | Yes |

## 🎯 Usage Examples

### Example 1: Create a Repository

```javascript
// Using MCP in Cursor, you can ask:
"Create a new GitHub repository called 'my-awesome-project' with a description"
```

### Example 2: Search Repositories

```javascript
// Find repositories:
"Search for my repositories related to machine learning"
```

### Example 3: Manage Issues

```javascript
// Create and manage issues:
"Create an issue in my repository about adding authentication"
```

### Example 4: Push Files

```javascript
// Push files to repository:
"Push these files to my GitHub repository"
```

## 🐛 Troubleshooting

### Common Issues

**1. "ERR_MODULE_NOT_FOUND" Error**
```bash
# Solution: Clear npx cache
rm -rf ~/.npm/_npx
```

**2. "Bad credentials" Error**
- Check if token is correct and properly formatted (no `<>` brackets)
- Verify token has required permissions
- Regenerate token if expired

**3. "No server info found" Error**
- Restart Cursor completely
- Check `mcp.json` syntax
- Verify command and args are correct

**4. Package Deprecated Warning**
```
npm warn deprecated @modelcontextprotocol/server-github
```
- This is expected - the package works but may have newer alternatives
- Continue using unless critical issues arise

### Debug Mode

To see detailed MCP logs in Cursor:
1. Open Cursor logs: `Help → Show Logs`
2. Look for MCP-related entries
3. Check for connection and authentication issues

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new MCP server integrations
- 📝 Improve documentation
- 🔧 Submit pull requests

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor Documentation](https://cursor.sh/docs)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [MCP GitHub Server Repository](https://github.com/modelcontextprotocol/servers)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for developing the MCP protocol
- [Cursor](https://cursor.sh/) for MCP integration support
- The open-source community for MCP server implementations

## 📞 Contact

**Ahmet Ruçhan Avcı**

- GitHub: [@Ahmet-Ruchan](https://github.com/Ahmet-Ruchan)
- Email: aruchanavci01@gmail.com

---

⭐ If you find this repository helpful, please consider giving it a star!

**Made with ❤️ using MCP**
