from client import ReActAgentEngine

tools = {
    "math_eval": lambda expr: str(eval(expr)),
    "currency_lookup": lambda cur: "1 USD = 7.24 CNY" if cur == "USD_CNY" else "Unknown"
}

agent = ReActAgentEngine(tools)
done, obs = agent.run_step("Need to check exchange rate", "currency_lookup", "USD_CNY")
print("Step 1 Observation:", obs)

done, obs = agent.run_step("Convert 50 USD to CNY", "math_eval", "50 * 7.24")
print("Step 2 Observation:", obs)

done, answer = agent.run_step("Got converted sum", "FINISH", f"50 USD is {obs} CNY")
print("Final Answer:", answer)
