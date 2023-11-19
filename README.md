# ccwc
A version of the Unix command line tool wc

This is a code challenge to build a version of the Unix command line tool wc from [The Coding Challenges](https://codingchallenges.fyi/challenges/intro/).

The description of the challenge can be found [here](https://codingchallenges.fyi/challenges/challenge-wc/)

This script simulate the `wc` command. It provides the options `-c`
, `-l`, `-w`, and `-m`. It also supports the default `wc` behaviour where no option is given, and accepts input from the stdin.

### Running the script

Make sure that you have python installed

* Clone the project and `cd` to the ccwc folder
* on Windows:
  * Run `python ccwc.py <option> <path_to_file>`
* On Linux/Unix
  * Run `ccwc <option> <path_to_file>`
  
You can compare the results with the ones given by `wc` with similar arguments.

If you have any issue feel free to create an issue or send me a message.
