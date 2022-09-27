import requests, logging
from enum import Enum
from config import Config
from sleeprange import wait

Pump = Enum("Pump", "activatePump deactivatePump")
ShellySwitch = Enum("ShellySwitch", "on off")

logging.basicConfig()
log = logging.getLogger(__name__)

# check, if hydra is active or is going to be active in 60s
# returns "activatePump" or "deactivatePump"
def checkHydra(config: Config):
    hydraStatusUrl = config.get("hydra-status-url")
    params = {
        'api_key': config.get("hydra-api-key")
    }
    response = requests.get(hydraStatusUrl, params=params)
    if response.status_code != 200:
        log.error("checkHydra returned NO 200, getStatus failed")
        raise Exception("Got no 200 response from checkHydra")
    data = response.json()
    for relay in data["relays"]:
        if relay["time"] <= 60:
            log.debug("Hydra needs pump and requests activation")
            return Pump.activatePump
    log.debug("Hydra needs no pump and requests deactivation")
    return Pump.deactivatePump


# check, if shelly is "on" or "off"
# returns "on" or "off"
def checkShelly(config: Config):
    shellyUrl = config.get("shelly-ip") + config.get("shelly-status-url")
    response = requests.get(shellyUrl)
    if response.status_code != 200:
        log.error("checkShelly returned NO 200, getStatus failed")
        raise Exception("Got no 200 response in checkShelly")
    data = response.json()
    if data["switch:0"]["output"] == True:
        log.debug("Shelly Switch is in status 'on'")
        return ShellySwitch.on
    log.debug("Shelly Switch is in status 'off'")
    return ShellySwitch.off


def switchShelly(status: ShellySwitch):
    shellyUrl = config.get("shelly-ip") + config.get("shelly-switch-url")
    output = "true"
    if status == ShellySwitch.off:
        output = "false"
    log.debug("Shelly Switch wants to switch to output=" + output)

    params = {
        'id': config.get("shelly-switch-id"),
        'on': output
    }
    response = requests.get(shellyUrl, params=params)
    if response.status_code == 200:
        log.debug("Shelly Switch returned 200, switch successful")
        return
    log.error("switchShelly returned NO 200, switch failed")
    raise Exception("Got no 200 response in switchShelly")


def singlestep(config: Config):
    needPump = checkHydra(config)
    currentShellyStatus = checkShelly(config)
    if needPump == Pump.deactivatePump and currentShellyStatus == ShellySwitch.off:
        log.info("No pump needed and shelly off, nothing to do")
        return
    if needPump == Pump.deactivatePump and currentShellyStatus == ShellySwitch.on:
        log.info("Pump not needed, but shelly on, turning it off")
        return switchShelly(ShellySwitch.off)
    if needPump == Pump.activatePump and currentShellyStatus == ShellySwitch.off:
        log.info("Pump needed, but shelly off, turning it on")
        return switchShelly(ShellySwitch.on)
    if needPump == Pump.activatePump and currentShellyStatus == ShellySwitch.on:
        log.info("Pump needed and shelly on, nothing to do")
        return

    log.error("Something strange happened, the singlestep failed and no exception was thrown")
    raise Exception("Singlestep failed, none of the above status checks succeeded. Should not happen.")


def mainloop(config: Config):
    while (True):
        try:
            singlestep(config)
        except Exception as e:
            log.error(e)
            log.warn("Program is ignoring the error and continues.")
        finally:
            wait(config.get("hydra-sleep"))


if __name__ == "__main__":
    config = Config("cfg/config.yml")
    log.setLevel(config.get("log-level"))
    mainloop(config)