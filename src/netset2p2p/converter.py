"""Core netset to p2p conversion logic."""

from __future__ import annotations

from ipaddress import IPv4Network, IPv6Network, ip_network


class NetsetParseError(ValueError):
    """Raised when an input line cannot be parsed as a netset entry."""


def _iter_networks(
    netset_text: str,
    *,
    allow_ipv6: bool,
    skip_invalid: bool,
) -> list[IPv4Network | IPv6Network]:
    networks: list[IPv4Network | IPv6Network] = []
    for line_number, raw_line in enumerate(netset_text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        candidate = line.split("#", maxsplit=1)[0].strip()
        if not candidate:
            continue

        token = candidate.split()[0]
        try:
            network = ip_network(token, strict=False)
        except ValueError as exc:
            if skip_invalid:
                continue
            raise NetsetParseError(
                f"Invalid netset entry on line {line_number}: {token!r}"
            ) from exc

        if (network.version == 6) and (not allow_ipv6):
            if skip_invalid:
                continue
            raise NetsetParseError(
                f"IPv6 entry on line {line_number} is not supported: {token!r}"
            )

        networks.append(network)
    return networks


def _to_range(network: IPv4Network | IPv6Network) -> tuple[str, str]:
    start = str(network.network_address)
    end = str(network.broadcast_address if network.version == 4 else network[-1])
    return start, end


def convert_netset_text_to_p2p(
    netset_text: str,
    *,
    label: str = "netset2p2p",
    allow_ipv6: bool = False,
    skip_invalid: bool = False,
) -> str:
    """Convert FireHOL-style netset text to PeerGuardian p2p format.

    Input netset:
    - comment lines start with '#'
    - data lines contain IPv4/IPv6 addresses or CIDRs

    Output p2p:
    - one range per line using: '<label>:<start-ip>-<end-ip>'
    """
    if (":" in label) or ("\n" in label) or ("\r" in label):
        raise ValueError("Label cannot contain ':', '\\n', or '\\r'.")

    networks = _iter_networks(
        netset_text,
        allow_ipv6=allow_ipv6,
        skip_invalid=skip_invalid,
    )
    if not networks:
        return ""

    lines: list[str] = []
    for network in networks:
        start, end = _to_range(network)
        lines.append(f"{label}:{start}-{end}")
    return "\n".join(lines) + "\n"
