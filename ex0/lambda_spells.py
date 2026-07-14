def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    ''' map() executes a specific function for each item in an iterable'''
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:

    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Shadow Blade", "power": 60, "type": "weapon"},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    mages = [
        {"name": "Alex", "power": 45, "element": "fire"},
        {"name": "Jordan", "power": 78, "element": "water"},
        {"name": "Riley", "power": 30, "element": "earth"},
    ]
    strong_mages = power_filter(mages, 40)
    print(f"Mages with power >= 40: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
