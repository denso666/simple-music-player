import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from pygame import mixer
from MusicPlayer import MusicPlayer
from ProgressControl import ProgressControl

class Handler:
    def __init__( self, mixer, progress, text ) -> None:
        self.mp = MusicPlayer( mixer )
        self.pb = ProgressControl( progress )
        self.t = text
        self.t.set_text( self.mp.song_string() )
        self.pb.start()

    def play( self, button ) -> None:
        self.mp.play()
        self.pb.restart( self.mp.song_time() )

    def toggle_pause( self, button ) -> None:
        self.mp.toggle_pause()
        self.pb.toggle_pause()

    def on_forward( self, button ) -> None:
        self.mp.next()
        self.pb.restart( self.mp.song_time() )
        self.t.set_text( self.mp.song_string() )

    def on_rewind( self, button ) -> None:
        self.mp.previous()
        self.pb.restart( self.mp.song_time() )
        self.t.set_text( self.mp.song_string() )

    def on_random( self, button ) -> None:
        self.mp.random()
        self.pb.restart( self.mp.song_time() )
        self.t.set_text( self.mp.song_string() )

    def on_destroy( self, button ) -> None:
        self.mp.stop()
        self.pb.kill()
        Gtk.main_quit()


##  GLOBAL INSTANCES
mixer.init()
builder = Gtk.Builder()
builder.add_from_file( "ui.glade" )
progress_bar = builder.get_object( "songProgress" )
text_area = builder.get_object( "textArea" )

builder.connect_signals( Handler( mixer, progress_bar, text_area ) )

##  WINDOWS INIT
window = builder.get_object( "MainWindow" )
window.show_all()

Gtk.main()