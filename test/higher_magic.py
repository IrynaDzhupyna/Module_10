from collections.abc import Callable


# spells
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


# condition
def condition_power(target: str, power: int) -> str:
    return power >= 20


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_power(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def call_all_spells(target: str, power: int) -> list[str]:
        all_spells = []
        for spell in spells:
            action = spell(target, power)
            all_spells.append(action)
        return all_spells
    return call_all_spells



def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"{result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    print(f"Original: {fireball('Dragon', 10)}")
    powered = power_amplifier(fireball, 3)
    print(f"Powered: {powered('Dragon', 10)}")

    print("\nTesting conditional_caster...")
    new_fireball = conditional_caster(condition_power, fireball)
    print(new_fireball("Dragon", 30))
    print(new_fireball("Dragon", 10))

    print("\nTesting spell_sequence...")
    spells = [fireball, heal]
    sequence = spell_sequence(spells)
    for spell in spells:
        print(spell("Dragon", 10))


main()
