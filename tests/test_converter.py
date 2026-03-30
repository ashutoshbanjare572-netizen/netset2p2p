from pathlib import Path

import pytest

from netset2p2p.converter import NetsetParseError, convert_netset_text_to_p2p


def test_convert_cidr_and_single_ip() -> None:
    source = "# header\n1.2.3.4\n10.0.0.0/30\n"
    actual = convert_netset_text_to_p2p(source)

    assert actual == (
        "netset2p2p:1.2.3.4-1.2.3.4\n"
        "netset2p2p:10.0.0.0-10.0.0.3\n"
    )


def test_convert_empty_input() -> None:
    assert convert_netset_text_to_p2p("   \n\n") == ""


def test_invalid_line_raises() -> None:
    with pytest.raises(NetsetParseError):
        convert_netset_text_to_p2p("not-a-network\n")


def test_skip_invalid_lines() -> None:
    actual = convert_netset_text_to_p2p(
        "10.0.0.0/31\nnot-a-network\n10.0.0.2/31\n",
        skip_invalid=True,
    )
    assert actual == (
        "netset2p2p:10.0.0.0-10.0.0.1\n"
        "netset2p2p:10.0.0.2-10.0.0.3\n"
    )


def test_ipv6_rejected_by_default() -> None:
    with pytest.raises(NetsetParseError):
        convert_netset_text_to_p2p("2001:db8::/126\n")


def test_ipv6_allowed_when_enabled() -> None:
    actual = convert_netset_text_to_p2p("2001:db8::/126\n", allow_ipv6=True, label="v6")
    assert actual == "v6:2001:db8::-2001:db8::3\n"


def test_label_validation() -> None:
    with pytest.raises(ValueError):
        convert_netset_text_to_p2p("10.0.0.0/31\n", label="bad:label")


def test_fixture_file_conversion_matches_expected_output() -> None:
    fixtures_dir = Path(__file__).parent / "fixtures"
    input_text = (fixtures_dir / "sample_firehol.netset").read_text(encoding="utf-8")
    expected = (fixtures_dir / "sample_firehol_expected.p2p").read_text(encoding="utf-8")

    actual = convert_netset_text_to_p2p(input_text, label="firehol_sample")
    assert actual == expected
