# Memory_Management

The program is written in Python 3.5 because python produces very readable code; we can switch to a different language if you guys would like.

The Reference_String.py module implements the creation of reference strings.  It creates a string object with the pages the program references in comma separated format.  (Note, it separates with a comma-space pair instead of just a comma.  e.g.:  "14, 99" instead of "14,99".)  If run on its own, the module generates such a string and writes it to a file.

The Memory Manager class implements the page replacement strategies. Initially two replacement strategies have been implemented - random replacement and FIFO replacement.  The constructor sets what algorithm an instance of the class implements and how many pages the "program" will be allowed to keep in memory (the resident set).  The class function handle_string reads the reference string and returns the number of page faults yielded.

