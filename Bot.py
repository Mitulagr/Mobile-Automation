import discord
from discord.ext import commands, tasks
import test

client = commands.Bot(command_prefix=["mab ","Mab ","MAB "])


@client.event
async def on_ready():
    print('Bot is online!')

@client.event
async def on_message(msg):
    if (msg.channel.id == 863770691902898196) : 
        m = (msg.content).split()
        for i in range (len(m)) : m[i] = m[i].lower()
        if('spotify' in m or 'song' in m or ('play' in m and 'movie' not in m and 'video' not in m)) and ('gaana' not in m) and ('ganna' not in m)  : 
            if(len(m)==1 and m[0]=='play') : test.pause()
            else :
                m2 = ""
                for i in m : 
                    if(i!='spotify' and i!='play' and i!='song') : m2 = m2 + i + " "
                test.spotify(m2)
        elif('gaana' in m or 'ganna' in m) : 
            m2 = ""
            for i in m : 
                if(i!='gaana' and i!='ganna' and i!='play' and i!='song') : m2 = m2 + i + " "
            test.gaana(m2) 
        elif('inshorts' in m or 'news' in m) : 
            test.inshorts_open()
            ctn = True
            while ctn : 
                if test.inshorts_swipe() : 
                    try : 
                        ms = await client.wait_for('message',timeout=15) 
                        ctn = False
                    except : ctn = True   
                test.up()           
        elif('prime' in m or 'movie' in m) : 
            m2 = ""
            for i in m : 
                if(i!='prime' and i!='video' and i!='vidoe' and i!='movie') : m2 = m2 + i + " "
            test.prime_video(m2)   
        elif('app' in m) :
            a = []
            for i in m : 
                try : a.append(int(i))
                except : pass
            test.app(a[0],a[1])   
        elif(m[0]=='type') :
            m2 = ""
            for i in m[1:] : m2 = m2 + i + " "
            test.type(m2)       
        elif('home' in m) : test.home()
        elif('back' in m) : test.back()    
        elif('off' in m) : test.off() 
        elif('on' in m) : test.on() 
        elif('volume' in m) : 
            a = m.count('up')
            for i in range(a) : test.volume_up()
            a = m.count('down')
            for i in range(a) : test.volume_down()  
        elif(('left' in m and 'swipe' in m) or ('right' in m and 'swipe' not in m)) : test.left()
        elif(('right' in m and 'swipe' in m) or ('left' in m and 'swipe' not in m)) : test.right()    
        elif(('up' in m and 'swipe' in m) or ('down' in m and 'swipe' not in m)) : test.up() 
        elif(('down' in m and 'swipe' in m) or ('up' in m and 'swipe' not in m)) : test.down() 
        elif('pause' in m or 'unpause' in m) : test.pause()
        elif('next' in m) : test.next()
        elif('prev' in m or 'previous' in m) : test.prev()
        elif('enter' in m) : test.enter() 
        elif(m[0]=='send') : test.wa_send()

client.run("ODYzNzY5MTY1Mjg1NDI1MTYy.YOrtuQ.cIa8hF1lTxgyRY_FQmCqaKtw0uU")
