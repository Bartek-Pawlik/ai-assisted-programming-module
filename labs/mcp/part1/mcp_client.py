import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # This MCP client demonstrates the complete client-server interaction:
    # 1. Spawns the MCP server with calculator functionality as a subprocess
    # 2. Performs MCP protocol handshake (initialize)
    # 3. Discovers available tools (list_tools)
    # 4. Executes tools with parameters (call_tool)
    # 5. Handles both successful operations and errors
    print("🧮 Calculator MCP Server Demo")
    print("=" * 50)
    
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize
            print("\n1️⃣  Initializing connection...")
            # The initialize() method performs the MCP handshake:
            # 1. Client sends initialization request to server
            # 2. Server responds with its capabilities (what it can do)
            # 3. Server info (name, version) and supported features are exchanged
            # 4. This establishes the MCP session and protocol version
            await session.initialize()
            print("   ✅ Connected to server")
            
            # List tools
            print("\n2️⃣  Listing available tools...")
            # The list_tools() method queries the server for all available tools:
            # - Server returns tool definitions with names, descriptions, and input schemas
            # - Client learns what operations the server can perform
            # - This is like asking "What can you do?" after the handshake
            tools = await session.list_tools()
            print("   Available tools:")
            for tool in tools.tools:
                print(f"      • {tool.name}: {tool.description}")
            
            # Test Addition
            print("\n3️⃣  Testing: 15 + 7")
            # The call_tool() method executes a specific tool on the server:
            # - Sends tool name and parameters to server
            # - Server validates inputs, executes the tool, and returns results
            # - This demonstrates the complete request-response cycle
            result = await session.call_tool("add", {"a": 15, "b": 7})
            print(f"   📊 {result.content[0].text}")
            
            # Test Multiplication
            print("\n4️⃣  Testing: 8 × 6")
            result = await session.call_tool("multiply", {"a": 8, "b": 6})
            print(f"   📊 {result.content[0].text}")
            
            # Test Division
            print("\n5️⃣  Testing: 100 ÷ 4")
            result = await session.call_tool("divide", {"a": 100, "b": 4})
            print(f"   📊 {result.content[0].text}")
            
            # Test Division by Zero
            print("\n6️⃣  Testing: 10 ÷ 0 (error handling)")
            # This tests how the server handles invalid inputs:
            # - Server should validate parameters and handle edge cases
            # - Demonstrates proper error handling in MCP tools
            # - Shows that tools can return error messages, not just results
            result = await session.call_tool("divide", {"a": 10, "b": 0})
            print(f"   📊 {result.content[0].text}")
            
            # Test Power Function
            print("\n7️⃣  Testing: 2 ^ 8 (power function)")
            # Test the new power tool that calculates x^y
            # Should return 256 (2^8 = 256)
            result = await session.call_tool("power", {"x": 2, "y": 8})
            print(f"   📊 {result.content[0].text}")
            
            # Test Power Edge Case
            print("\n8️⃣  Testing: 0 ^ 0 (edge case)")
            # Test edge case: 0^0 should return 1 (mathematical convention)
            result = await session.call_tool("power", {"x": 0, "y": 0})
            print(f"   📊 {result.content[0].text}")
            
            print("\n" + "=" * 50)
            print("✅ Demo complete!")
            print("\nCheck the colored output above to see the JSON-RPC traffic.")
            print("=" * 50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
