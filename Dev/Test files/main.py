import pygame as pg, time, asyncio, core.game as game, core.event as event

#import vars.textVars, vars.textBoxVars, vars.buttonVars.menuButtonVars, vars.buttonVars.cheatButtonVars, vars.buttonVars.upgradeButtonVars
import vars.infoboxVars, vars.buttonVars.testButtonVars

async def gameLoop():
    tick = 0
    running = True
    while running:
        running = event.eventCheck(running)
        game.updateScreen()
        tick = game.gameTick(tick)
        time.sleep(.01)
        await asyncio.sleep(0)
asyncio.run(gameLoop())
pg.quit()