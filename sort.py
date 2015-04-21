import glob
import os

def mk_tree(path):
    #files to sort
    files = glob.glob(os.path.join(path, "*.pdf"))
    #creating directories to be filled with certain number of decoy .mol2 files
    chunks = [files[chunk:chunk+100] for chunk in range(0, len(files), 100)]
    for i, chunk in enumerate(chunks):
        new_dir = os.path.join(path, "pdf%05d" % i)
        os.mkdir(new_dir)
        for fn in chunk:
            os.rename(fn, os.path.join(new_dir, os.path.basename(fn)))
            
def main():
    mk_tree("Job_search")

if __name__ == '__main__':
    main()
