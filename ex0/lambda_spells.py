def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True) 


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    pass


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


def main() -> None:

    artifacts: list[dict] = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"}
    ]
    print("\nTesting artifact sorter")
    sorted_artifacts = artifact_sorter(artifacts)
    



if __name__ == "__main__":
    main()