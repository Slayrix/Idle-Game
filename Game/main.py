import pygame as pg
import time, asyncio, game, event, text, buttonVars #Keep the text and buttonVars it is needed
  
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