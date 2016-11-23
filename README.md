Generate your very own 'Friends' episode name by running

    friends.py

Some episode titles I've gotten so far:

    The One where Phoebe Embezzles the Lettuce
    The One where Joey Exhumes the Bather
    The One where Ross Shears the Omelet
    The One with the Hamster

Basically comes from the observation that most 'Friends' episode titles follow
[the same format](https://en.wikipedia.org/wiki/List_of_Friends_episodes):
either "The One where (someone does something)" or "The One with (something)".
As a rough grammar this looks something like:

    S -> {S1,S2}
    S1 -> "The One where" Charactername V (Det N)
    S2 -> "The One with" {Det N,Charactername's N}

where

- Charactername = one of the main six 'Friends' characters
- V = a verb ending in 's'
- Det = "the"
- N = a noun

Not related to [Andy Pandy's](https://twitter.com/_Pandy) work, which generates
[entire episode scripts](http://fortune.com/2016/01/21/robot-friends-sequel/)
using TensorFlow.
