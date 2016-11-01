# sylvester
A bot that generates a Markov chain based on text fed to it (Alice in Wonderland, by Lewis Carroll here) and spawns sentences using said Markov chain.

Bot functionality: Combs through Twitter for latest tweets containing a certain hashtag (#AliceInWonderland) here and retweets the last three of those with a comment. The text of the comment is generated using the Markov chain.


Libraries:

Tweepy - to connect to Twitter API

markovify - for Markov text generation. [https://github.com/jsvine/markovify]

