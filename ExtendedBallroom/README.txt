
####################################
Changelog:

09.19.2016: v1.1 : made corrections on tempo annotations thanks to Brandon Wu <b99901103@ntu.edu.tw>

07.22.2016: v1 : dataset used for the publication 'Scale and shift invariant time/frequency representation using auditory statistics: application to rhythm description' in IEEE MLSP 2016 workshop.

 

####################################
If you use this test-set, please cite:

    U. Marchand, G. Peeters. “Scale and shift invariant time/frequency representation using auditory statistics: application to rhythm description.” in IEEE International Workshop on Machine Learning for Signal Processing, September 2016.

or

    U. Marchand, G. Peeters, "The Extended Ballroom Dataset", in ISMIR 2016 Late-Breaking Session, New-York, USA.


####################################
Content of the test-set:

- extendedballroom_v1.1.xml contains all the metadata of the dataset in xml format.

- getExtendedBallroomDataset.py is the script to download the audio of the dataset. Typing 'python getExtendedBallroomDataset.py' should work on most configurations.


####################################
Audio files:

We do not provide audio files, use the script provided to download them.


####################################
Metadata:

The root node of the xml contains one genrenode for each genre class.

Each genrenode contains one songnode for each song belonging to that genre class.

Each songnode contains several informations:

- album: album name (scraped from the website)

- artist: artist name (scraped from the website)

- title: song title (scraped from the website)

- bpm: tempo in bpm (scraped from the website). From v1.1 some wrong/missing tempo annotations were manually corrected. In the case of varying tempo over the track, the average was taken.

- hash: md5 hash, used to check adequation of the audio

- version: indicates that this track is a version repetition of the song with the id provided

- exact: indicates that this track is an exact duplicate of the song with the id provided

- time: indicates that this track is an time duplicate of the song with the id provided

- karaoke: indicates that this track is an karaoke duplicate of the song with the id provided. (one of the two tracks have a 'voiced' attribute, meaning that the track is the version with voice)

