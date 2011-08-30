def main():
    def inner():
        print inner.__name__
        print inner.redbug
        print inner.count
        inner.count += 1
        
    inner.redbug = "redbug"
    inner.count = 0    
    inner()
    inner()
    inner()

if __name__ == "__main__": main()