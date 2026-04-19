from modules.http_headers import check_http_headers

def run_scan(target: str) -> dict:
    results = {}

    results["port_scan"] = {"status": "pending"}
    results["http_headers"] = check_http_headers(target)
    results["ssl_tls"] = {"status": "pending"}
    results["dir_scan"] = {"status": "pending"}

    return {
        "target": target,
        "results": results
    }