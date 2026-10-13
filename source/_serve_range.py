#!/usr/bin/env python3
"""05.10 · локальний сервер деки з підтримкою Range (http.server без Range → Chrome обриває великі mp4, друге відео на слайді не стартує).
usage: python3 source/_serve_range.py [port]   (з папки preza-ai-operator; за замовчуванням 8765, 127.0.0.1)"""
import os, re, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class H(SimpleHTTPRequestHandler):
    def send_head(self):
        rng = self.headers.get('Range')
        path = self.translate_path(self.path)
        if not rng or os.path.isdir(path) or not os.path.isfile(path):
            return super().send_head()
        m = re.match(r'bytes=(\d*)-(\d*)', rng)
        size = os.path.getsize(path)
        if not m:
            return super().send_head()
        a, b = m.group(1), m.group(2)
        if a == '':
            start, end = max(0, size - int(b)), size - 1
        else:
            start, end = int(a), (int(b) if b else size - 1)
        end = min(end, size - 1)
        if start > end:
            self.send_error(416); return None
        f = open(path, 'rb'); f.seek(start)
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Content-Range', 'bytes %d-%d/%d' % (start, end, size))
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Accept-Ranges', 'bytes')
        self.end_headers()
        self._left = end - start + 1
        return f
    def copyfile(self, src, dst):
        left = getattr(self, '_left', None)
        if left is None:
            return super().copyfile(src, dst)
        try:
            while left > 0:
                chunk = src.read(min(256 * 1024, left))
                if not chunk: break
                dst.write(chunk); left -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')   # 06.10: без no-cache — браузер кешує ассети, дека гортається швидше
        super().end_headers()
    def log_message(self, *a): pass

if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
