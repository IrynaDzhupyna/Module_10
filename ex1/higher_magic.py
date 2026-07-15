from collections.abc import Callable

# spells
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


# Higher Order Functions
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    # should it return a str as a spell or match subject
    def amplified_power(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {', '.join(result)}")

    print("\nTesting power amplifier...")
    original = fireball("Dragon", 10)
    amplified = power_amplifier(fireball, 3)("Dragon", 10)
    print(f"Original: {original}")
    print(f"Amplified: {amplified}")

    print("\nTesting conditional caster...")
    strong_spell = conditional_caster(lambda t, p: p > 5, fireball)
    weak_spell = conditional_caster(lambda t, p: p > 5, fireball)
    print(f'Success case: {strong_spell("Dragon", 10)}')
    print(f'Fizzle case: {weak_spell("Dragon", 3)}')

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    results = sequence("Dragon", 10)
    for line in results:
        print(line)


if __name__ == "__main__":
    main()
