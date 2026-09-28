import sys
import json
from client import ReActAgentEngine

tools = {
    "echo": lambda x: f"Echo: {x}",
    "length": lambda x: str(len(x))
}
agent = ReActAgentEngine(tools)

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "react_step",
                        "description": "Execute single ReAct step (thought, action, input) with scratchpad tracking",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "thought": {"type": "string"},
                                "action": {"type": "string"},
                                "action_input": {"type": "string"}
                            },
                            "required": ["thought", "action", "action_input"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "react_step":
            done, output = agent.run_step(args["thought"], args["action"], args["action_input"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"finished": done, "output": output, "scratchpad": agent.scratchpad})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
