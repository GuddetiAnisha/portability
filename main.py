import argparse
from pathlib import Path

from converter import convert
from report import make_report


PROFILES = ["legacy", "standard", "normalized"]


def main():
    parser = argparse.ArgumentParser(
        description="Analyze and transform structured text using configurable software rules."
    )
    parser.add_argument("input")
    parser.add_argument("--source", required=True, choices=PROFILES)
    parser.add_argument("--target", required=True, choices=PROFILES)
    parser.add_argument("--output", default="converted.txt")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    result = convert(text, args.source, args.target)

    output_path = Path(args.output)
    output_path.write_text(result.converted_text, encoding="utf-8")

    report_path = Path(str(output_path) + ".report.md")
    report_path.write_text(make_report(text, result), encoding="utf-8")

    print(f"Wrote {output_path}")
    print(f"Replacements: {result.replacements}")
    for warning in result.warnings:
        print("WARNING:", warning)


if __name__ == "__main__":
    main()
