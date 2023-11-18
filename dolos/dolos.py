import os
import argparse
from pptree import Node, print_tree


def is_dir_cgroup(dir: str) -> bool:
    """
    This function returns `True` if the given directory is a cgroup. This
    is determined by checking if the directory has a `cgroup.controllers` file.
    """
    for f in os.listdir(dir):
        if f == 'cgroup.controllers':
            return True
    return False


def build_tree(root_cgroup_path: str) -> Node:
    name = root_cgroup_path.split('/')[-1]
    root_node = Node(name)
    frontier = [(root_cgroup_path, root_node)]
    while len(frontier) > 0:
        path, node = frontier.pop()
        for f in os.listdir(path):
            path_to_f = path + '/' + f
            if os.path.isdir(path_to_f) and is_dir_cgroup(path_to_f):
                child_name = path_to_f.split('/')[-1]
                child_path = path_to_f
                child_node = Node(child_name, node)
                frontier.append((child_path, child_node))
    return root_node


def main():
    parser = argparse.ArgumentParser(
                    prog='dolos',
                    description='visualize the cgroup hierarchy')
    parser.add_argument('-r', '--root',
                        default='/sys/fs/cgroup',
                        help='path to the root cgroup (by default \
                            /sys/fs/cgroup)')
    parser.add_argument('-p', '--pretty',
                        default=True,
                        help="pretty-prints the hierarchy as a tree")
    args = parser.parse_args()
    cgroup_mount_point = args.root
    if cgroup_mount_point[-1] == '/':
        cgroup_mount_point = cgroup_mount_point[:-1]
    tree = build_tree(cgroup_mount_point)
    print_tree(tree)


if __name__ == '__main__':
    main()
