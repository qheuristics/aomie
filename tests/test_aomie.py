
from click.testing import CliRunner

from aomie.cli import fetch


def test_fetch():
    runner = CliRunner()
    result = runner.invoke(fetch, [])

    assert result.exit_code == 0
    # assert result.output == '()\n'
