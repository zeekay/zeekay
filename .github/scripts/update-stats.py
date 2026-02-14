#!/usr/bin/env python3
"""Update README.md with latest stats from zeekay/stats dashboard."""

import json
import os
import re
import urllib.request


def api(path, token=""):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def fmt(n):
    if abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif abs(n) >= 1_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,}"


def replace_section(text, marker, content):
    pattern = f"(<!-- {marker}:START -->).*?(<!-- {marker}:END -->)"
    return re.sub(pattern, f"\\1\n{content}\n\\2", text, flags=re.DOTALL)


def main():
    token = os.environ.get("GH_TOKEN", "")

    # Fetch org repo counts
    orgs = {}
    for org in ["hanzoai", "luxfi", "zenlm", "zoo-labs"]:
        try:
            data = api(f"/orgs/{org}", token)
            orgs[org] = data.get("public_repos", 0)
        except Exception:
            orgs[org] = "?"

    user = api("/users/zeekay", token)
    orgs["zeekay"] = user.get("public_repos", 0)

    # Try fetching stats from raw GitHub content
    has_stats = False
    stats = None
    try:
        url = "https://raw.githubusercontent.com/zeekay/stats/main/docs/data.json"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as r:
            stats_data = json.loads(r.read())
        stats = stats_data["data"]["zeekay"]["stats"]
        has_stats = True
        print(f"Fetched stats: {stats['total_commits']:,} commits")
    except Exception as e:
        print(f"Stats data unavailable: {e}")

    with open("README.md") as f:
        readme = f.read()

    # Update org counts
    focus = {
        "hanzoai": "AI infrastructure, agents, MCP, LLM gateway",
        "luxfi": "Post-quantum blockchain, consensus, DeFi",
        "zenlm": "Open foundation models, training, inference",
        "zoo-labs": "DeAI research, decentralized science",
        "zeekay": "Open source tools, protocols, experiments",
    }
    org_lines = ["| Org | Repos | Focus |", "|-----|-------|-------|"]
    for org, count in orgs.items():
        org_lines.append(f"| [{org}](https://github.com/{org}) | {count} | {focus[org]} |")
    readme = replace_section(readme, "ORGS", "\n".join(org_lines))

    if has_stats:
        stats_block = (
            "```\n"
            f"  {stats['total_commits']:>7,}  commits        {stats['years_coding']:.1f}  years coding       {stats['unique_repos']:,}  repos touched\n"
            f"  {fmt(stats['total_additions']):>5}   lines added    {fmt(stats['total_deletions']):>5} lines deleted      {fmt(stats['net_loc_change']):>5}  net lines\n"
            f"  {stats['active_days']:>7,}  active days       {stats['longest_streak']:>2}  longest streak     {stats['most_productive_day'][:3]}  most productive day\n"
            "```"
        )
        readme = replace_section(readme, "STATS", stats_block)

        yearly = stats["yearly"]
        years_sorted = sorted(yearly.items(), key=lambda x: x[0], reverse=True)
        lines = [
            "```",
            "Year     Commits    Lines Added    Lines Deleted    Net LOC        Active Days",
            "─────    ───────    ───────────    ─────────────    ───────────    ───────────",
        ]
        for year, yd in years_sorted:
            net = yd["net_loc"]
            sign = "+" if net >= 0 else ""
            lines.append(
                f"{year}     {yd['commits']:>7,}     {yd['additions']:>11,}       {yd['deletions']:>11,}     {sign}{net:>11,}          {yd['days_active']:>3}"
            )
        lines.append("```")
        readme = replace_section(readme, "YEARLY", "\n".join(lines))

        p30 = stats["periods"]["30d"]
        recent_block = (
            "```\n"
            f"  {p30['commits']:,} commits across {p30['repos']} repos\n"
            f"  {fmt(p30['additions'])}  lines added\n"
            f"  {fmt(p30['deletions'])}  lines deleted\n"
            "```"
        )
        readme = replace_section(readme, "RECENT", recent_block)

        print(f"Full update: {stats['total_commits']:,} commits, {stats['years_coding']:.1f} years")
    else:
        print("Org counts updated (stats data unavailable)")

    with open("README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
