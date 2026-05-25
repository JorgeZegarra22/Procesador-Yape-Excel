import urllib.request
import json
import sys

def get_status(channel):
    url = f"https://kick.com/api/v2/channels/{channel}"
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            is_live = data.get('livestream') is not None
            viewer_count = 0
            stream_title = ""
            if is_live and data['livestream']:
                viewer_count = data['livestream'].get('viewer_count', 0)
                stream_title = data['livestream'].get('session_title', "")
            return {
                "isLive": is_live,
                "viewers": viewer_count,
                "title": stream_title,
                "success": True
            }
    except Exception as e:
        return {
            "isLive": False,
            "viewers": 0,
            "title": "",
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    channel_name = sys.argv[1] if len(sys.argv) > 1 else "kingteka"
    result = get_status(channel_name)
    print(json.dumps(result))
