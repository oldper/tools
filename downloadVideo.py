import shutil
import os
from pytube import YouTube
from pytube import Playlist
print( 'Input cmd :' )
print( '1. mp4 ' )
print( '2. mp3 ' )
print( '3. list' )
print( '0. quit ' )
cmd = eval(input())
while cmd != 0 :
    if cmd == 1:
        url = input( 'Input the url:' )
        yt = YouTube(url)
        print(yt.title)
        yt.streams.filter().get_highest_resolution().download()
        print( 'done' )
    elif cmd == 2:
        url = input( 'Input the url:' )
        yt = YouTube(url)
        print( yt.title )
        yt.streams.filter().get_audio_only().download()
        print( 'done' )
    elif cmd == 3 :
        url = input( 'Input the url:' )
        p = Playlist( url )
        print( p.title )
        print('1.Video')
        print('2.Music')
        cmd2 = eval(input())
        if cmd2 == 1 :
            os.mkdir( p.title )
            for video in p.videos:
                print( video.title )
                video.streams.filter().get_highest_resolution().download()
                source = video.title+'.mp4'
                dest = p.title+'/'+source
                shutil.move(source,dest)
        elif cmd2 == 2 :
            for video in p.videos:
                print( video.title )
                video.streams.filter().get_audio_only().download()
                source = video.title+'.mp3'
                dest = p.title+'/'+source
                shutil.move(source,dest)
        else:
            print( "error" )

    else :
        print( "error" )

    print( 'If  you want to quit enter \'0\'' )
    cmd = eval(input())
