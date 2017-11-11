FILE *fd = fopen("MUL.py", "r");
PyRun_SimpleFileEx(fd, "MUL.py", 1); // last parameter == 1 means to close the
                                     // file before returning.
