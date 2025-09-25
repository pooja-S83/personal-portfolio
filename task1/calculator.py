
"""
Enhanced CLI Calculator
- Functions for +, -, *, / (explicit functions provided)
- Safe expression eval (AST-based)
- Menu + free-form expression mode
- 'ans' token reuses last result inside expressions or as operand
- Save history to a file
"""

import ast
import operator as op
import math
from typing import Any, List, Tuple

# --- Required operation functions ---
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# Extras
def power(a, b): return a ** b
def percent(a): return a / 100.0
def sqrt(a):
    if a < 0:
        raise ValueError("sqrt of negative number is not supported.")
    return math.sqrt(a)

# --- Safe expression evaluation via AST ---
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
    ast.FloorDiv: op.floordiv,
}

def safe_eval(expr: str) -> float:
    """Evaluate a numeric expression safely (only arithmetic)."""
    try:
        tree = ast.parse(expr, mode='eval')
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}") from e

    def _eval(node):
        if isinstance(node, ast.Expression): return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)): return node.value
            raise ValueError("Only numeric constants allowed")
        if isinstance(node, ast.BinOp):
            l, r = _eval(node.left), _eval(node.right)
            opf = ALLOWED_OPERATORS.get(type(node.op))
            if not opf: raise ValueError(f"Operator {type(node.op)} not allowed")
            try:
                return opf(l, r)
            except ZeroDivisionError:
                raise ValueError("Division by zero is not allowed")
        if isinstance(node, ast.UnaryOp):
            opf = ALLOWED_OPERATORS.get(type(node.op))
            if not opf: raise ValueError(f"Unary operator {type(node.op)} not allowed")
            return opf(_eval(node.operand))
        raise ValueError("Unsupported syntax")

    return _eval(tree)


# --- CLI Helpers ---
def print_menu():
    print("""
                   Hello WelCome to personal Calculator🧮💕
          
Choose an option:
 1) Add (a + b)
 2) Subtract (a - b)
 3) Multiply (a * b)    
 4) Divide (a / b)
 5) Power (a ** b)
 6) Square root (sqrt a)
 7) Percent (a % -> a/100)
 8) Enter a free-form expression (e.g. 2 + 3*4 - (1/2))
 9) Show history
 S) Save history to file
 Q) Quit
""")

def two_inputs(prompt1="Enter first number: ", prompt2="Enter second number: " ) -> Tuple[str, str]:
    a = input(prompt1).strip()
    b = input(prompt2).strip()
    return a, b

def maybe_replace_ans(token: str, ans: Any) -> str:
    if token.lower() == 'ans' and ans is not None:
        return str(ans)
    return token

def save_history(history: List[str], filename: str = "calculator_history.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n".join(history) + "\n")
    print(f"Saved history to {filename}")

# --- Main loop ---
def main():
    history: List[str] = []
    memory: float = 0.0
    last_answer: Any = None

    while True:
        print_menu()
        choice = input("Enter choice: ").strip().lower()
        if not choice:
            continue
        if choice == 'q':
            print(" Thanks for using the calculator!🤝 HAVE A NICE DAY 💕")
            break

        try:
            if choice == '1':
                a_s, b_s = two_inputs()
                a_s = maybe_replace_ans(a_s, last_answer)
                b_s = maybe_replace_ans(b_s, last_answer)
                a, b = float(a_s), float(b_s)
                res = add(a, b)
                print("Result:", res)
                history.append(f"{a} + {b} = {res}"); last_answer = res

            elif choice == '2':
                a_s, b_s = two_inputs()
                a_s = maybe_replace_ans(a_s, last_answer)
                b_s = maybe_replace_ans(b_s, last_answer)
                a, b = float(a_s), float(b_s)
                res = sub(a, b)
                print("Result:", res)
                history.append(f"{a} - {b} = {res}"); last_answer = res

            elif choice == '3':
                a_s, b_s = two_inputs()
                a_s = maybe_replace_ans(a_s, last_answer)
                b_s = maybe_replace_ans(b_s, last_answer)
                a, b = float(a_s), float(b_s)
                res = mul(a, b)
                print("Result:", res)
                history.append(f"{a} * {b} = {res}"); last_answer = res

            elif choice == '4':
                a_s, b_s = two_inputs()
                a_s = maybe_replace_ans(a_s, last_answer)
                b_s = maybe_replace_ans(b_s, last_answer)
                a, b = float(a_s), float(b_s)
                res = div(a, b)
                print("Result:", res)
                history.append(f"{a} / {b} = {res}"); last_answer = res

            elif choice == '5':
                a_s, b_s = two_inputs()
                a_s = maybe_replace_ans(a_s, last_answer)
                b_s = maybe_replace_ans(b_s, last_answer)
                a, b = float(a_s), float(b_s)
                res = power(a, b)
                print("Result:", res)
                history.append(f"{a} ** {b} = {res}"); last_answer = res

            elif choice == '6':
                a_s = input("Enter number: ").strip()
                a_s = maybe_replace_ans(a_s, last_answer)
                a = float(a_s)
                res = sqrt(a)
                print("Result:", res)
                history.append(f"sqrt({a}) = {res}"); last_answer = res

            elif choice == '7':
                a_s = input("Enter number: ").strip()
                a_s = maybe_replace_ans(a_s, last_answer)
                a = float(a_s)
                res = percent(a)
                print("Result:", res)
                history.append(f"percent({a}) = {res}"); last_answer = res

            elif choice == '8':
                expr = input("Enter expression (you can use 'ans'): ").strip()
                if last_answer is not None:
                    expr = expr.replace("ans", str(last_answer)).replace("ANS", str(last_answer))
                res = safe_eval(expr)
                print("Result:", res)
                history.append(f"{expr} = {res}"); last_answer = res

            elif choice == '9':
                if not history:
                    print("History is empty.")
                else:
                    print("--- History (last 50 entries) ---")
                    for i, item in enumerate(history[-50:], start=1):
                        print(f"{i}. {item}")

            elif choice == 's':
                if not history:
                    print("Nothing to save (history empty).")
                else:
                    fn = input("Filename (default calculator_history.txt): ").strip()
                    if not fn:
                        fn = "calculator_history.txt"
                    save_history(history, fn)

            else:
                print("Unknown choice. Enter menu number")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Thank you!")
