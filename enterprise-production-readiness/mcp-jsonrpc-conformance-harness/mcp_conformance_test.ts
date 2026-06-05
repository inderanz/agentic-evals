import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import fs from "fs";

const command = process.env.MCP_COMMAND || "node";
const args = (process.env.MCP_ARGS || "dist/server.js").split(" ");

async function main() {
  const transcript: any[] = [];
  const transport = new StdioClientTransport({ command, args });
  const client = new Client({ name: "enterprise-mcp-evaluator", version: "1.0.0" }, { capabilities: {} });
  await client.connect(transport);

  const tools = await client.listTools();
  transcript.push({ step: "tools/list", response: tools });

  if (!tools.tools || tools.tools.length === 0) throw new Error("No tools exposed");
  for (const tool of tools.tools) {
    if (!tool.name) throw new Error("Tool missing name");
    if (!tool.inputSchema) throw new Error(`Tool ${tool.name} missing inputSchema`);
  }

  try {
    await client.callTool({ name: tools.tools[0].name, arguments: {} });
  } catch (err: any) {
    transcript.push({ step: "tools/call-invalid", error: String(err.message || err) });
  }

  fs.writeFileSync("mcp-transcript.json", JSON.stringify(transcript, null, 2));
  await client.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
