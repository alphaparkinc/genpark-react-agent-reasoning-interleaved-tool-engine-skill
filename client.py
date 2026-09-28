"""ReAct (Reasoning + Acting) Agent Engine.
100% Python Standard Library.
"""

class ReActAgentEngine:
    """ReAct interleaved reasoning and tool acting engine with scratchpad memory."""
    def __init__(self, tools):
        self.tools = tools
        self.scratchpad = []

    def run_step(self, thought, action_name, action_input):
        self.scratchpad.append(f"Thought: {thought}")
        if action_name == "FINISH":
            self.scratchpad.append(f"Final Answer: {action_input}")
            return True, action_input

        if action_name in self.tools:
            try:
                obs = self.tools[action_name](action_input)
                self.scratchpad.append(f"Action: {action_name}({action_input})")
                self.scratchpad.append(f"Observation: {obs}")
                return False, obs
            except Exception as e:
                err = f"Execution error: {e}"
                self.scratchpad.append(f"Observation Error: {err}")
                return False, err
        else:
            err = f"Tool '{action_name}' not found."
            self.scratchpad.append(f"Observation Error: {err}")
            return False, err
