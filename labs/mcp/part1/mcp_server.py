import json
import sys
from datetime import datetime
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# This MCP server provides calculator tools for LLMs:
# - Implements the server side of the Model Context Protocol
# - Exposes mathematical operations (add, multiply, divide) as tools
# - Communicates via stdio using JSON-RPC 2.0 protocol
# - Includes educational logging to show protocol traffic
# - Demonstrates how external tools can be made available to AI models

# Terminal colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def log_message(msg_type, data):
    """Pretty print messages to stderr for educational purposes"""
    # This logging function makes the JSON-RPC traffic visible to students:
    # - Shows exactly what messages are sent between client and server
    # - Color-codes different message types for easy reading
    # - Helps students understand the MCP protocol in action
    # - Uses stderr so it doesn't interfere with the actual MCP communication on stdout
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    
    print(f"\n{BOLD}{CYAN}[{timestamp}] {msg_type}{RESET}", file=sys.stderr)
    print(f"{YELLOW}{'─'*60}{RESET}", file=sys.stderr)
    
    # Pretty print JSON with color coding based on message direction
    formatted = json.dumps(data, indent=2)
    for line in formatted.split('\n'):
        if '"method"' in line or 'Client → Server' in msg_type:
            print(f"{BLUE}{line}{RESET}", file=sys.stderr)  # Client requests in blue
        elif '"result"' in line or 'Server → Client' in msg_type:
            print(f"{GREEN}{line}{RESET}", file=sys.stderr)  # Server responses in green
        elif '"error"' in line:
            print(f"{MAGENTA}{line}{RESET}", file=sys.stderr)  # Errors in magenta
        else:
            print(f"{line}", file=sys.stderr)  # Other content in default color
    
    print(f"{YELLOW}{'─'*60}{RESET}\n", file=sys.stderr)
    sys.stderr.flush()

# Create server with logging
app = Server("calculator-server")
# This creates an MCP server instance:
# - "calculator-server" is the server name (advertised during initialization)
# - The @app decorators below register handlers for different MCP requests
# - This server will respond to tools/list and tools/call requests

@app.list_tools()
async def list_tools() -> list[Tool]:
    # This function is called when clients request "tools/list":
    # - Returns all available tools that this server provides
    # - Each tool has a name, description, and inputSchema (parameter definitions)
    # - The inputSchema uses JSON Schema to define what parameters are required/allowed
    # - This is how clients discover what operations the server can perform
    log_message("Client → Server: LIST TOOLS REQUEST", {"method": "tools/list"})
    
    tools = [
        Tool(
            name="add",
            description="Add two numbers together",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="multiply",
            description="Multiply two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="divide",
            description="Divide two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "Numerator"},
                    "b": {"type": "number", "description": "Denominator"}
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="power",
            description="Calculate x raised to the power of y (x^y)",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "Base number"},
                    "y": {"type": "number", "description": "Exponent"}
                },
                "required": ["x", "y"]
            }
        )
    ]
    
    log_message("Server → Client: LIST TOOLS RESPONSE", {
        "tools": [{"name": t.name, "description": t.description} for t in tools]
    })
    
    return tools

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    # This function is called when clients request "tools/call":
    # - Executes the actual tool logic based on the tool name
    # - Validates and processes the input arguments
    # - Returns results as TextContent (MCP's standard response format)
    # - Handles errors gracefully (like division by zero)
    # - This is where the server's business logic lives
    log_message("Client → Server: TOOL CALL REQUEST", {
        "tool": name,
        "arguments": arguments
    })
    
    if name == "add":
        result = arguments["a"] + arguments["b"]
        response_text = f"Result: {arguments['a']} + {arguments['b']} = {result}"
    
    elif name == "multiply":
        result = arguments["a"] * arguments["b"]
        response_text = f"Result: {arguments['a']} × {arguments['b']} = {result}"
    
    elif name == "divide":
        if arguments["b"] == 0:
            response_text = "Error: Cannot divide by zero"
        else:
            result = arguments["a"] / arguments["b"]
            response_text = f"Result: {arguments['a']} ÷ {arguments['b']} = {result}"
    
    elif name == "power":
        # Handle edge case: 0^0 = 1 (mathematical convention)
        if arguments["x"] == 0 and arguments["y"] == 0:
            result = 1
        else:
            result = arguments["x"] ** arguments["y"]
        response_text = f"Result: {arguments['x']} ^ {arguments['y']} = {result}"
    
    else:
        raise ValueError(f"Unknown tool: {name}")
    
    response = [TextContent(type="text", text=response_text)]
    
    log_message("Server → Client: TOOL CALL RESPONSE", {"result": response_text})
    
    return response

async def main():
    # This is the server's main entry point:
    # - Sets up stdio-based communication (stdin/stdout with the client)
    # - Starts the MCP server event loop
    # - Handles incoming JSON-RPC requests from clients
    # - Routes requests to the appropriate handler (@app.list_tools, @app.call_tool)
    print(f"\n{BOLD}{GREEN}🚀 Calculator MCP Server Starting...{RESET}", file=sys.stderr)
    print(f"{CYAN}Watch the JSON-RPC traffic below:{RESET}\n", file=sys.stderr)
    sys.stderr.flush()
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
