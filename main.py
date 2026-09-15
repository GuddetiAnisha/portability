import argparse
from pathlib import Path
from app.converter import convert
from app.report import make_report

def main():
    p = argparse.ArgumentParser(description="Convert a constrained subset of vendor-specific RTL.")
    p.add_argument("input")
    p.add_argument("--source", required=True, choices=["xilinx","intel","asic_generic","generic"])
    p.add_argument("--target", required=True, choices=["xilinx","intel","asic_generic","generic"])
    p.add_argument("--output", default="converted.sv")
    args = p.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    result = convert(text, args.source, args.target)
    Path(args.output).write_text(result.converted_text, encoding="utf-8")
    Path(args.output + ".report.md").write_text(make_report(text, result), encoding="utf-8")
    print(f"Wrote {args.output}")
    print(f"Replacements: {result.replacements}")
    for w in result.warnings:
        print("WARNING:", w)

if __name__ == "__main__":
    main()
