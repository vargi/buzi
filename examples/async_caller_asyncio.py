import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.gen
import tornado.platform.asyncio
import logging
import asyncio

from buzi.asyncio.caller import Buzi

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        b = Buzi()
        result = yield from b.call("foo", 2, 3)
        self.set_header('Content-Type', 'text/html')
        self.write(str(result))
        self.finish()

application = tornado.web.Application([
    (r'/', MainHandler),
])




if __name__ == '__main__':
    tornado.platform.asyncio.AsyncIOMainLoop().install()

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print('Demo is runing at 0.0.0.0:8888\nQuit the demo with CONTROL-C')
    asyncio.get_event_loop().run_forever()
