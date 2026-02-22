from datetime import datetime, timezone


def main() -> None:
    print("connected-vehicle-threat-monitoring-system initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
