#!/usr/bin/env python
"""Tiny GAQL runner mirroring the read-only google-ads-mcp search tool.

usage: gaql.py <customer_id> "<GAQL>" [--out file.json]
Prints JSON rows (flattened, *_micros left as-is) to stdout or --out.
"""
import json
import sys
import os

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.protobuf.json_format import MessageToDict

CFG = os.path.expanduser("~/google-ads.yaml")


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out


def run(customer_id, query):
    client = GoogleAdsClient.load_from_storage(CFG, version=os.environ.get("GOOGLE_ADS_API_VERSION", "v22"))
    svc = client.get_service("GoogleAdsService")
    rows = []
    stream = svc.search_stream(customer_id=str(customer_id).replace("-", ""), query=query)
    for batch in stream:
        for row in batch.results:
            rows.append(flatten(MessageToDict(row._pb, preserving_proto_field_name=True)))
    return rows


def main():
    args = sys.argv[1:]
    out = None
    if "--out" in args:
        i = args.index("--out")
        out = args[i + 1]
        del args[i:i + 2]
    cid, query = args[0], args[1]
    try:
        rows = run(cid, query)
    except GoogleAdsException as ex:
        errs = [e.message for e in ex.failure.errors]
        print(json.dumps({"error": errs, "request_id": ex.request_id}), file=sys.stderr)
        sys.exit(2)
    payload = json.dumps(rows, indent=1)
    if out:
        with open(out, "w") as f:
            f.write(payload)
        print(f"{len(rows)} rows -> {out}")
    else:
        print(payload)


if __name__ == "__main__":
    main()
