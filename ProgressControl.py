from threading import Thread
from time import sleep

class ProgressControl( Thread ):
	def __init__( self, pb) -> None:
		super().__init__()
		self.time = 0
		self.pb = pb
		self.pb.set_fraction( 0.0 )
		self.paused = True
		self.alive = True
    
	def run( self ):
		while ( self.alive ):
			if ( not self.paused ):
				self.pb.set_fraction( self.pb.get_fraction() + ( 1 / self.time ) )
				sleep( 1 )

	def kill( self ) -> None:
		self.alive = False

	def restart( self, time: float ) -> None:
		self.pb.set_fraction( 0.0 )
		self.paused = False
		self.time = time

	def toggle_pause( self ) -> None:
		self.paused = not self.paused


