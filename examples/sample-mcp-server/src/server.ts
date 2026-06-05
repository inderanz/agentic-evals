import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "payment-investigation-mcp",
  version: "1.0.0"
});

server.tool("search_payment", { paymentId: z.string().min(3) }, async ({ paymentId }) => ({
  content: [{ type: "text", text: JSON.stringify({ paymentId, status: "PENDING", source: "mock-for-eval" }) }]
}));

server.tool("replay_payment", { paymentId: z.string().min(3), approvalId: z.string().min(5) }, async ({ paymentId, approvalId }) => ({
  content: [{ type: "text", text: `Replay requested for ${paymentId} with approval ${approvalId}` }]
}));

const transport = new StdioServerTransport();
await server.connect(transport);
