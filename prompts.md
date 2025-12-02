# 🧠 Team Shared Prompt Library
**Goal:** Standardize how we use Copilot to ensure consistent code quality, security, and documentation across the team.

---

## 🛠️ 1. The Refactoring Standard
**Use when:** Modernizing legacy code or cleaning up technical debt.
**Why:** Ensures everyone follows PEP8 and uses efficient data structures (like Dictionaries instead of massive If/Else chains).

### The Prompt:
> "Refactor this selected code to adhere to PEP8 standards. Replace long `if/else` chains with dictionary lookups where applicable to improve performance. Add type hints to all function signatures."

---

## 🛡️ 2. The Security Auditor
**Use when:** Reviewing code before opening a Pull Request.
**Why:** Catch common vulnerabilities (OWASP Top 10) that humans often miss.

### The Prompt:
> "@workspace /explain Analyze the selected file for OWASP Top 10 security vulnerabilities. Specifically check for:
> 1. Input Validation issues
> 2. Hardcoded Secrets
> 3. SQL Injection risks"

---

## 📝 3. The Documentation Generator
**Use when:** You inherit code with zero comments (like `order_processor.py`).
**Why:** Enforces a consistent docstring style (Google-Style) so automated tools can read it later.

### The Prompt:
> "/doc Generate Google-style docstrings for all functions in this file. Include 'Args', 'Returns', and 'Raises' sections. Ensure the summary explains the *business logic* not just the syntax."

---

## 🧪 4. The Edge-Case Hunter
**Use when:** Writing Unit Tests.
**Why:** Developers write "Happy Path" tests. AI is better at thinking of ways to break the code.

### The Prompt:
> "/tests Generate a pytest suite for this function. Specifically include edge cases for:
> 1. Negative numbers
> 2. Null or None values
> 3. Invalid string formats
> Ensure all tests are self-contained."

---

## ⚡ 5. The SQL Optimizer
**Use when:** You have a slow database query.
**Why:** Explains the "Cost" of the query and suggests specific indexes.

### The Prompt:
> "Analyze this SQL query for performance on a dataset of 10 million rows. Identify potential bottlenecks (like full table scans) and suggest specific Indexes that would optimize the execution plan."