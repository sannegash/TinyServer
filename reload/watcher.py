import time 

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

#Global flag to track changes 

changes_detected = False;

class MyEventHandler(FileSystemEventHandler):
    def on_any_change(self, event):
          global changes_detected
          # Ignore directory modifications if you want only file changes
          if not event.is_directory:
            print(f"Change detected: {event.src_path}")
            changes_detected = True


event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()

