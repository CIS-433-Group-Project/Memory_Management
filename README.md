# Memory_Management
___
This project is a simulation of a memory management system for the purpose of defining well-behaved programs and to test
different page replacement strategies.  It is the term project for the Spring 2016 term of CIS 433, Operating Systems.
The group is Sean Abdoli, Alan Boggess, and Trent Jordan.

## Build
___
The project has been written in Python3.5, available from www.python.org.  It has no 3rd party dependencies.  As a
python project, it does not need to be built or compiled to run, you just need a Python version installed on your
system.

## Classes
___
### Reference Strings
The Reference_String.py module implements the creation of reference strings.  It defines a class to enumerate program
behavior types, but otherwise relies entirely on the method generate_list().  The method should be provided an Enum to
determine which behavior the reference string should have.  It returns a list of integers.

The main() method of Reference_String.py performs 100 trials to test assertions against entropy and to benchmark the
function, and writes the final trial to a .txt file.  Behaviors and the filename are currently hard-coded and must be
changed manually between tests.

### Page Replacement
The Page_Replacement.py class implements the page replacement strategies.  In a similar fashion to reference strings,
the page replacement strategies have been implemented in this module.  The module defines two classes:  an Enum as above
and a MemoryManager class, which implements the page replacement strategies.  The class's init() should be passed a
member of the Strategy Enum, an integer setting how many pages the class is allowed to use at once while handling
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