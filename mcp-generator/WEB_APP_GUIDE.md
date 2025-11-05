# 🌐 MCP Generator Web Application Guide

A beautiful, user-friendly web interface for generating MCP servers without writing code!

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd mcp-generator
pip install -r web_requirements.txt
```

### 2. Start the Web Server

```bash
python web_app.py
```

You should see:
```
🚀 Starting MCP Generator Web UI...
📍 Open your browser at: http://localhost:5000
🛑 Press Ctrl+C to stop
```

### 3. Open Your Browser

Navigate to: **http://localhost:5000**

## 📖 How to Use

### Step 1: Basic Information

Fill in the basic details about your MCP server:

1. **Server Name** (required)
   - Use lowercase with hyphens
   - Example: `weather-api`, `calculator-tool`, `database-server`
   - Must match pattern: `^[a-z0-9-]+$`

2. **Description** (required)
   - Describe what your server does
   - Example: "A weather API MCP server that provides current weather and forecasts"

3. **Server Type** (required)
   - **Tool Server**: For APIs, calculations, and functions
   - **Resource Server**: For data access and resources
   - **Full Server**: Complete server with tools, resources, and prompts

Click **"Next Step"** to continue.

### Step 2: Configuration

Based on your selected server type, you'll configure different components:

#### For Tool Servers:

Click **"Add Tool"** and provide:
- **Tool Name**: Function name (e.g., `get_weather`, `calculate`)
- **Tool Description**: What the tool does
- **Parameters**: Add input parameters for the tool
  - Parameter name
  - Parameter type (string, number, boolean, object, array)
  - Parameter description
  - Is required? (yes/no)

**Example Tool:**
```
Name: get_current_weather
Description: Get current weather for a city
Parameters:
  - city (string, required): City name
  - units (string, optional): Temperature units (metric/imperial)
```

#### For Resource Servers:

Click **"Add Resource"** and provide:
- **Resource URI**: Unique identifier (e.g., `data://users`, `file://docs`)
- **Resource Name**: Display name
- **Resource Description**: What data this provides
- **Resource Type**: `json` or `text`

**Example Resource:**
```
URI: weather://current
Name: Current Weather Data
Description: Real-time weather information
Type: json
```

#### For Full Servers:

Configure **Tools**, **Resources**, AND **Prompts**:

Click **"Add Prompt"** and provide:
- **Prompt Name**: Template name
- **Prompt Description**: What this prompt does

**Example Prompt:**
```
Name: summarize_weather
Description: Create a weather summary for the user
```

Click **"Next Step"** when done.

### Step 3: Review Configuration

Review all your settings:
- ✅ Check server name
- ✅ Verify description
- ✅ Review all tools/resources/prompts
- ✅ Make sure everything looks correct

**Need to change something?**
Click **"Previous"** to go back and edit.

**Everything looks good?**
Click **"Continue"** to proceed.

### Step 4: Generate!

1. Review the final summary
2. Click **"Generate Server"**
3. Wait for the generation to complete (usually < 5 seconds)
4. Click **"Download Server Files"** to get your ZIP file

The ZIP contains:
- `server.py` - Your MCP server code
- `README.md` - Documentation
- `requirements.txt` - Python dependencies

### Step 5: Use Your Server

1. **Extract the ZIP file**
   ```bash
   unzip your-server-name.zip
   cd your-server-name
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test your server**
   ```bash
   python server.py
   ```

4. **Configure in your AI tool**

   Add to `~/.cursor/mcp.json` or `~/.config/claude-code/mcp.json`:
   ```json
   {
     "mcpServers": {
       "your-server-name": {
         "command": "python",
         "args": ["/absolute/path/to/your-server-name/server.py"]
       }
     }
   }
   ```

5. **Restart your AI tool**

6. **Start using your server!**

## 🎨 Web Interface Features

### Modern Design
- Beautiful gradient backgrounds
- Smooth animations and transitions
- Responsive design (works on mobile!)
- Intuitive step-by-step wizard

### User-Friendly
- Clear progress indicators
- Helpful tooltips and hints
- Real-time validation
- Error messages when needed

### Quick Actions
- Add/remove components easily
- Edit configurations on the fly
- Download generated files instantly
- Create multiple servers quickly

## 🔧 Configuration Examples

### Example 1: Calculator Server

**Step 1:**
- Name: `calculator-server`
- Description: `A simple calculator with math operations`
- Type: `Tool Server`

**Step 2 - Tools:**
1. Tool: `add`
   - Description: "Add two numbers"
   - Parameters:
     - a (number, required): "First number"
     - b (number, required): "Second number"

2. Tool: `multiply`
   - Description: "Multiply two numbers"
   - Parameters:
     - a (number, required): "First number"
     - b (number, required): "Second number"

### Example 2: Database Resource Server

**Step 1:**
- Name: `database-server`
- Description: `Access database tables as resources`
- Type: `Resource Server`

**Step 2 - Resources:**
1. Resource:
   - URI: `db://users`
   - Name: "User Database"
   - Description: "User records and profiles"
   - Type: `json`

