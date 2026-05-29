# Sync Hydrawise watering system with Shelly actor

Because my pressure pump sensor is broken, the pump was running a lot (expensive watering solution :-( ). I decided to integrate a Shelly PM 1 plus sensor/actor to the circle and remove the pressure pump sensor that normally activates/deactivates the pump.

Nowadays the pump is activated, when the Hydrawise needs it and is deactivated, when it is no longer needed. This small python project realizes just that.

Take care: The server this script is running on, should be in the local area network (LAN) and be able to pull the hydrawise api from the internet and the shelly using its LAN-IP. The Shelly could be triggered using the cloud api, for simplicity i decided against it. Actually my [Magic Mirror](https://github.com/stefanjacobs/MagicMirror) that uses a raspberry pi is the server I am running this script on ;-)

## Installation

Das Projekt nutzt `uv` als Paketmanager. Einmalig Abhängigkeiten installieren:

```bash
cd /home/pi/tools/hydraShellySync
uv sync
```

Danach das Skript starten:

```bash
uv run app.py
```

Oder direkt via Python aus dem `.venv`:

```bash
.venv/bin/python app.py
```

Für den Dauerbetrieb auf einem Server bietet sich [pm2](https://pm2.keymetrics.io/) oder ein systemd-Service an.

## Configuration

An example configuration can be seen in `cfg/config.example.yml`, just make a copy of it and name it in cfg and name it `cfg/config.yml`:

```yaml
log-level: WARN
hydra-status-url: "https://api.hydrawise.com/api/v1/statusschedule.php"
hydra-api-key: "XXXX-XXXX-XXXX-XXXX"
hydra-sleep: 60
shelly-ip: "http://192.168.12.12/"
shelly-status-url: "rpc/Shelly.GetStatus"
shelly-switch-url: "rpc/Switch.Set"
shelly-switch-id: "0"
```

- `log-level` see python.logging doc [here](https://docs.python.org/3/howto/logging.html#logging-levels), set here as a string
- `hydra-status-url` see Hydrawise API at the links section
- `hydra-api-key` see Hydrawise API at the links section
- `hydra-sleep` integer wait time in seconds. If you hit the hydrawise api more than once a minute you may get rate-limited
- `shelly-ip` the static ip/url for your local shelly actor
- `shelly-status-url` the get status action url, may be constant
- `shelly-switch-url` the set switch action url, may be constant
- `shelly-switch-id` the id of the switch, there are shelly devices with more than one switch

## Links

- [Hydrawise API](https://support.hydrawise.com/hc/en-us/article_attachments/360058265154/Hydrawise_REST_API.pdf)
- [Shelly PM 1 plus API](https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Switch#switchset)
