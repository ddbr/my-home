from sf.lib import aiocurl, alog

async def onButtonEvent(*argv):
    await alog("Button pressed: %s", argv)
    await aiocurl(
        'http://192.168.1.123:5000/trigger',
        method='POST',
        headers={'Content-Type': 'application/json'},
        body='{"button_id": "{scene_name}"}'
    )
