import re

def convert_deg_min_sec(expr):
    def repl(m):
        deg = float(m.group(1)) if m.group(1) else 0
        minute = float(m.group(2)) if m.group(2) else 0
        second = float(m.group(3)) if m.group(3) else 0
        return f"({deg} + {minute}/60 + {second}/3600)"
    for trig in ['sin', 'cos', 'tan', 'cotan']:
        expr = re.sub(
            fr"{trig}\(([0-9]+(?:\.[0-9]+)?)(?:'([0-9]+(?:\.[0-9]+)?))?(?:'([0-9]+(?:\.[0-9]+)?))?'?\)",
            lambda m: f"{trig}{repl(m)}", expr)
    return expr

def parse_int_value(value):
    value = value.strip()
    if value.startswith('0b'):
        return int(value, 2)
    elif value.startswith('0x'):
        return int(value, 16)
    elif value.startswith('0o'):
        return int(value, 8)
    else:
        return int(float(value))