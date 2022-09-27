# https://support.hydrawise.com/hc/en-us/article_attachments/360058265154/Hydrawise_REST_API.pdf

# curl https: //api.hydrawise.com/api/v1/statusschedule.php?api_key=XXXX-XXXX-XXXX-XXXX
{
    "time": 1664263384,
    "nextpoll": 60,
    "message": "",
    "simRelays": 1,
    "options": 1,
    "master": 12,
    "master_timer": 0,
    "master_post_timer": 0,
    "expanders": [],
    "sensors": [],
    "relays": [
        {
            "relay_id": 2605507,
            "time": 153416,
            "type": 6,
            "run": 420,
            "relay": 1,
            "name": "asdf",
            "period": 259200,
            "timestr": "Thu"
        },
        {
            "relay_id": 2605508,
            "time": 153836,
            "type": 1,
            "run": 540,
            "relay": 2,
            "name": "asdf",
            "period": 259200,
            "timestr": "Thu"
        },
        {
            "relay_id": 2605509,
            "time": 154376,
            "type": 6,
            "run": 420,
            "relay": 3,
            "name": "asdf",
            "period": 259200,
            "timestr": "Thu"
        },
        {
            "relay_id": 2605510,
            "time": 67016,
            "type": 6,
            "run": 420,
            "relay": 4,
            "name": "asdf",
            "period": 259200,
            "timestr": "04:00"
        },
        {
            "relay_id": 2605511,
            "time": 67436,
            "type": 6,
            "run": 540,
            "relay": 5,
            "name": "asdf",
            "period": 259200,
            "timestr": "04:07"
        },
        {
            "relay_id": 2605512,
            "time": 155756,
            "type": 6,
            "run": 540,
            "relay": 6,
            "name": "asdf",
            "period": 259200,
            "timestr": "Thu"
        },
        {
            "relay_id": 2605513,
            "time": 67976,
            "type": 6,
            "run": 420,
            "relay": 7,
            "name": "asdf",
            "period": 259200,
            "timestr": "04:16"
        },
        {
            "relay_id": 2605514,
            "time": 68396,
            "type": 6,
            "run": 420,
            "relay": 8,
            "name": "asdf",
            "period": 259200,
            "timestr": "04:23"
        }
    ]
}


time: Number of seconds until the next programmed run. Value will be 1 if a run is in progress