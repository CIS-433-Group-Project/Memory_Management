# Memory_Management
This project is a simulation of a memory management system for the purpose of defining well-behaved programs and to test
different page replacement strategies.  It is the term project for the Spring 2016 term of CIS 433, Operating Systems.
The group is Sean Abdoli, Alan Boggess, and Trent Jordan.

## Build
The project has been written in Python3.5, available from www.python.org.  It has no 3rd party dependencies.  As a
python project, it does not need to be built or compiled to run, you just need a Python version installed on your
system.
## Modules
### Reference Strings
The Reference_String.py module implements the creation of reference strings.  It defines a class to enumerate program
behavior types, but otherwise relies entirely on the method generate_list().  The method should be provided an Enum to
determine which behavior the reference string should have.  It returns a list of integers.

The main() method of Reference_String.py performs 100 trials to test assertions against entropy and to benchmark the
function, and writes the final trial to a .txt file.  Behaviors and the filename are currently hard-coded and must be
changed manually between tests.

The following behaviors have been implemented:

 * Random
 * Extended Loop
 * Average (follows 90/10 rule, no further constraints)

### Page Replacement
The Page_Replacement.py module implements the page replacement strategies.  The module defines two classes:  an Enum as
above and a MemoryManager class, which implements the page replacement strategies.  The class's init() should be passed
a member of the Strategy Enum, an integer setting how many pages the class is allowed to use at once while handling
reference strings, and (optional) a boolean.  If the boolean is True, this instance of the class is allowed to adjust
the reference set of the objects it manages; if false, the resident set is statically set to the value passed.  (Default
behavior is static, i.e.:  False.)

The handle_string() method is the actual implementation of each page replacement strategy.  It should be passed a list
of integers (as produced by the reference_string.py module's generate_list() method) and an integer which sets an
initial limit of the resident set.  (0 is unlimited.)  The method returns the number of faults generated when handling
that list of pages with the parameters set in the class instance.

Presently, the following algorithms have been implemented:

 * First-In-First-Out
 * Random
 * Least-Recently-Used
 * Theoretical Optimal

 The module performs benchmark trials and assertion testing when run from the command-line.  It is not intended to be
 used to gather data.

### Driver
The page_driver.py module performs a series of trials for a given Behavior and Strategy as defined by the Enums in each
appropriate module.  For each trial it generates a new reference string of the appropriate behavior and parses it
according to the given strategy.  It computes/records average data for the trials and inserts it appropriately into
benchmarks.csv, a comma-separated-values file.  (Its contents are just plain text values, but it is intended to be read
by a spreadsheet managing program such as Microsoft Office.  It separates values by commas and lines by the Windows \r\n
pattern.)
## Results
The benchmarks.csv file provided here contains some sample results.  Note that because the driver module performs a set
of trials for each execution that each row in the results file represents an *average* result for a single *set* of
trials.  Actual variance can be significant for different program behaviors and replacement strategies.