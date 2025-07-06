## 📅 Day 3 - Convert English Sentence into Structured Formats

### 🧠 Skill of the Day:
Today, I learned how to convert a simple English sentence into **structured formats** like:
- 📦 JSON (commonly used in APIs and data storage)
- 📊 Table (used in SQL, Excel, and data visualization tools)
- 🌐 Graph (used in knowledge graphs and databases like Neo4j)

This skill helps break down unstructured natural language into machine-readable formats.

---

### ✨ Input Sentence:
> **"OpenAI collaborated with Microsoft to deploy ChatGPT, which was trained on large-scale text datasets using Reinforcement Learning from Human Feedback (RLHF)."**

### 📦 JSON Output

```json
{
  "collaboration": {
    "partners": ["OpenAI", "Microsoft"],
    "project": "ChatGPT",
    "action": "deployed"
  },
  "training": {
    "model": "ChatGPT",
    "data": "large-scale text datasets",
    "method": "Reinforcement Learning from Human Feedback (RLHF)"
  }
}

