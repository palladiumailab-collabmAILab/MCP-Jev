from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ScaffoldContractTests(unittest.TestCase):
    def test_repository_is_explicitly_marked_non_deployable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Status: scaffold / not deployable", readme)
        self.assertIn("mcp-toolbox/servers/jev-cloudflare", readme)

    def test_design_preserves_fail_closed_and_bounded_intent(self) -> None:
        design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
        self.assertIn("fail-closed", design)
        self.assertIn("bounded", design.lower())


if __name__ == "__main__":
    unittest.main()
