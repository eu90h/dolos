# dolos
dolos is a very small tool for displaying the cgroup hierarchy.

Usage is simple: execute `dolos` to pretty-print the `/sys/fs/cgroup` directory. If your cgroup dir is mounted somewhere else, try `dolos --root PATH_TO_ROOT_CGROUP`.

The output will look something like <img src="./example_output.png" alt="example output image" />
