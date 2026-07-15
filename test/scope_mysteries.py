from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter = 0

    def call_counter() -> int:
        nonlocal counter
        counter += 1
        return counter
    return call_counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def power_accumulator(amount: int) -> int:
        nonlocal power
        power = power + amount
        return power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> tuple[str, Any]:
        vault[key] = value
        return key, value

    def recall(key: str) -> Any:
        if key not in vault:
            return "Memory not found"
        return vault[key]
    return {"store": store, "recall": recall}


def main() -> None:

    print("\nTesting mage counter...")
    counter_a = mage_counter()
    for i in range(1, 4):
        print(f"counter_a call {i}: {counter_a()}")

    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    initial_power = 100
    new_power = spell_accumulator(initial_power)
    print(f"Base {initial_power}, add 20: {new_power(20)}")
    print(f"Base {initial_power}, add 30: {new_power(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    print(f"{flaming('Sword')}")
    frozen = enchantment_factory("Frozen")
    print(f"{frozen('Shield')}")

    print("\nTesting memory vault...")
    vault = memory_vault()

    key, value = vault["store"]("secret", 42)
    print(f"Store '{key}' = {value}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


main()
