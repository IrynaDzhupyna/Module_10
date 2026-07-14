from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_power(target, power) -> int:
        return power * multiplier
    return amplified_power


def main() -> None:
    # variable that stores a function. It is a function
    mega_fireball = power_amplifier(fireball, 3)

    print(mega_fireball("Dragon", 10))

    print()
    new_power = mega_fireball("Bat", 5)
    print(new_power)


main()
