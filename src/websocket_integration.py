
import asyncio
import websockets

async def update_data(websocket, path):
    while True:
        # Fetching new data (Placeholder)
        new_data = 'New Twitter Data'
        await websocket.send(new_data)
        await asyncio.sleep(10)  # Sending new data every 10 seconds

start_server = websockets.serve(update_data, 'localhost', 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