2. Resource:
   - URI: `db://products`
   - Name: "Product Catalog"
   - Description: "Product inventory"
   - Type: `json`

### Example 3: Full E-commerce Server

**Step 1:**
- Name: `ecommerce-server`
- Description: `Complete e-commerce backend`
- Type: `Full Server`

**Step 2:**

**Tools:**
1. `search_products`
   - Parameters: query (string, required), category (string, optional)

2. `add_to_cart`
   - Parameters: product_id (string, required), quantity (number, required)

**Resources:**
1. `shop://products` - "Product Catalog"
2. `shop://cart` - "Shopping Cart"

**Prompts:**
1. `recommend_products` - "Generate product recommendations"

## 🐛 Troubleshooting

### Port Already in Use

If port 5000 is already in use:

```bash
# Find and kill the process
lsof -i :5000
kill -9 <PID>

# Or use a different port
python web_app.py --port 8080
```

### Module Not Found Errors

```bash
# Reinstall dependencies
pip install -r web_requirements.txt

# Or install individually
pip install fastapi uvicorn jinja2 python-multipart
```

### Cannot Connect to Server

1. Check if the server is running
2. Try accessing `http://127.0.0.1:5000` instead
3. Check firewall settings
4. Restart the web server

### Browser Shows Blank Page

1. Check browser console for errors (F12)
2. Try clearing browser cache
3. Try a different browser
4. Check that static files are loading

### Generation Fails

1. Verify all required fields are filled
2. Check that tool/resource names are valid
3. Ensure at least one component is added
4. Try with a simpler configuration first

## 🎯 Tips & Best Practices

### Naming Conventions

- **Server names**: Use kebab-case (e.g., `my-server-name`)
- **Tool names**: Use snake_case (e.g., `get_user_data`)
- **Resource URIs**: Use format `scheme://resource` (e.g., `data://users`)
- **Parameter names**: Use snake_case (e.g., `user_id`)

### Organization

- Group related tools together
- Use clear, descriptive names
- Write helpful descriptions
- Mark required parameters correctly

### Testing

- Start with simple configurations
- Test locally before deploying
- Validate generated code
- Add error handling in generated servers

### Performance

- Keep tools focused and simple
- Don't add too many components
- Use appropriate parameter types
- Consider rate limiting for APIs

## 📊 Web App Architecture

```
mcp-generator/
├── web_app.py              # FastAPI backend
├── templates/
│   └── index.html          # Main UI
├── static/
│   └── js/
│       └── app.js          # Frontend logic
└── web_requirements.txt    # Dependencies
```

### API Endpoints

- `GET /` - Main page
- `GET /api/examples/{type}` - Get example configs
- `POST /api/validate` - Validate configuration
- `POST /api/generate-and-prepare` - Generate server
- `GET /api/download/{filename}` - Download files
- `GET /health` - Health check

## 🔒 Security Notes

- The web app runs locally by default
- No data is sent to external servers
- Generated files are temporary
- Use firewall if exposing to network

## 🚀 Advanced Usage

### Running on Custom Port

```python
# Edit web_app.py, change last line:
uvicorn.run(app, host="0.0.0.0", port=8080)
```

### Running in Production

```bash
# Use gunicorn for production
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker web_app:app
```

### Adding Custom Templates

Edit `web_app.py` and add custom example configurations in the `get_example` function.

## 💡 Feature Ideas

Future enhancements:
- [ ] Save/load configurations
- [ ] Template library
- [ ] Code preview before generation
- [ ] Batch server generation
- [ ] Export/import configs as JSON
- [ ] User accounts and history
- [ ] Cloud deployment options

## 🆘 Support

Need help?
- 📧 Email: aruchanavci01@gmail.com
- 🐛 Issues: https://github.com/Ahmet-Ruchan/MCP/issues
- 📖 Docs: Check DETAILED_README.md

## 📄 License

MIT License - See LICENSE file

---

**Happy Generating! 🎉**

Made with ❤️ by Ahmet Ruçhan Avcı
