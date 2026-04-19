import requests

SECURITY_HEADERS = [ 
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection",
    "Feature-Policy",
    "Public-Key-Pins",
    "HTTP Strict-Transport-Security",
    "Cache-Control",
    "CORS Headers",
    "Cross-Origin-Resource-Policy",
    "Secure Cookies",
    "Expect-CT",
]

def check_http_headers(target: str) -> dict:
    try:
        if not target.startswith("http://") and not target.startswith("https://"):
            target = "http://" + target

        response = requests.get(target, timeout=10)
        headers =  dict(response.headers)

        found = {}
        missing = []

        for header in SECURITY_HEADERS:
            value = headers.get(header, None)
            if value is not None:
                found[header] = value
            else:
                missing.append(header)

        return { 
            "status": "OK",
            "found": found,
            "missing": missing
        }
    
    except requests.exceptions.ConnectionError:
        return { "status": "error", "message": "Could not connect to target" }
    except requests.exceptions.Timeout:
        return { "status": "error", "message": "Request timed out" }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": str(e)}