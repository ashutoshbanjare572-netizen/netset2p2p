import runpy
from pathlib import Path

from netset2p2p.cli import main


def test_cli_writes_output_file(tmp_path: Path) -> None:
    input_file = tmp_path / "example.netset"
    output_file = tmp_path / "example.p2p"

    input_file.write_text("# test\n10.0.0.0/30\n", encoding="utf-8")
    exit_code = main(
        [str(input_file), "--output", str(output_file), "--label", "firehol_level1"]
    )

    assert exit_code == 0
    assert (
        output_file.read_text(encoding="utf-8")
        == "firehol_level1:10.0.0.0-10.0.0.3\n"
    )


def test_cli_writes_to_stdout(capsys: object, tmp_path: Path) -> None:
    input_file = tmp_path / "stdout.netset"
    input_file.write_text("198.51.100.9\n", encoding="utf-8")

    exit_code = main([str(input_file), "--label", "stdout_test"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "stdout_test:198.51.100.9-198.51.100.9\n"


def test_cli_returns_error_for_invalid_input(capsys: object, tmp_path: Path) -> None:
    input_file = tmp_path / "bad.netset"
    input_file.write_text("not-a-network\n", encoding="utf-8")

    exit_code = main([str(input_file)])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Invalid netset entry" in captured.err


def test_python_m_module_entrypoint(monkeypatch: object) -> None:
    monkeypatch.setattr("netset2p2p.cli.main", lambda: 0)
    try:
        runpy.run_module("netset2p2p.__main__", run_name="__main__")
    except SystemExit as exc:
        assert exc.code == 0
