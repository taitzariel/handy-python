import argparse

_TAX_PER_CEILING = [
    (7_010, 0.1),
    (10_060, 0.14),
    (16_150, 0.2),
    (22_440, 0.31),
    (46_690, 0.35),
    (60_130, 0.47),
    (99_999, 0.5),
]

POINT_VALUE = 235  # value of one point of credit in NIS

def mas(bruto: float, points: float = 0) -> float:
    if bruto < 0:
        raise ValueError("bruto must be positive")
    
    tax = 0.0
    previous_ceiling = 0.0

    for ceiling, rate in _TAX_PER_CEILING:
        if bruto > ceiling:
            tax += (ceiling - previous_ceiling) * rate
            previous_ceiling = ceiling
        else:
            tax += (bruto - previous_ceiling) * rate
            break
    else:
        # Bruto above last ceiling
        last_rate = _TAX_PER_CEILING[-1][1]
        tax += (bruto - previous_ceiling) * last_rate

    # Subtract points of credit
    tax -= points * POINT_VALUE
    return max(tax, 0.0)  # tax can't be negative

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Israeli income tax (mas) from bruto salary.")
    parser.add_argument("bruto", type=float, help="Bruto monthly salary in NIS")
    parser.add_argument("-p", "--points", type=float, default=0.0, help="Number of tax credit points (נקודות זיכוי)")
    args = parser.parse_args()

    tax = mas(args.bruto, args.points)
    print(f"Bruto salary: {args.bruto} NIS")
    print(f"Tax credit points: {args.points}")
    print(f"Calculated tax: {tax:.2f} NIS")
