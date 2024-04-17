import os

def main():
    for root,dirs,files in os.walk('.'):
        trees = filter(lambda f: f.startswith('tree'), files)
        trees = filter(lambda f: f.endswith('.txt'), trees)
        for tree_filename in trees:
            tree_filename = os.path.join(root,tree_filename)
            yaml_filename = tree_filename.replace('.txt','.yml')
            print(f'{tree_filename} → {yaml_filename}')
            with open(tree_filename,'r') as tree, open(yaml_filename,'w') as yaml:
                # the first line is special
                line = tree.readline().strip()
                prefix = 'Folder PATH listing for volume '
                assert line.startswith(prefix)
                volume = line[len(prefix):]
                yaml.write(f'volume: {volume}\n')
                # the second line is special
                line = tree.readline().strip()
                prefix = 'Volume serial number is '
                assert line.startswith(prefix)
                sn = line[len(prefix):]
                yaml.write(f'sn: {sn}\n')
                # the third line is special
                line = tree.readline().strip()
                suffix = ':\\'
                assert line.endswith(suffix)
                drive = line[:1]
                yaml.write(f'drive: {drive}\n')
                # the other lines are pattern
                yaml.write('tree:\n')
                for line in tree.readlines():
                    line = line.strip()
                    indent, item = line.split(sep='---', maxsplit=1)
                    indent = (len(indent)//4)+1
                    yaml.write(f'{indent*'  '}"{item}":\n')
                
if __name__=='__main__': main()
