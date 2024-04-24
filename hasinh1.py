# khai bao cau hinh dau
#cau hinh ke tiep
#cau hinh cuoi
#in ra
n=int(input())
a=[0]*(n+1)

def ktao():
    for i in range(1,n+1):
        a[i]=0
def sinh():
    i=n
    while i>=1 and a[i]==1:
        a[i]=0
        i-=1
    if i==0:
        return False # cau hinh cuoi 
    else:
        a[i]=1
        return True
def main():
    ok = True
    ktao()
    while ok:
        for i in range(1,n+1):
            print(a[i] , end='')
        print()
        ok=sinh()
if __name__ == "__main__":
    main()
    
        
    
            
