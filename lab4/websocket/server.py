import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        WebSocketServer.clients.add(self)

    def on_close(self):
        WebSocketServer.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(seft):
        return random.choice(seft.word_list)

def main():
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)

    io_loop = tornado.ioloop.IOLoop.current()

    word_selector = RandomWordSelector(['apple', 'banana','orange', 'grape', 'melon','kokonut','strongberry','lemon','watermelon','melon'])
    #for i in range(0, 5): 
        #print(word_selector[i])
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda:WebSocketServer.send_message(word_selector.sample()), 3000
        )

    periodic_callback.start()
    io_loop.start()
    
if __name__ == "__main__":
    main()   