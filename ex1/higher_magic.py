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
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


def main() -> None:

    print("\nTesting spell combiner")

    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined("Dragon", 10)}")

    print("\nTesting power_amplifier")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball("Dragon", 10)}, "
          f"\nAmplified: {mega_fireball("Dragon", 10)}")

    # test_values = [6, 8, 15]
    # test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']



if __name__ == "__main__":
    main()
