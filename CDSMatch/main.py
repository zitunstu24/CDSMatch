import argparse
from CDSMatch.blast import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run CDSMatch pipeline with configuration.")
    parser.add_argument("--config", type=str, default="config/config.yaml", help="Path to configuration file")
    args = parser.parse_args()

    main(args.config)

