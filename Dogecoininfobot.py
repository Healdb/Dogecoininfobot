import time
import praw
import random
import re
import urllib2

# Login in to Reddit and the bot
r = praw.Reddit('dogecoininfobot')
r.login("dogecoininfobot","PASSWORD")

#a set for two-factor verification
already_done = set()

#initial summoning command, the bot doesnt have gold so I have to do it like this
Name = ['+/u/dogeinfo']

#defines all the summoning commands
help = ['+/u/dogeinfo Help']

grid = ['ASICs']

halve = ['The Halvening']

digital = ['Digital Currencies']

GPU = ['GPU', 'Mining']

mining = ['Mining']

scrypt = ['Scrypt', 'Mining']

attack = ['51% attack']

multi = ['Multipools']

doge = ['Dogecoin']

def find():
    try:
        print 'Starting bot...'
        subreddit_comments = r.get_comments('dogecoin',limit=100)
        for comment in subreddit_comments:
            author = comment.author
            op_text = comment.body
            tot = author.name
            #Defines the bot's username so it doesnt answer itself
            me = ['DogecoinInfoBot']
            has_praw = any(string in op_text for string in Name)
            has_name = any(string in tot for string in me)
            has_help = any(string in op_text for string in help)
            obj = open('seen_users.txt', 'ab+')
            #Checks to see if the comment.id is in the text file
            if comment.id in open("seen_users.txt").read():
                print 'That user has already been helped. Pausing for 1 second'
                time.sleep(1)
                pass
            else:
            	   #checks to see if the comment was made by the bot
                if has_name:
                    already_done.add(comment.id)
                    obj.write(comment.id )
                    obj.close()
                    time.sleep(3)
                    pass
                
                if comment.id not in already_done and has_help:
                	   #Im not exactly sure why I put this here, but it doesnt hurt anything. Ill clean it up later
                    print 'Found post! Replying now..'
                    comment.reply('Hi there! I am a Reddit bot owned by /u/healdb that helps people understand tough topics like what exacly a 51% attack is! My current list of commands is- \n\n* +/u/dogeinfo Help \n\n* +/u/dogeinfo Dogecoin \n\n* +/u/dogeinfo ASICs \n\n* +/u/dogeinfo The Halvening \n\n* +/u/dogeinfo Digital Currencies \n\n* +/u/dogeinfo GPU Mining \n\n* +/u/dogeinfo Mining \n\n* +/u/dogeinfo Scrypt Mining \n\n* +/u/dogeinfo 51% attack \n\n* +/u/dogeinfo Multipools \n\n* +/u/dogeinfo Dogecoin \n\nBe sure to capatalize the word you want defined! \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com)')
                    already_done.add(comment.id)
                    obj.write(comment.id )
                    obj.close()
                    time.sleep(3)
                    print 'Done! Starting over...'
                    break
                if comment.id not in already_done and has_praw:
                	   #looks for comments with the command +/u/dogeinfo
                    print 'Found post! Replying now..'
                    #Defines what the commands are relative to comment.body
                    has_grid = all(string in op_text for string in grid)
                    has_halve = all(string in op_text for string in halve)
                    has_digital = all(string in op_text for string in digital)
                    has_gpu = all(string in op_text for string in GPU)
                    has_mining = all(string in op_text for string in mining)
                    has_scrypt = all(string in op_text for string in scrypt)
                    has_attack = all(string in op_text for string in attack)
                    has_multi = all(string in op_text for string in multi)
                    has_doge = all(string in op_text for string in doge)
                    #Response list
                    if comment.id not in already_done and has_doge:
                        comment.reply('**Dogecoin** is a fun cryptocurrency featuring a Shiba Inu from the Doge Internet meme on its logo. It was introduced on December 8, 2013. Compared to other cryptocurrencies, Dogecoin has a fast initial coin production schedule: there will be approximately 100 billion coins in circulation by the end of 2014 with an additional 5.2 billion coins every year thereafter. Dogecoin is known for its friendly community and their generous contributions to various charities, including doge4water. Its free and easy to join the fun! \n\n[Wallet](http://dogecoin.com), [Community](http://reddit.com/r/dogecoin). \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(3)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_multi:
                        comment.reply('Multipools mine whatever coin is most profitable at the moment, and immediately sell it on the market for another coin, usually bitcoin. When multipools such as waffle pool control a significant amount of our global mining hashrate, it is detrimental to dogecoin because a huge amount are being dumped on the markets, increasing selling pressure. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(3)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_attack:
                        comment.reply('If one entity controlled 51% of the mining power of dogecoin, they could theoretically double spend coins before the block chain would notice. This would create a hard fork in the network. It is possible because the primary purpose of mining is to confirm transactions, as a reward, miners get dogecoins. Note that pools which control 51% of the mining network are not able to pull off a 51% attack on their own, they would need every member of their pool to not only agree, but to implement new code to do so. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_scrypt:
                        comment.reply('Scrypt mining, as opposed to SHA256 mining (bitcoin) is relatively new. So far, no one has developed ASICs for this algorithm. There are many claims on the internet that they exist, but nothing conrete, other than the gridseed USB powered ASICs, which dont do much better than GPUs. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_gpu:
                        comment.reply('GPU mining is the process of using a graphics card designed for gaming to generate dogecoins. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_digital:
                        comment.reply('A digital currency which is primarily used on the internet as a means of distributing anonymous, secure, fast, transaction fee-less currency. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_halve:
                        comment.reply('The halvening is when the reward from finding blocks goes down by half after every 100,000 blocks are found. \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_grid:
                        comment.reply('ASCIS are specialized computers not good for anything except mining crytocurrencies which use the scrypt algorithm. Much efficiency! \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                    if comment.id not in already_done and has_mining:
                        comment.reply('Mining is usually done in pools, so that anyone in the pool who finds a block (which is very rare) distributes the doge reward evenly among members of their pool \n\nCrypto mining can be done in many ways, through CPU, GPU, Scrypt, and ASICs. Please specify which method you would like an explanation for. Summon me again like this- +/u/dogeinfo GPU mining \n\n^I ^was ^made ^by ^/u/healdb ^through ^[bots4doge.com](http://bots4doge.com) \n\n^Reply ^to ^this ^bot ^with ^"+/u/dogeinfo ^Help" ^to ^see ^a ^full ^list ^of ^its ^commands')
                        time.sleep(5)
                        already_done.add(comment.id)
                        obj.write(comment.id )
                        obj.close()
                        print 'Done! Starting over...'
                        break
                

               

    except urllib2.HTTPError, err:
        if err.code == 404:
            time.sleep(5)
            break
        else:
            time.sleep(3)
            break
            
while True:
    find()
    time.sleep(10)
