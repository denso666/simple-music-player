from os import listdir
from random import randint
from mutagen.mp3 import MP3
PATH="./songs/"

class MusicPlayer:
	def __init__( self, mixer ):
		self.__mixer = mixer
		self.__song_list = listdir( PATH )
		self.__index = 0	
		self.__paused = False

	def play( self ):
		self.__mixer.music.load( PATH + self.__song_list[ self.__index ] )
		self.__mixer.music.play()

	def toggle_pause( self ):
		if ( self.__paused ):
			self.__mixer.music.unpause()
		else:
			self.__mixer.music.pause()

		self.__paused = not self.__paused

	def stop( self ):
		self.__mixer.music.stop()

	def next( self ):
		self.__index += 1
		self.__index %= len( self.__song_list )

		self.__mixer.music.pause()
		self.play()

	def previous( self ):
		self.__index -= 1
		self.__index %= len( self.__song_list )

		self.__mixer.music.pause()
		self.play()

	def random( self ):
		self.__index = randint( 0, len( self.__song_list )-1 )
		self.__mixer.music.pause()
		self.play()

	def song_string( self ):
		songs = ""
		for i in range(0, len( self.__song_list ) ):
			s = "[{n}]: ".format( n=(i+1) )
			if ( i == self.__index ):
				s += ">> "
			
			s += self.__song_list[ i ] + "\n"
			songs += s
		
		return songs

	def song_time( self ) -> float:
		audio = MP3( PATH + self.__song_list[ self.__index ] )
		return audio.info.length