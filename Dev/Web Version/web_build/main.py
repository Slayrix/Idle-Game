import pygame as pg, time, asyncio, game, event

#importing buttons and text (important)
import vars.textVars, vars.buttonVars.menuButtonVars, vars.buttonVars.cheatButtonVars, vars.buttonVars.upgradeButtonVars
  
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